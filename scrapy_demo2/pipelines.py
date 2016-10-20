#!/usr/bin/python
#coding=utf-8
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  

class ScrapyDemo2Pipeline(object):
    def __init__(self):
        self.file = open("hequan.json", "w+")

    def process_item(self, item, spider):
        # 此处如果有中文的话，要加上ensure_ascii=False参数，否则可能出现乱码
        record = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(record)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()
