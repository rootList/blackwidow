# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#章节的目录和内容
class ContentItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    
#目录item
class CatalogueItem(scrapy.Item):
    Url_List = []
    
