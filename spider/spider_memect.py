# -*- coding: utf-8 -*-
import requests
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
from spider_base import baseSpider
from multiprocessing.dummy import Pool as ThreadPool
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

class memectSpider(baseSpider):
    def __init__(self):
        self.dropwords = [u'日报',u'iOS',u'Android']

    def generateHtml(self, url):
        r = requests.get(url, timeout=10)
        if r.encoding != 'utf-8':r.encoding='utf-8'
        html = r.content
        html.replace(u'&nbsp;','***')
        html = html.split(u'&nbsp;')
        html = '***'.join(html)
        return html

    def generateUrlList(self, url):
        html = self.generateHtml(url)
        soup = BeautifulSoup(html)
        content = soup.find_all("div", attrs={"class": "f-floatright"})
        content = content[1:]
        # print content

        url_list = []
        for i in range(len(content)):
            item = content[i]
            title = item.find('h2', {'class': 'title'}).get_text()
            title = str(title).strip()
            if u'日报' not in title:
                # print title
                url_list.append(item.find('h2', {'class': 'title'}).find('a').get('href'))
        # print url_list
        return url_list

    def extractContent(self, url):
        dropwords = self.dropwords
        # print url
        html = self.generateHtml(url)
        soup = BeautifulSoup(html)

        try:
            title = soup.find('h1', {'class' : 'title-thread'}).get_text()
            for i in range(len(dropwords)):
                if dropwords[i] in title:
                    return 'None'
        except:
            return 'None'
        # print title

        try:
            soup = soup.find('div', {'class' : 'items-thread item-thread clearfix'})
        except:
            return 'None'

        # 标签
        try:
            tag_soup = soup.find('div', {'class':'keyword-wrapper'}).find_all('span')
            tags = [tag_soup[i].string for i in range(len(tag_soup))]
            if tags != []:
                for i in range(len(tags)):
                    if tags[i] in dropwords:
                        return 'None'
        except:
            tags = []
        # print tags

        
        # 作者
        try:
            author = soup.find('span', {'style':"font-size:14px"}).b.get_text()
        except:
            author = ''
        # print author

        # 头像图片
        try:
            news_avatar = soup.find('a', {'class':"profile_image_wrapper"}).img.get('src')
        except:
            return 'None'
        # print news_avatar

        # 时间
        try:
            news_time = soup.find('span', {'class':"datetime"}).get_text()
        except:
            return 'None'
        # print news_time

        #内容和网址
        try:
            news_url = soup.find('div', {'class':"text"}).find('a').get('href')
        except:
            news_url = ''

        try:
            soup.find('div', {'class':"text"}).a.decompose()
            content = soup.find('div', {'class':"text"}).get_text().strip()
        except:
            return "None"
        # print content,news_url

        # 图片
        try:
            image_url = soup.find('div', {'class': 'original_pic'}).find('img').get('src')
        except:
            image_url = ''

        post = {'title':title, 'tags':tags, 'author':author, 'content':content,\
                'news_url':news_url, 'original_url':url, 'image_url':image_url, \
                'news_avatar':news_avatar,'news_time':news_time, }
        return post


    def mainSpider(self, url):
        url_list = self.generateUrlList(url)
        for i in range(len(url_list)):
            link = url_list[i]
            find = db.news.find_one({"original_url":""})
            if str(find) == 'None':
                post = self.extractContent(link)
                if post != 'None':
                    # print post
                    post['insert_time'] = str(time.strftime("%Y-%m-%d %H:%M", time.localtime()))
                    post['show'] = 1
                    post['news_id'] = int(db.news.find().count())+1
                    db.news.insert_one(post)
                    if post['tags'] != {}:
                        for i in range(len(post['tags'])):
                            post_tag = {"tag" : post['tags'][i], "news_time":post['news_time'],\
                                        "news_id":post['news_id']}
                            db.newstag.insert_one(post_tag)
            # break    

def mutispider():
    url_list = ['http://forum.memect.com/page/'+str(i) for i in range(1,607)]
    # print url_list
    pool = ThreadPool(5)
    pool.map(memectSpider().mainSpider, url_list)

if __name__ == '__main__':
    # m = memectSpider()
    # url = 'http://forum.memect.com/page/'
    # for i in range(1,607):
    #     # print i
    #     url_ = url + str(i)
    #     print url_
    #     m.mainSpider(url_)
    # # m.mainSpider(url)
    # mutispider()
    print 'test'
    url = ['http://forum.memect.com/page/1',
           'http://forum.memect.com/page/2',
           'http://forum.memect.com/page/3']
    for i in range(len(url)):
        memectSpider().mainSpider(url[i])
        print i