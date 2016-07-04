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

from core.rounte.rounte import BeijingRounte

travelrec = Blueprint('travelrec', __name__, template_folder='templates')

@travelrec.route('/travelrectest', methods=['GET','POST'])
def travelrectest():
    travelList = [u"鸟巢",u"奥林匹克公园",u"北海公园",u"长安街",u"王府井大街",
                    u"颐和园",u"清华大学",u"南锣鼓巷",u"国子监",u"八达岭"]
    b = BeijingRounte()
    return b.route(travelList)