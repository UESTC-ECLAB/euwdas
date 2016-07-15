# -*- coding: utf-8 -*-

import os
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

class News(object):
    def __init__(self, news_id = None, title = None, content = None,\
                tags = None, news_url = None, image_url = None, \
                news_avatar = None, news_time = None, author = None
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
