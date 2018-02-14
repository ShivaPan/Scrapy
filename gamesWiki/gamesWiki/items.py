# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class GameswikiItem(scrapy.Item):
    title = scrapy.Field()
    sales = scrapy.Field()
    release = scrapy.Field()
    genre = scrapy.Field()
    developer = scrapy.Field()
    publisher = scrapy.Field()
    
