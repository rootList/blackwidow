#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 2018年3月21日
@author: chentao
'''
from https import httpthread
from https import HttpClient
from https import urlparser
import time

# domain_name="http://www.booktxt.net"
# MAIN_URL = "http://www.booktxt.net/5_5417"
 
#域名
domain_name="https://www.booktxt.net/"
#目录页面
MAIN_URL = "https://www.booktxt.net/2_2219/"

URL_MAP = {} #所有章节
URL_LIST = [] #所有章节按顺序存放
ALL_CONTENT = {}

# 获取所有章节的url
def getAllUrl():
    url_content = HttpClient.getUrl(MAIN_URL)
    urlparser.parserCat(url_content, URL_MAP, URL_LIST, domain_name)
    

getAllUrl()

now = time.time()
threads = []
for i in range(1, 20):
    thread = httpthread.urlThread(i,str(i)+"thread", URL_LIST, ALL_CONTENT)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread", time.time() - now)

row = len(ALL_CONTENT)
with open(u'C:\\document\\圣墟.txt', mode='w', encoding='utf-8') as f:
    for i in range(1, row+1):
        for key in ALL_CONTENT:
            if key+1 == i:
                f.write(ALL_CONTENT[key])
                break
        
print("use time", time.time() - now)