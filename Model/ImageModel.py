from Model.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime

imageWordAssociationTable = Table('image_word_association', Base.metadata,\
	Column('imgno', Integer, ForeignKey('image.no')),\
	Column('wordno', Integer, ForeignKey('word.no'))\
)

class Image(Base) :
	__tablename__ = 'image'
	no = Column(Integer, primary_key = True)
	owner = Column(Integer, ForeignKey('video.no'))
	title = Column(String(100))
	caption = Column(String(256))
	localpath = Column(String(256))
	postdate = Column(DateTime)

	video = relationship('Video', backref=backref('images'))
	words = relationship('Word', secondary=imageWordAssociationTable, back_populates='images')
	def __init__(self, no, owner, title, caption, localpath) :
		self.no = no
		self.owner = owner
		self.title = title
		self.caption = caption
		self.localpath = localpath
		self.postdate = datetime.today()
	def __repr__(self) :
		return "<Image('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.no, self.owner, self.title \
			, self.caption, self.localpath, self.postdate)
	def __str__(self) :
		return "no : %s, owner : %s, title : %s, caption : %s, localpath : %s, postdate : %s" \
		%(str(self.no), str(self.owner), self.title, self.caption, self.localpath, self.postdate)
