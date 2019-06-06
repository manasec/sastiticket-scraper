# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    Platform = scrapy.Field()
    offerdetails = scrapy.Field()
    channel = scrapy.Field()
    category = scrapy.Field()
    coupon = scrapy.Field()
    bankwallet = scrapy.Field()
    constraints = scrapy.Field()
    validity = scrapy.Field()
    minimumamount = scrapy.Field()


