from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class ParserGoodsPipeline:
    def process_item(self, item, spider):
        return item

class CitilinkPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):

        if item['photos']:
            for img in item['photos']:
                try:
                    yield Request(img)
                except Exceptionas e:
                    print(e)

    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item