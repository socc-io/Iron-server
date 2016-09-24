import os, subprocess

imgRate = 1.0
imgResolution = '320x240'

#outputPath : ex) output%d.jpg

def vidToImg(vidPath, outputPath) :
	command = 'ffmpeg -i %s -an -r %f -y -s %s %s' % (vidPath, imgRate, imgResolution, outputPath);
	result = subprocess.check_output(command, shell=True)
