# -*- coding: utf-8 -*-

import os
import uuid
import hashlib
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUserMixin,
                            confirm_login, fresh_login_required)

import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.eclab

class User(UserMixin):
    def __init__(self, email=None, password=None, username=None, userid=None):
        self.email = email
        self.password = password
        self.username = username
        self.isAdmin = False
        self.user_id = None

    def save(self):
        email = self.email
        password = self.password
        username = self.username

        secure_password = hashlib.sha1(password).hexdigest()
        userid = str(int(db.user.find().count())-1)

        user_info = {
            "email": email,
            "password": secure_password,
            "username": username,
            "createdAt": time.strftime('%Y-%m-%d %H:%M:%S'),
            "userid": userid
        }
        print "new user id = %s " % userid
        db.user.insert_one(user_info)
        return userid

    def get_by_email(self, email):
        one_user = db.user.find_one({"email":email})
        if str(one_user) == 'None':
            return False
        else:
            self.email = one_user['email']
            self.username = one_user['username']
            self.userid = one_user['userid']
            return self

    def get_by_username(self, username):
        one_user = db.user.find_one({"username":username})
        if str(one_user) == 'None':
            return False
        else:
            self.email = one_user['email']
            self.username = one_user['username']
            self.userid = one_user['userid']
            return self

    def get_by_userid(self, userid):
        one_user = db.user.find_one({"userid":userid})
        if str(one_user) == 'None':
            return False
        else:
            self.email = one_user['email']
            self.username = one_user['username']
            self.userid = one_user['userid']
            return self

    def get_by_w_email(self, email):
        one_user = db.user.find_one({"email":email})
        if str(one_user) == 'None':
            return False
        else:
            return True

    def get_by_w_username(self, username):
        one_user = db.user.find_one({"username":username})
        if str(one_user) == 'None':
            return False
        else:
            return True

class Anonymous(AnonymousUserMixin):
    name = u"Anonymous"
