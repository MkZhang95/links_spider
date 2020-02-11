# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LinksSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LinkItem(scrapy.Item):
    source_link = scrapy.Field()
    target_link = scrapy.Field()
    status = scrapy.Field()
    source_date = scrapy.Field()
