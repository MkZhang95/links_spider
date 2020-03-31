from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from links_spider.resolver import RedisResolver

class XCrawlerProcess(CrawlerProcess):

    def _get_dns_resolver(self):
        return RedisResolver(
            reactor=reactor,
            timeout=self.settings.getfloat('DNS_TIMEOUT')
        )

settings = get_project_settings()
process = XCrawlerProcess(settings)

process.crawl('links_spider')
process.start()