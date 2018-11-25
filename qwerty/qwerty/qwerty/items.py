# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QwertyItem(scrapy.Item):
    name=scrapy.Field()
    uuid=scrapy.Field()
    link=scrapy.Field()
    crawled_from=scrapy.Field()
    price=scrapy.Field()
    brand=scrapy.Field()
    image=scrapy.Field()
