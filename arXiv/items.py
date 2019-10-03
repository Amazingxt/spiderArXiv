# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArxivItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()

    abstract = scrapy.Field()

    url = scrapy.Field()

    authors = scrapy.Field()

    major = scrapy.Field()
