# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GucciItem(scrapy.Item):
    name=scrapy.Field()
    price=scrapy.Field()
    image=scrapy.Field()
    link=scrapy.Field()
    uuid=scrapy.Field()
    crawled_from=scrapy.Field()
