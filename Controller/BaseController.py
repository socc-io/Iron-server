from Model.database import db_session
from flask import Blueprint, request, session, request, abort
from Service.MiscService import generateCsrf
from secret import *

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
	pass