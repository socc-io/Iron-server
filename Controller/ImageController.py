
from flask import Blueprint, request, flash, Response
from Service import ImageService as imageService
from Service import WordService as wordService
from secret import *
from werkzeug.utils import secure_filename
from Model.database import db_session

import Service.MiscService as misc
import os

imageCont = Blueprint('imageCont', __name__, template_folder='../templates')

####################################################
# Image List
####################################################
@imageCont.route('/admin/img/list', methods=['GET'])
def ImgList() :
	res = ''
	for img in imageService.findAll() :
		res += str(img) + '<br>'
	return res
####################################################
# Image GET
####################################################
@imageCont.route('/img/<int:imgno>', methods=['GET']) 
def GetImg(imgno) :
	localpath = imageService.findLocalpathByNo(imgno)
	if localpath == None :
		return "image not found"
	return Response(misc.get_file(localpath[0]), mimetype="image/jpeg")

####################################################
# Image DELETE
####################################################
@imageCont.route('/img/<int:imgno>', methods=['DELETE']) 
def DeleteImg(imgno) :
	return str(imageService.deleteByNo(imgno))

####################################################
# Image POST
####################################################
@imageCont.route('/img', methods=['POST'])
def PostImg() :
	if 'file' not in request.files :
		flash('No file part')
		return 'no file found'
	file = request.files['file']
	ext = misc.extractExtension(file.filename)
	if not(ext in IMAGE_EXTENSIONS) :
		return 'not image file'
	if file.filename == '' :
		return 'invalid image file name'
	filename = secure_filename(file.filename)
	file.save(os.path.join(IMAGE_FOLDER_BEFORE, filename))
	newno = imageService.signImage(filename)

	return "{msg:'%s',imgno:'%d'}"%("success", newno)