# -*- coding: utf-8 -*-
import time
import random
import string
from flask import Blueprint, request, redirect, current_app, url_for, send_from_directory, json, abort, render_template, abort, make_response, session


preprocess = Blueprint('preprocess', __name__, url_prefix='/preprocess')

#@api.route('/team/icon/<int:team_id>')

@preprocess.route('/cutwords/zh')
def cutWords():
	return 'error'

@preprocess.route('/compoundwords/mc')
def cw_mc():
	return 'error'