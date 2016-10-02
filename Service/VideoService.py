from Model.database import db_session
from Model.ImageModel import Image
from Model.VideoModel import Video
from secret import *

import Service.CaptionService as cs
import Service.ImageService as imageService
import Service.MiscService as misc
import random, subprocess
import SentenceSpliter as spliter
import SentenceSpliter as ss

imgRate = 1.0
imgResolution = '320x240'

def deleteByNo(no) :
	obj = findOneByNo(no)
	if obj == None :
		return 'already not exists'
	db_session.delete(obj)
	db_session.commit()
	return "deleted"

def findAll() :
	return Video.query.all()

def findOneByNo(no) :
	return Video.query.filter(Video.no == no).first()

def generateNo() :
	no = random.randint(1,100000)
	while findOneByNo(no) != None :
		no = random.randint(1,100000)
	return no

#outputPath : ex) output%d.jpg

def deleteVideofile(filename) :
	subprocess.check_output('rm ' + VIDEO_FOLDER + filename, shell=True)

def insertVideo(vidno, outerpath, thumbnail, title) :
	video = Video(vidno, title, outerpath, thumbnail) # empty is title
	db_session.add(video)
	db_session.commit()

def selectThumbnail(filename, no) :
	thumbnail = IMAGE_FOLDER_AFTER + 'vid_'+str(no)+'.jpg'
	cmd = 'cp %s %s' % (IMAGE_FOLDER_BEFORE + filename + '_1.jpg', thumbnail)
	subprocess.check_output(cmd, shell=True)
	return thumbnail

def vidToImg(vidPath, outputPath) :
	command = 'ffmpeg -i %s -an -r %f -y -s %s %s' % (vidPath, imgRate, imgResolution, outputPath);
	result = subprocess.check_output(command, shell=True)

def signVideo(filename, outerpath, title) :
	vidno = generateNo()
	vidToImg(VIDEO_FOLDER + filename, IMAGE_FOLDER_BEFORE + filename + '_%d.jpg')
	thumbnail = selectThumbnail(filename, vidno)
	insertVideo(vidno, outerpath, thumbnail, title)
	deleteVideofile(filename)
	for imgpath in misc.scanFolder(IMAGE_FOLDER_BEFORE) :
		imgname = imgpath.split('/')[-1]
		imageService.signImage(imgname, vidno)

