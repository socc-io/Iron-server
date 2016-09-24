from Controller.BaseController import *
from Controller.ImageController import *
from Controller.VideoController import *

def registerController(app) :
	app.register_blueprint(baseCont)
	app.register_blueprint(imageCont)
	app.register_blueprint(videoCont)