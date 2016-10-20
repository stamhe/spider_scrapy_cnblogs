# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ScrapyDemo2Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title   = Field()   # 标题
    desc    = Field()   # 摘要
    link    = Field()   # 链接
