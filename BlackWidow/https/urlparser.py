#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 2018年3月21日

@author: chentao
'''
import html.parser as h
import re

pre="http://www.booktxt.net"
# 从主页中解析所有章节的url
class UrlParser(h.HTMLParser):
    
    def __init__(self, URL_MAP, URL_LIST, MAIN_URL):
        h.HTMLParser.__init__(self)
        self.URL_MAP = URL_MAP
        self.MAIN_URL = MAIN_URL
        self.URL_LIST = URL_LIST
    
    temp = False
    is_start = False# 目录开始 
    is_url = False
    tempUrl=""
    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        if tag.startswith('a'):
            for attr in attrs:
                if attr[0]=="href":
                    self.tempUrl = attr[1]
                    self.is_url=True
                    break
        if tag.startswith('dt'):
            self.temp = True 
            
    #获取章节和对应的url
    def handle_data(self, data):
        if self.temp == True and self.is_start == False:
            start = re.findall(".*正文.*", data)
            if len(start) == 0:
                self.temp = False   
            else:
                self.is_start = True  
                
        if self.is_start:
            matchObj = re.match('第.{1,}章', data)
            if matchObj:
                #print matchObj.group()
                self.URL_MAP[matchObj.group()] = pre+self.tempUrl
                self.URL_LIST.append(self.MAIN_URL+self.tempUrl)
        
#         matchObj = re.match('第.{1,}章', data, re.M|re.I)
#         if matchObj:
#             #print matchObj.group()
#             self.URL_MAP[matchObj.group()] = pre+self.tempUrl
#         pass
    
    #处理结束标签，比如</xx>或者<……/>
    def handle_endtag(self, tag):
        if tag == "a":
            self.is_url=False

def parserCat(content, URL_MAP,URL_LIST, MAIN_URL):
    p= UrlParser(URL_MAP, URL_LIST, MAIN_URL)
    p.feed(content)
    p.close()
    
# URL_MAP = {}
# p= UrlParser()
# with open('C:\\document\\zj.txt', mode='r') as file:
#     text = file.readlines()
#     content = ""
#     for str in text:
#         content+=str
#     p.feed(content)
#     p.close()
#     for key in URL_MAP:
#         print "key",key, URL_MAP[key]