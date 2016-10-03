from Model.database import db_session
from Model.WordModel import Word
import SentenceSpliter as ss
import random

def deleteByNo(no) :
	obj = findOneByNo(no)
	if obj == None :
		return 'already not exists'
	db_session.delete(obj)
	db_session.commit()
	return "deleted"

def findAll() :
	return db_session.query(Word).all()

def findOneByNo(no) :
	return db_session.query(Word).filter(Word.no == no).first()

def findOneByContent(content) :
	return db_session.query(Word).filter(Word.content == content).first()

def findByContentLike(content) :
	return db_session.query(Word).filter(Word.content.like('%'+content+'%')).all()

def generateNo() :
	no = random.randint(1,100000)
	while findOneByNo(no) != None :
		no = random.randint(1,100000)
	return no

def insert(content, commit=True) :
	no = generateNo()
	word = Word(no, content)
	db_session.add(word)
	if commit : 
		db_session.commit()
	return word

def insertByCaption(caption, image) :
	words = ss.splitCaption(caption)
	word_list = []
	for word in words :
		no = generateNo()
		word = Word(no, word)
		word.images.append(image)
		word_list.append(word)
		db_session.add(word)
	db_session.commit()
	return word_list