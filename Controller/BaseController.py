from Model.database import db_session
from flask import Blueprint, request, session, request, abort, render_template
from Service.MiscService import generateCsrf
from secret import *

import Service.SearchService as searchService

baseCont = Blueprint('baseCont', __name__, template_folder='../templates')

####################################################
# Home Page
####################################################
@baseCont.route('/', methods=['GET'])
def Home() :
	return render_template('index.html')

@baseCont.route('/search', methods=['GET'])
def SearchPage() :
	txt = request.args.get('txt', 0)
	if txt == 0 :
		txt = ''
	search_result = searchService.search(txt)
	imgs = search_result['images']
	vids = search_result['videos']
	noresult = (len(imgs) == 0) and (len(vids) == 0)
	return render_template('searchPage.html', txt=txt, imgs=imgs, vids=vids, noresult=noresult)

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
