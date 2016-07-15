# -*- coding: utf-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
import time
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

class News(object):
    def __init__(self, news_id = None, title = None, content = None,\
                tags = None, news_url = None, image_url = None, \
                news_avatar = None, news_time = None
                ):
        self.news_id = news_id
        news = self.set_by_id(self.news_id)
        self.title = news["title"]
        self.content = news["content"]
        self.tags = news["tags"]
        self.news_url = news["news_url"]
        self.news_avatar = news["news_avatar"]
        self.news_time = news["news_time"]
        self.author = news["author"]

    def set_by_id(self, news_id):
        news = db.news.find_one({"news_id":news_id})
        return news

if __name__ == '__main__':
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
	print template_variables





