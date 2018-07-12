# -*- coding: utf-8 -*-
'''
Created on 2018年3月26日

@author: chentao
'''
import scrapy.cmdline  
  
if __name__ == '__main__':  
    scrapy.cmdline.execute(argv=['scrapy','crawl','dmoz'])  