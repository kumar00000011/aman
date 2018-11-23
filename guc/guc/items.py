# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GucItem(scrapy.Item):
    link=scrapy.Field()
    image=scrapy.Field()
    uuid=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
