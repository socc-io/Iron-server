from Model.database import Base
from Model.ImageModel import imageWordAssociationTable
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Word(Base) :
	__tablename__ = 'word'
	no = Column(Integer, primary_key = True)
	content = Column(String(256))
	postdate = Column(DateTime)

	images = relationship('Image', secondary=imageWordAssociationTable, back_populates='words')
	def __init__(self, no, content) :
		self.no = no
		self.content = content
		self.postdate = datetime.today()
	def __repr__(self) :
		return "<Word('%s', '%s', '%s')>" % (self.no, self.content \
			, self.postdate)