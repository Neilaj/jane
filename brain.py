from GreyMatter import general_conversations, play_music

def brain(name, speech_text, music_path):
	def check_message(check):
		words_of_message = speech_text.split()
		if  set(check).issubset(set(words_of_message)):
		#if speech_text == check:
			return True
		else:
			return False

	if check_message (['who', 'are', 'you']) or check_message (['what', 'is', 'your', 'name']):
		general_conversations.who_are_you()

	elif check_message(['who', 'created',  'you' ]) or check_message(['built', 'you']):
		general_conversations.who_created_you()

	elif check_message(['what', 'can', 'you', 'do']) or check_message(['do', 'you', 'what']):
		general_conversations.what_can_you_do()

	elif check_message(['play', 'music']):
		play_music.play_random(music_path)

	else:
		general_conversations.undefined()