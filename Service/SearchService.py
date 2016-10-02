from Model.database import db_session
from Model.ImageModel import Image
from Model.VideoModel import Video
from Model.WordModel import Word
from secret import *

import Service.ImageService as ImageService
import Service.VideoService as videoService
import Service.WordService as wordService
import SentenceSpliter as ss
import random, subprocess, os, sys


def search(sentence) :
	from_words = ss.splitCaption(sentence)
	images = []
	image_no = {}
	videos = []
	video_no = {}
	for word in from_words :
		db_words = wordService.findByContentLike(word)
		for db_word in db_words :
			img = db_word.image
			if image_no.get(img.no, -1) == -1 :
				image_no[img.no] = 1;
				images.append(img)
				vidno = img.owner
				if vidno != None and video_no.get(vidno, -1) == -1 :
					vid = img.video
					video_no[vidno] = 1
					videos.append(vid)
					del images[-1]
	return {'images' : images, 'videos' : videos}

