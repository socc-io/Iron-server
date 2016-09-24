
import random
import os

mock_caption_list = ['A boy is kicking a soccer ball',\
						'A swimmer is ready for diving',\
						'A basketball is in the air',\
						'Cars are parked on parking place',\
						'The class is a little cracked']
def generateCaption(folderpath) :
	return mock_caption_list[random.randint(0,4)];