from Model.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Video(Base) :
	__tablename__ = 'video'
	no = Column(Integer, primary_key = True)
	title = Column(String(256))
	outerpath = Column(String(256))
	thumbnail = Column(String(256))
	postdate = Column(DateTime)

	def __init__(self, no, title, outerpath, thumbnail) :
		self.no = no
		self.outerpath = outerpath
		self.title = title
		self.postdate = datetime.today()
		self.thumbnail = thumbnail
	def __repr__(self) :
		return "<Video('%s', '%s', '%s', '%s')>" % (str(self.no), self.outerpath, self.title \
			, str(self.postdate))