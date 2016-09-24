
from flask import Blueprint, request, flash, Response
from Service import ImageService as imageService
from Service import WordService as wordService
from Service import VideoService as videoService
from secret import *
from werkzeug.utils import secure_filename
from Model.database import db_session

import Service.MiscService as misc
import os

videoCont = Blueprint('videoCont', __name__, template_folder='../templates')

####################################################
# Video GET
####################################################
@videoCont.route('/vid/<int:vidno>', methods=['GET'])
def GetVid(vidno) :
	query = 'select localpath from video where no=%d' % vidno
	cur = RunQuery(query)
	vids = cur.fetchall()
	if len(vids) < 1 :
		return "video not found"
	return Response(get_file(vids[0]), mimetype="video/mp4")

####################################################
# Video DELETE
####################################################
@videoCont.route('/vid/<int:vidno>', methods=['DELETE'])
def DeleteVid(vidno) :
	pass

####################################################
# Video POST
####################################################
@videoCont.route('/vid', methods=['POST'])
def PostVid() :
	if 'file' not in request.files :
		flash('No file part')
		return 'no file found'
	outerpath = request.form.get('outerpath', 0)
	if outerpath == 0 :
		return 'no outerpath'
	file = request.files['file']
	ext = misc.extractExtension(file.filename)
	if not(ext in VIDEO_EXTENSIONS) :
		return 'not video file'
	if file.filename == '' :
		return 'invalid video file name'	
	filename = secure_filename(file.filename)
	file.save(os.path.join(VIDEO_FOLDER, filename))
	videoService.signVideo(filename, outerpath)
	return 'success'