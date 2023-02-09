import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from parser_goods.items import ParserGoodsItem


class CitilinkRuSpider(scrapy.Spider):
    name = "citilink_ru"
    allowed_domains = ["citilink.ru"]

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        # self.start_urls = [f"https://citilink.ru/search/?text={kwargs.get('query')}"]
        self.start_urls = ["https://citilink.ru/search/?text=Аксессуары+и+комплектующие+для+котлов"]

    def parse(self, response: HtmlResponse):
        pages_links = response.xpath("//div[@class='SearchResults']//a[contains(@class, 'ProductCardVertical__name')]")
        for link in pages_links:
            yield response.follow(link, callback=self.parse_goods)

    def parse_goods(self, response: HtmlResponse):
        loader = ItemLoader(item=ParserGoodsItem(), response=response)

        loader.add.xpath('name', "//h1/text()")
        loader.add.value('url', response.url)
        loader.add.xpath('price', "//div[@class='ProductHeader__price-block']//span[contains(@class, 'price-default_current-price')]/text()")
        loader.add.xpath('photos', "//img[contains(@class, 'PreviewList__image')]/@src")
        yield loader.load_item()