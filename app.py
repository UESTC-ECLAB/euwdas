# -*- coding: utf-8 -*-
from flask import Flask, g, request
import random
from flask import Flask, send_from_directory, session, url_for, jsonify, abort, render_template
import os
import sys
import random
import datetime
import pymongo
from pymongo import MongoClient
import time

from form.user import *

from core.preprocess import preprocess
reload(sys)
sys.setdefaultencoding('utf-8')
client = MongoClient()
client = MongoClient('localhost', 27017)

def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('global_settings.py')
    # mongo.init_app(_app)
    # configure_logging(_app)
    configure_jinja2(_app)
    _app.register_blueprint(preprocess)



    @_app.route('/', methods=['GET'])
    def homepage():
        return render_template('index.html')

    @_app.route('/login', methods=['GET'])
    def login():
        return render_template('login.html')

    @_app.route('/register', methods=['GET','POST'])
    def register():
        form = RegisterForm(request.form)
        if request.method == 'POST':
            print form.username.data, form.email.data,form.password.data
            if not form.validate():
                return render_template('register.html', form=form, error=form.errors)
            # user = User(form.username.data, form.email.data,
            #             form.password.data)
            # db_session.add(user)
            
            flash('Thanks for registering')
            return redirect(url_for('login'))
        print 'jjjjjjjjjjjjjjjjj',form
        return render_template('register.html', form=form)


    @_app.route('/develop')
    def develppage():
        return render_template('develop.html') 

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