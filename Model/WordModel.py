from Model.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Word(Base) :
	__tablename__ = 'word'
	no = Column(Integer, primary_key = True)
	owner = Column(Integer, ForeignKey('image.no'))
	content = Column(String(256))
	postdate = Column(DateTime)

	image = relationship('Image', backref=backref('words'))
	def __init__(self, no, owner, content) :
		self.no = no
		self.owner = owner
		self.content = content
		self.postdate = datetime.today()
	def __repr__(self) :
		return "<Word('%s', '%s', '%s', '%s')>" % (self.no, self.owner, self.content \
			, self.postdate)