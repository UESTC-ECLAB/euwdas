# -*- coding: utf-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
import time
import pymongo
from pymongo import MongoClient
from multiprocessing.dummy import Pool as ThreadPool
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

if __name__ == '__main__':
	find = db.news.find().sort("news_time",pymongo.ASCENDING)
	for i in range(find.count()):
		print find[i]['_id']
		db.news.update({"_id":find[i]['_id']},{"$set":{"news_id":int(i)+1}})
		print find[i]['news_id']