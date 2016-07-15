# -*- coding: utf-8 -*-
import os
import sys
from flask import current_app, Blueprint, render_template, abort, request, flash, redirect, url_for
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
reload(sys)
sys.setdefaultencoding('utf-8')


news = Blueprint('news', __name__, template_folder='templates')

@news.route('/news', methods=['GET','POST'])
def news():
    print 'test'