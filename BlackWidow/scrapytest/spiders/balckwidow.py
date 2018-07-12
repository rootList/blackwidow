#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from scrapytest.items import CatalogueItem
from scrapy.crawler import CrawlerProcess

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://www.800txt.net"]
    start_urls = [
        "http://www.800txt.net/book_38021/"
       # "http://www.booktxt.net/5_5417/2020673.html"
    ]

    def parse(self, response):
#         filename = response.url.split("/")[-2]
#         print filename
#         items = ScrapytestItem()
#         items["title"]=response.xpath('//h1/text()').extract()
#         items["content"] = response.xpath('//div[@id="content"]/text()').extract()
#         bootemSelectors = response.xpath('//div[@class="bottem1"]/a')
#         for bootemSelector in bootemSelectors:
#             data= bootemSelector.xpath("text()").re('上一章')
#             print data
        print(response.body.decode("GBK"))
        with open("ml.txt", 'w') as f:
#             f.write(items["title"][0].encode('utf-8'))
#             for c in items["content"]:
#                 c = c.strip()
#                 if c.strip() != "":
#                     f.write(c.encode('utf-8')+"\n")
            f.write(response.body.decode("GBK"))
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(DmozSpider)
process.start()
