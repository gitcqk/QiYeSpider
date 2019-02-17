# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QyxxItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    id_code = scrapy.Field()
    url_x = scrapy.Field()
    people = scrapy.Field()
    time = scrapy.Field()
    zhuangtai = scrapy.Field()