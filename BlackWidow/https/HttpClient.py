# -*- coding=utf-8 -*-
'''
Created on 2018年3月20日
@author: chentao

'''
from urllib import request  
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    

def getUrl(url):
    req = request.Request(url=url, headers = headers)
    response = request.urlopen(req)
    res = response.read()
    return res.decode("GBK") 
