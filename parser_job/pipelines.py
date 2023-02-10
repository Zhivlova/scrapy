from itemadapter import ItemAdapter
from pymongo import MongoClient


# class ParserJobPipeline:
#     def __init__(self):
#         client = MongoClient('localhost:27017')
#         self.mongo_db = client.parser_job
#     def process_item(self, item, spider):
#         item["salary"] = self.clean_salary(list_salary=item["salary"])
#         collection = self.mongo_db[spider.name]
#         collection.insert_one(item)
#
#         return item
#
#     def clean_salary(self, list_salary):
#         min_salary = None
#         max_salary = None
#         currency_salary = None
#         tax_salary = None
#
#         for i in range(len(list_salary) - 1):
#             if list_salary[i] == 'от':
#                 min_salary = int(list_salary[i + 1].replace('\xa0', ''))
#             elif list_salary[i] == 'до':
#                 max_salary = int(list_salary[i + 1].replace('\xa0', ''))
#         if min_salary or max_salary:
#             currency_salary = list_salary[-3]
#             tax_salary = list_salary[-1]
#
#         return {
#             'min_salary': min_salary,
#             'max_salary': max_salary,
#             'currency_salary': currency_salary,
#             'tax_salary': tax_salary,
#         }


class InstaparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.instagram

    def process_item(self, item, spider):
        collection = self.mongobase[item.get('username')]
        collection.insert_one(item)
        return item