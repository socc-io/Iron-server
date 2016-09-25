from Model.database import db_session
from flask import Blueprint, request, session, request, abort
from Service.MiscService import generateCsrf
from secret import *

import Service.SearchService as searchService

baseCont = Blueprint('baseCont', __name__, template_folder='../templates')

####################################################
# Home Page
####################################################
@baseCont.route('/', methods=['GET'])
def Home() :
	return "Hello this is home! " + request.url

####################################################
# get CSRF Token
####################################################
@baseCont.route('/csrf', methods=['GET'])
def GetCsrf() :
	csrf = generateCsrf();
	session['csrf_token'] = csrf;
	return csrf;

####################################################
# Search API
####################################################
@baseCont.route('/search/<string:text>', methods=['GET'])
def Search(text) :
	search_result = searchService.search(text)
	result = '' # String result
	for img in search_result['images'] :
		result += str(img) + '<br>'
	for vid in search_result['videos'] :
		result += str(vid) + '<br>'
	return result