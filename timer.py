# -*- coding: utf-8 -*-
import requests
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from spider.spider_memect import memectSpider

class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'test',
            'func': 'timer:test',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
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
	url = ['http://forum.memect.com/page/1',
		   'http://forum.memect.com/page/2',
		   'http://forum.memect.com/page/3',
		  ]
	for i in range(len(url)):
		memectSpider().mainSpider(url[i])

if __name__ == '__main__':
	print 'tt'