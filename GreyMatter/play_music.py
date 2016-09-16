import os
import sys
import random

from SenseCells.tts import tts

def mp3gen(music_path):
	music_list = []
	for root, dirs, files in os.walk(music_path):
		for filename in files:
			if os.path.splitext(filename)[1] == ".mp3":
				music_list.append(os.path.join(root, filename.lower()))
	return music_list

def music_player(file_name):
	if sys.platform == 'darwin':
		player = "afplay '" + file_name + "'"
		return os.system(player)
	elif sys.platform == 'linux2' or sys.platform =='linux':
		player = "mpg123 '" + file_name + "'"
		return os.system(player)


def play_random(music_path):
	try:
		music_listing = mp3gen(music_path)
		music_playing = random.choice(music_listing)
		tts("now Playing: " + music_playing)
		music_player(music_playing)
	except IndexError as e:
		tts("No music files found")
		print ("no music files found:{0}".format(e))

		
