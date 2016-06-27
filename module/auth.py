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

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        print form.username.data, form.email.data, form.password.data
        print form.validate(),form.errors,type(form.errors)
        if not form.validate():
            return render_template('register.html', form = form, error = form.errors)
        if User().get_by_w_email(form.email.data):
            error = u'邮箱已被注册'
            return render_template('register.html', form = form, error = error)
        if User().get_by_w_username(form.username.data):
            error = u'用户名已被注册'
            return render_template('register.html', form = form, error = error)
        new_user = User(form.email.data, form.password.data, form.username.data)
        userid = new_user.save()
        flash('success')
        return redirect('/login')
    print 'jjjjjjjjjjjjjjjjj',form
    return render_template('register.html', form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')



@auth.route("/logout")
# @login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect('/login')