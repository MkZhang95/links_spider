import scrapy
from links_spider.modules.domain_list import parsable_domain_list as domains, moddules
from links_spider.modules.start_urls import urls
from links_spider.items import LinkItem
from scrapy.http import Request
from links_spider.modules.waybackapi import WayBackApi
import sqlite3

class linksParser(scrapy.Spider):

    name = "links"
    start_urls = urls

    handle_httpstatus_list = [301, 302, 400, 404, 500]



    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        con = sqlite3.connect('links.db')
        cur = con.cursor()
        value = (response.request.url,)
        cur.execute("SELECT source_link FROM link where source_link =? and status != 'no_scraper'", value)
        print(cur.fetchone())
        exist = cur.fetchone()
        cur.close()
        if exist:
            print("The link has been crawled ")
        else:
            link_item = LinkItem()
            print("aaaaaa")
            source_status = WayBackApi(response.request.url, "none").way_back_find()
            print(source_status)
            if source_status == "dead":
                link_item['source_link'] = response.request.url
                link_item['status'] = 'dead'
                yield link_item
            else:
                for i in range(len(domains)):
                    parseable = "FALSE"
                    if domains[i] in response.url:
                        parseable = "TRUE"
                        motheringParser = moddules[i](source_status)
                        try:
                            date = motheringParser.get_date()
                        except Exception as e:
                            date = 'No date'
                        target_link = motheringParser.get_all_links()
                        if target_link:
                            for link in target_link:
                                link_item['target_link'] = link
                                link_item['source_date'] = date
                                if "web.archive.org" not in source_status:
                                    link_item['source_link'] = source_status
                                    link_item['status'] = 'OK'
                                    yield link_item
                                else:
                                    source_link = "http" + source_status.split("/http")[1]
                                    link_item['source_link'] = source_link
                                    link_item['status'] = 'archived'
                                    link_item['archived_link'] = source_status
                                    yield link_item
                                link_status = WayBackApi(link, date).way_back_find()
                                print(link_status)
                                if link_status == "dead":
                                    if "web.archive.org" not in link:
                                        link_item['source_link'] = link
                                    else:
                                        source_link = "http" + link.split("/http")[1]
                                        link_item['source_link'] = source_link
                                    link_item['target_link'] = None
                                    link_item['source_date'] = None
                                    link_item['status'] = 'dead'
                                    yield link_item
                                elif link_status == link:
                                    yield Request(response.urljoin(link), callback=self.parse, dont_filter=True)
                                else:
                                    yield Request(response.urljoin(link_status), callback=self.parse, dont_filter=True)

                        else:
                            if "web.archive.org" not in source_status:
                                link_item['source_link'] = source_status
                            else:
                                source_link = "http" + source_status.split("/http")[1]
                                link_item['source_link'] = source_link
                            link_item['source_date'] = date
                            link_item['status'] = 'No link'
                            if "web.archive.org" not in source_status:
                                yield link_item
                            else:
                                link_item['archived_link'] = source_status
                                yield link_item
                        break
                if parseable == "FALSE":
                    link_item['status'] = "no_scraper"
                    if "web.archive.org" not in source_status:
                        link_item['source_link'] = source_status
                        yield link_item
                    else:
                        source_link = "http" + source_status.split("/http")[1]
                        link_item['source_link'] = source_link
                        link_item['archived_link'] = source_status
                        yield link_item




        '''
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
        '''






