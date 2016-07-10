# -*- coding: utf-8 -*-
import requests
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from bs4 import BeautifulSoup
import time
# from pymongo import MongoClient
# from multiprocessing.dummy import Pool as ThreadPool
# client = MongoClient()
# client = MongoClient('localhost', 27017)
# db = client.news

class baseSpider(object):
    def __init__(self):
        pass

    def method1(self):
        pass

class memectSpider(baseSpider):
    def __init__(self):
        pass

    def method1(self):
    	self.method2()
        print 'hh'

    def method2(self):
    	print 'method2'
        

if __name__ == '__main__':
    m = memectSpider()
    m.method1()
    print 'end'