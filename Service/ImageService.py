from Model.database import db_session
from Model.ImageModel import Image
from secret import *

import Service.CaptionService as cs
import Service.WordService as wordService
import random, subprocess
import SentenceSpliter as ss

def deleteByNo(no) :
	obj = findOneByNo(no)
	if obj == None :
		return 'already not exists'
	deleteImageFile(str(obj.no) + '.jpg')
	db_session.delete(obj)
	db_session.commit()
	return "deleted"

def findAll() :
	return db_session.query(Image).all()

def findOneByNo(no) :
	return db_session.query(Image).filter(Image.no == no).first()

def findLocalpathByNo(no) :
	return db_session.query(Image.localpath).filter(Image.no == no).first()

def generateNo() :
	no = random.randint(1,100000)
	while findOneByNo(no) != None :
		no = random.randint(1,100000)
	return no

def deleteImageFile(filename) :
	subprocess.check_output('rm ' + IMAGE_FOLDER_AFTER + filename);

def insertImage(filename, imgno, owner, title, caption) :
	image = Image(imgno, owner, title, caption, IMAGE_FOLDER_AFTER+str(imgno)+'.jpg')
	db_session.add(image)
	db_session.commit()	
	return image

def signImage(filename, owner=None) :
	imgno = generateNo()
	caption = cs.generateCaption(IMAGE_FOLDER_BEFORE)
	print 'got caption : ' + caption
	command = 'mv %s%s %s%s' % (IMAGE_FOLDER_BEFORE, filename, \
		IMAGE_FOLDER_AFTER, str(imgno)+'.jpg') # Move file to afterFolder
	subprocess.check_output(command, shell=True)
	image = insertImage(filename, imgno, owner, filename, caption)
	for cap in ss.splitCaption(caption) :
		word = wordService.findOneByContent(cap)
		if word == None :
			word = wordService.insert(cap, commit=False)
		word.images.append(image)
	db_session.commit()
	return imgno