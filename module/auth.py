# -*- coding: utf-8 -*-
import datetime
from flask import current_app, Blueprint, render_template, abort, request, flash, redirect, url_for
from jinja2 import TemplateNotFound
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)
import os
import sys
from form.user import *
from handler.user import User
# from libs.User import User
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
reload(sys)
sys.setdefaultencoding('utf-8')

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        print form.username.data, form.email.data, form.password.data
        print form.validate(),form.errors,type(form.errors)
        if not form.validate():
            return render_template('register.html', form=form, error=form.errors)
        new_user = User()
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        
        # flash('Thanks for registering')

        return redirect(url_for('login'))
    print 'jjjjjjjjjjjjjjjjj',form
    return render_template('register.html', form=form)





@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect('/login')