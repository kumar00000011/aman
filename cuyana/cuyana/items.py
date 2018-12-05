# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CuyanaItem(scrapy.Item):
    brand=scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
    sub_category_link=scrapy.Field()
    sub_category_title=scrapy.Field()
