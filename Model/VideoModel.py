from Model.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Video(Base) :
	__tablename__ = 'video'
	no = Column(Integer, primary_key = True)
	outerpath = Column(String(256))
	postdate = Column(DateTime)

	def __init__(self, no, outerpath) :
		self.no = no
		self.outerpath = outerpath
		self.postdate = datetime.today()
	def __repr__(self) :
		return "<Video('%s', '%s', '%s')>" % (str(self.no), self.outerpath \
			, str(self.postdate))