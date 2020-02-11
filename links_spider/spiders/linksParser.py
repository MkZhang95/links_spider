import scrapy
from links_spider.modules.domain_list import parsable_domain_list as domains, moddules
from links_spider.modules.start_urls import urls
from links_spider.items import LinkItem
from scrapy.http import Request
from links_spider.modules.waybackapi import WayBackApi


class linksParser(scrapy.Spider):

    name = "links"
    start_urls = urls

    handle_httpstatus_list = [301, 302, 400, 404, 500]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        link_item = LinkItem()
        orginal_status = WayBackApi(response.request.url, "none").way_back_find()
        print(orginal_status)

        for i in range(len(domains)):
            parsable = "FALSE"
            if domains[i] in response.url:
                parsable = "TRUE"
                motheringParser = moddules[i](response.request.url)
                try:
                    date = motheringParser.get_date()
                except Exception as e:
                    date = 'No date'
                target_link = motheringParser.get_all_links()
                if target_link:
                    for link in target_link:
                        link_item['source_link'] = response.request.url
                        link_item['target_link'] = link
                        link_item['source_date'] = date
                        link_status = WayBackApi(link, date).way_back_find()
                        print(link_status)
                        if link_status == "dead":
                            link_item['status'] = 'dead'
                            yield link_item
                        elif link_status == link:
                            link_item['status'] = 'OK'
                            yield link_item
                            yield Request(response.urljoin(link), callback=self.parse, dont_filter=True)
                        else:
                            link_item['status'] = 'archived'
                            yield link_item
                            yield Request(response.urljoin(link_status), callback=self.parse, dont_filter=True)
                else:
                    link_item['source_link'] = response.request.url
                    link_item['source_date'] = date
                    link_item['status'] = 'No link'
                    yield link_item
                break

        if parsable == "FALSE":
            link_item['source_link'] = response.request.url
            link_item['status'] = "no_scraper"
            yield link_item






