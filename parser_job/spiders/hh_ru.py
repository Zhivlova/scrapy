import scrapy
from scrapy.http import HttpResponse


class HhRuSpider(scrapy.Spider):
    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://hh.ru/search/vacancy?area=88&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&text=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA'
                  ]

    def parse(self, response: HttpResponse):
        print('\n################\n%s\n################\n'% response.url)
