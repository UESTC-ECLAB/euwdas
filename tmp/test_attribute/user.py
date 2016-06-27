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
    def __init__(self, email=None, password=None, username=None, \
                        userid=None, avatar=None, active=None, \
                        is_admin=False):
        self.email = email
        self.password = password
        self.username = username
        self.is_admin = False
        self.is_active = active
        self.userid = None
        self.avatar = None
