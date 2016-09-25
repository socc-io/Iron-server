from Model.database import db_session
from Model.WordModel import Word
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

def findByContentLike(content) :
	return db_session.query(Word).filter(Word.content.like('%'+content+'%')).all()

def generateNo() :
	no = random.randint(1,100000)
	while findOneByNo(no) != None :
		no = random.randint(1,100000)
	return no

def insert(owner, content, commit=True) :
	no = generateNo()
	word = Word(no, owner, content)
	db_session.add(word)
	if commit : 
		db_session.commit()
	return no