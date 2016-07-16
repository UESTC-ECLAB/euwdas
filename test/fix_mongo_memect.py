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

def drop():
	find = db.news.find({"show":1})
	print find.count()
	for i in range(find.count()):
		news = find[i]
		if news['show'] == 1:
			new_find = db.news.find({"show":1,"content":news['content']})
			if new_find.count() >= 2:
				for j in range(1,new_find.count()):
					print j
					db.news.update({"_id":new_find[j]['_id']},{'$set':{"show":0}})

if __name__ == '__main__':
	# find = db.news.find({"show":1})
	# drop = [u'日报',u'iOS',u'Android',u'安卓']
	# print find.count()
	# for i in range(find.count()):
	# 	print i*1.0/find.count()
	# 	news = find[i]
	# 	# print news
	# 	for j in range(len(drop)):
	# 		if drop[j] in news['title'] or drop[j] in news['tags']:
	# 			db.news.update({"_id":news['_id']},{"$set":{"show":0}})
	# 	# break
	while 1:
		try:
			drop()
		except:
			print 'error'


			# print db.news.find({"show":1,"content":news['content']}).count()
		# break



