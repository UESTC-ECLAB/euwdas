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
    template_variables = {}
    if request.method == 'POST':
        # print form.username.data, form.email.data, form.password.data
        # print form.validate(),form.errors,type(form.errors)
        if not form.validate():
            form_error = []
            for k,v in form.errors.items():
                form_error.append(v[0])
            template_variables['form_error'] = form_error
            return render_template('register.html', form = form, template_variables = template_variables)
        if User().get_by_w_email(form.email.data):
            template_variables['form_error'] = [u'邮箱已被注册']
            return render_template('register.html', form = form, template_variables = template_variables)
        if User().get_by_w_username(form.username.data):
            template_variables['form_error'] = [u'用户名已被注册']
            return render_template('register.html', form = form, template_variables = template_variables)
        new_user = User(form.email.data, form.password.data, form.username.data)
        userid = new_user.save()
        # flash(u'恭喜您,注册成功！我们已经往您邮箱发送了验证邮件！现在您可以登录体验了！')
        flash(u'恭喜您,注册成功！现在您可以登录体验了！')
        return redirect('/login')
    return render_template('register.html', form=form, template_variables = template_variables)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    template_variables = {}
    if request.method == 'POST':
        # print form.email.data, form.password.data
        if not form.validate():
            form_error = []
            for k,v in form.errors.items():
                form_error.append(v[0])
            template_variables['form_error'] = form_error
            return render_template('login.html', template_variables = template_variables)

        if not User().get_by_w_email(form.email.data):
            template_variables['form_error'] = [u'您的邮箱还未注册！']
            return render_template('login.html', template_variables = template_variables)

        one_user = User().get_by_email_password(form.email.data, form.password.data)

        if not one_user:
        	template_variables['form_error'] = [u'对不起，您的邮箱和密码不匹配！']
        	return render_template('login.html', template_variables = template_variables)
        print 'hh'
        
        login_user(one_user)
        return redirect('/login')
    return render_template('login.html', template_variables = template_variables)



@auth.route("/logout")
# @login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect('/login')