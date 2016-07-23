# -*- coding: utf-8 -*-
from flask import Flask, g, request
import random
from flask import Flask, send_from_directory, session, url_for, jsonify, abort, render_template, flash, redirect
from flask.ext.login import LoginManager, current_user
from flask_apscheduler import APScheduler
import os
import sys
import random
import datetime
import pymongo
from pymongo import MongoClient
import time

from form.user import *
from handler.user import User
from timer import SchedulerConfig
from core.news.homepage import *
from module.auth import auth
from module.travelrec import travelrec

reload(sys)
sys.setdefaultencoding('utf-8')
client = MongoClient()
client = MongoClient('localhost', 27017)
login_manager = LoginManager()
scheduler = APScheduler()
db = client.eclab

def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('global_settings.py')
    _app.config.from_object(SchedulerConfig())
    # mongo.init_app(_app)
    # configure_logging(_app)
    configure_jinja2(_app)
    login_manager.setup_app(_app)
    login_manager.login_view = 'login'
    scheduler.init_app(_app)
    _app.register_blueprint(auth)
    _app.register_blueprint(travelrec)

    @_app.route('/', methods=['GET'])
    def homepage():
        return render_template('index.html', template_variables = homepage_rec())

    @_app.route('/develop')   
    def develppage():
        return render_template('develop.html') 

    @_app.route('/test')   
    def testpage():
        return render_template('test.html') 

    @_app.before_request
    def before_request():
        g.user = current_user
    return _app

def configure_jinja2(app):
    app.jinja_env.trim_blocks = True

    @app.template_filter()
    def time_delta(d, **params):
        return d + datetime.timedelta(**params)

def configure_logging(app):
    """Configure file(info) and email(error) logging."""
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler(os.path.join(app.config['LOG_PATH'], 'eclab.log'), maxBytes=100000, backupCount=10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('[%(asctime)s](%(levelname)s) %(message)s  [%(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

@login_manager.user_loader
def load_user(userid):
    if userid is None:
        redirect('/login')
    user = User()
    user.get_by_id(userid)
    if user.is_active:
        return user
    else:
        return None
