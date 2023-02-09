import scrapy
from itemloaders.processors import MapCompose, Compose, TakeFirst
from twisted.web.html import output


def clean_price(value):
   try:
      value = value[0].replace('', '').replace('\n', '')
      value = list(value)
   except:
      return value
   return value

class ParserGoodsItem(scrapy.Item):
   name = scrapy.Field(output_processor=TakeFirst())
   url = scrapy.Field(output_processor=TakeFirst())
   price = scrapy.Field(input_processor=Compose(clean_price), output_processor=TakeFirst())
   photos = scrapy.Field()
   _id = scrapy.Field()

