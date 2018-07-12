#!/usr/local/bin/python2.7
# encoding: utf-8
import html.parser as h

class MyHTMLParser(h.HTMLParser):
    is_catalog = False #是否是目录
    catalog = ""#目录内容
    temp_url=""
    pre_url="" #上一页url
    is_pre=False # 是否是上一页
    
    next_url="" #下一页url
    is_next = False # 是否是下一页
    is_content=False # 是否是正文内容
    content = "" # 正文内容
    
    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        if tag.startswith('div'):
            if attrs[0][1] == "content":
                self.is_content=True
        if tag.startswith('h1'):
            self.is_catalog=True
        if tag.startswith('a'):
            self.is_next=True
            self.temp_url=attrs[0][1]
            self.is_pre=True
            
    #处理<xx>data</xx>中间的那些数据
    def handle_data(self, data):
        if self.is_content is True and data.strip() != "":
            self.content += data.strip()+"\n"
        if self.is_catalog is True:
            self.catalog = data.strip()
        if self.is_next is True and data.find("下一章") != -1:
            self.next_url = self.temp_url
        if self.is_next is True and data.find("上一章") != -1:
            self.pre_url = self.temp_url
    #处理结束标签，比如</xx>或者<……/>
    def handle_endtag(self, tag):
        if tag == "div":
            self.is_content=False
            self.is_catalog=False
        if tag == "h1":
            self.is_catalog=False
        if tag == "a":
            self.is_next=False

def parserContent(content):
    p=MyHTMLParser()
    p.feed(content)
    p.close()
    return p
# p=MyHTMLParser()
# with open('C:\\document\\text.txt', mode='r') as f:
#         text = f.readlines()
#         content = ""
#         for str in text:
#             content+=str
#   
# p.feed(content)
# p.close()
# print(p.catalog)
# print(p.content)
# print(p.pre_url)
# print(p.next_url)