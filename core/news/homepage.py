# -*- coding: utf-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
import time
import pymongo
from pymongo import MongoClient
from handler.news import News
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

def homepage_rec():
    #TODO:user_id
    template_variables = {}
    rec_news = db.news.find({"show":1}).sort("news_time",pymongo.DESCENDING)
    homepage_news = []
    for i in range(10):
        one_news = {}
        news = News(rec_news[i]['news_id'])
        one_news['title'] = news.title
        one_news['tags'] = news.tags
        one_news['news_time'] = news.news_time
        one_news['author'] = news.author
        one_news['news_avatar'] = news.news_avatar
        homepage_news.append(one_news)
    template_variables['homepage_news'] = homepage_news
    return template_variables

