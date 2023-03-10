from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from parser_job.spiders.citilink_ru import CitilinkRuSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(CitilinkRuSpider, query='Аксессуары+и+коплектующие+для+котлов')

    reactor.run()