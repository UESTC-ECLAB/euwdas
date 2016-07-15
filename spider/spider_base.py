# -*- coding: utf-8 -*-
import requests
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
from multiprocessing.dummy import Pool as ThreadPool
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

class baseSpider(object):
    def __init__(self):
        pass

    def generateHtml(self, url):
        r = requests.get(url)
        if r.encoding != 'utf-8':r.encoding='utf-8'
        html = r.content
        html.replace(u'&nbsp;','***')
        html = html.split(u'&nbsp;')
        html = '***'.join(html)
        return html

    def generateUrlList(self, url):
        html = self.generateHtml(url)
        soup = BeautifulSoup(html)
        url_list = []
        return url_list

    def extractContent(self, url):
        html = self.generateHtml(url)
        soup = BeautifulSoup(html)
        post = {}
        return post

    def mainSpider(self, url):
        url_list = self.generateUrlList(url)
        for i in range(len(url_list)):
            link = urlList[i]
            find = db.news.find_one({"original_url":""})
            if str(find) == 'None':
                post = self.extractContent(link)
                if post != 'None':
                    db.news.insert_one(post)