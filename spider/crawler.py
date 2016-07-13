__author__ = 'Administrator'
#coding:utf-8

from bs4 import BeautifulSoup
import requests

def get_url(url):

    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    content = soup.findAll('div', {'class':"f-floatright"})

    titles = []
    url_of_titles = {}

    for item in content[1:]:
        wanted = item.find('h2', {'class': 'title'})
        title = wanted.get_text()
        title = str(title).strip()
        titles.append(title)
        the_url = wanted.find('a').get('href')
        url_of_titles[title] = the_url
    return titles, url_of_titles

def get_needed_content(url):

    html = requests.get(url)
    soup = BeautifulSoup(html.text)

    #作者
    for_author = soup.find('span', {'style':"font-size:14px"})
    author = for_author.b.get_text()

    #封面图片
    for_head = soup.find('a', {'class':"profile_image_wrapper"})
    head = for_head.img.get('src')

    #标签
    for_tags = soup.findAll('a', {'class':'fe_tag'})
    tags = []
    for item in for_tags:
        tag = item.get_text()
        tags.append(tag)
    tags = tags[1:]

    #时间
    for_time = soup.find('span', {'class':"datetime"})
    time = for_time.get_text()

    #内容和来源网址
    for_source_content = soup.find('div', {'class':"text"})
    url_source = for_source_content.find('a').get('href')
    content = for_source_content.get_text()
    content = content.strip()

    #图片
    for_picture = soup.find('div', {'class': 'original_pic'})
    try:
        picture = for_picture.find('img').get('src')
    except AttributeError as e:
        picture = 'Null'
    else:
        pass

    return author, head, tags, time, url_source, content, picture


url = 'http://forum.memect.com/page/'
fn = open('crawled_data.txt', 'w', encoding = 'utf-8')
fn.write('title\tauthor\thead\ttags_string\ttime\turl_source\tcontent\tpicture\n')
for i in range(1, 603):
    titles, url_of_titles = get_url(url + str(i) + '/')
    for title in titles:
        print(title)
        target_url = url_of_titles[title]
        author, head, tags, time, url_source, content, picture = get_needed_content(target_url)
        tags_string = ''
        for tag in tags:
            tags_string += (tag + ' ')
        fn.write(title + '\t' + author + '\t' + head + '\t' + tags_string + '\t' + time + '\t' + url_source + '\t' + content + '\t' + picture + '\n')
    break
fn.close()
