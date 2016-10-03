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
			for img in db_word.images :
				if image_no.get(img.no, -1) == -1 :
					image_no[img.no] = 1;
					if img.video == None :
						images.append(img)
					else :
						video = img.video
						if video_no.get(video.no, -1) == -1 :
							video_no[video.no] = 1
							videos.append(video)
	return {'images' : images, 'videos' : videos}

