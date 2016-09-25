
import random, os, subprocess


# def generateCaption(folderpath) :
# 	out = subprocess.check_output('/run.sh', shell=True)
# 	lines = out.split('\n')
# 	res = {}
# 	cpline = []
# 	for idx, line in enumerate(out.split('\n')) :
# 		if line[0:2] == 'cp' :
# 			cpline.append(idx)
# 	for cpidx in cpline :
# 		res[lines[cpidx].split('/')[-1]] = lines[cpidx+1].split(':')[-1]
# 	return res

mock_caption_list = ['A boy is kicking a soccer ball',\
						'A swimmer is ready for diving',\
						'A basketball is in the air',\
						'Cars are parked on parking place',\
						'The class is a little cracked']
def generateCaption(folderpath) :
	return mock_caption_list[random.randint(0,4)];