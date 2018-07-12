#!/usr/local/bin/python2.7
# encoding: utf-8
'''

'''
import threading
from https import HttpClient
import re
import htmlparser
from time import sleep
from warnings import catch_warnings
threadLock = threading.Lock()

class urlThread(threading.Thread):
    def __init__(self, threadID, name, URL_LIST, ALL_CONTENT):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        #self.URL_MAP = URL_MAP
        self.URL_LIST = URL_LIST
        self.ALL_CONTENT = ALL_CONTENT
      
    #从任务队列中获取一个任务，并执行
    def run(self): 
        while True:
            try:
                threadLock.acquire()
                num, url = getWork(self.URL_LIST)
                threadLock.release()
                if num == None:
                    break
                content = getUrl(url)
                p = htmlparser.parserContent(content)
                self.ALL_CONTENT[num] = p.catalog+"\n"+p.content
            finally:
                pass
def getUrl(url):
    return HttpClient.getUrl(url)

# 获取任务数
def getWork(URL_LIST):
    if len(URL_LIST) > 0:
        print("left", len(URL_LIST))
        return (len(URL_LIST)-1, URL_LIST.pop(len(URL_LIST)-1))
    else: 
        return (None,None)
    
