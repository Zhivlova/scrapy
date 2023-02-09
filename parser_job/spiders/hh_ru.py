import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ParserJobItem


class HhRuSpider(scrapy.Spider):
    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://hh.ru/search/vacancy?area=88&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&text=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA'
                  ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vacancies_links = response.xpath("//a[@data-qa='vacancy-serp__vacancy-title']/@href").getall()
        for link in vacancies_links:
            yield response.follow(link, callback=self.parse_vacancy)
        print('\n################\n%s\n################\n'% response.url)

    def parse_vacancy(self, response: HtmlResponse):
        vacancies_name = response.css("h1::text").get()
        vacancies_salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        vacancies_url = response.url

        yield ParserJobItem(
            name=vacancies_name,
            salary=vacancies_salary,
            url=vacancies_url
        )

        print('\n****************\n%s\n%s\n%s\n****************\n'%(
            vacancies_name,
            vacancies_salary,
            vacancies_url

        ))
