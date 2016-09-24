import os, glob
import CaptionService as cs

def generateCsrf() :
	res = ''
	for idx in range(CSRF_LENGTH) :
		res += chr(random.randint(ord('a'), ord('z')))
	return res;

def extractExtension(filename) :
	words = filename.split('.')
	if len(words) < 2 :
		return -1;
	else :
		return words[-1];

def root_dir() :
	return os.path.abspath(os.path.dirname(__file__))

def get_file(filename) :
	try :
		print 'read : ' + str(filename)
		fp = open(filename)
		dat = fp.read()
		fp.close()
		return dat
	except IOError as exc :
		return str(exc)

def scanFolder(path) :
	return glob.glob(path+'/*')