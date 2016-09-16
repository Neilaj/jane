import os
import sys

import yaml
import speech_recognition as sr 
from brain import brain
from GreyMatter.SenseCells.tts import tts
from GreyMatter import play_music


profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

#Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
music_path = profile_data['music_path']


tts('Hello ' + name +  ' , How may I help you?.  ')



def main():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('I am listening')
		audio = r.listen(source)

	try:
		speech_text = r.recognize_google(audio).lower().replace("'", "")
		print("Jane thinks you said '" + speech_text + "'")
	except sr.UnknownValueError:
		print("Jane could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google speech Recognition service; {0}".format(e))


	play_music.mp3gen(music_path)
	#tts(speech_text)
	brain(name, speech_text, music_path)
	
main()

# r = sr.Recognizer()
# with sr.Microphone() as source:
# 	print("say something")
# 	audio = r.listen(source)

# with open("recording.wav", "wb") as f:
# 	f.write(audio.get_wav_data())

# try:
# 	print("Google thinks you said :" + r.recognize_google(audio))
# except sr.UnknownValueError:
# 	print("Google could not understand audio." )
# except sr.RequestError as e:
# 	print("Could nor request results from GSR;{0}".format(e))

#TTS Engine
