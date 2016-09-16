import random
from SenseCells.tts import tts

def who_are_you():
	messages = ['I am Jane. Your Voice Integrated Personal Assistant.', 'My name is Jane. I told you before.']
	tts(random.choice(messages))

def who_created_you():
	tts('Neil Ajodah is my creator. I was designed to help the elderlee.')
	
def what_can_you_do():
	tts('I can do all sorts of things, like, Search Wikipedia. Play music. Check email. Browse the internet. And more. Please see my instruction manual for full details.',)
	

def undefined():
	message = ' I do not know that yet. Sorry!'
	tts(message)
