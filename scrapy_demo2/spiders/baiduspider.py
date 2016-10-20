#!/usr/bin/python
#coding=utf-8
# @hequan

from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy_demo2.items import ScrapyDemo2Item
from scrapy.linkextractors import LinkExtractor
import re

from scrapy.spiders import CrawlSpider

class scrapy_demo2(CrawlSpider):
    # 爬虫的识别名称，必须是唯一的，在不同的爬虫中你必须定义不同的名字
    name = "scrapydemo2"    # 设置爬虫名称

    # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = ["cnblogs.com"] # 设置允许的域名

    # 爬取的url列表，爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始，其他子url将会从这些起始url中继承性生成
    start_urls = [
            'http://www.cnblogs.com/artech/default.html?page=1',
            'http://www.cnblogs.com/artech/default.html?page=2',
    ]


    # 解析的方法，调用的时候传入从每一个url传回的response对象作为唯一参数，负责解析并获取抓取的数据(解析为item)，跟踪更多的url
    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//div[@class="forFlow"]/div[@class="day"]')
        items = []
        for article in articles:
            item = ScrapyDemo2Item()
            item['title']   = article.xpath('div[@class="postTitle"]/a/text()').extract()
            item['desc']    = article.xpath('div[@class="postCon"]/div/text()').extract()
            item['link']    = article.xpath('div[@class="postTitle"]/a/@href').extract()
            items.append(item)

        return items


