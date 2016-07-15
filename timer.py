# -*- coding: utf-8 -*-
import requests
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from spider.spider_memect import memectSpider
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'test',
            'func': 'timer:test',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10000
        },
        {
            'id': 'memect',
            'func': 'timer:memect',
            'args': (),
            'trigger': {
                'type':'cron',
                'hour': '3,6,13,20'
            }
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True

def test(a, b):
    print 'test'
    print a,b

def memect():
    post = {"task_time":str(time.strftime("%Y-%m-%d %H:%M", time.localtime())), 
            "task_name" : "memect_spider",
            }
    url = ['http://forum.memect.com/page/1',
           'http://forum.memect.com/page/2',
           'http://forum.memect.com/page/3',
          ]
    try:
        for i in range(len(url)):
            memectSpider().mainSpider(url[i])
        post["success"] = 'yes'
    except:
        post["success"] = 'no'
        post["failed_reason"] = 'some reason'
    db.timer.insert_one(post)
