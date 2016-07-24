# -*- coding: utf-8 -*-
import os
import sys
import json
from flask import current_app, Blueprint, render_template, abort, request, flash, redirect, url_for,jsonify
from handler.news import News
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
reload(sys)
sys.setdefaultencoding('utf-8')
db = client.eclab

news = Blueprint('news', __name__, template_folder='templates')

@news.route('/news', methods=['GET','POST'])
def newspage():
    print 'test'
    return 'test'

@news.route('/homepagenews', methods=['GET','POST'])
def homepage_news():
    username = request.values.get('username', '')
    # if username == 'anonymous':
    candidate_news = db.news.find({"show":1}).sort("news_time",pymongo.DESCENDING)
    recommend_news = []
    for i in range(10):
    	one_news = {}
        news = News(candidate_news[i]['news_id'])
        one_news['title'] = news.title
        one_news['tags'] = news.tags
        one_news['news_time'] = news.news_time
        one_news['author'] = news.author
        one_news['news_avatar'] = news.news_avatar
        recommend_news.append(one_news)
    return jsonify({'news':recommend_news})
