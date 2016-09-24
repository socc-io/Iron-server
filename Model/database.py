from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from secret import *

engine = create_engine(MYSQL_DATABASE_HOST, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	# import all modules here that might define models
	import Model.VideoModel
	import Model.ImageModel
	import Model.WordModel
	Base.metadata.create_all(bind=engine)
