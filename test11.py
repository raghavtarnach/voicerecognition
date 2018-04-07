import webbrowser
import string
import speech_recognition as sr
from gtts import gTTS
import os

def test():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		wtext = "Hello Sir, My name is Sheela. how may i help you :"
		language = 'en'
		myobj = gTTS(text=wtext, lang=language, slow=False)
		myobj.save("w.mp3")
		os.system("mpg321 w.mp3")
		os.system('clear')
		print("Give Input : ")
		audio = r.listen(source)
	try:
		if 'Wiki' in r.recognize_google(audio):
			r2 = sr.Recognizer()
			url = 'https://en.wikipedia.org/wiki/'
			with sr.Microphone() as source :
				ptext = "Sir can you tell me what would you like to search on wikipedia ?"
				language = 'en'
				myobj = gTTS(text=ptext, lang=language, slow=False)
				myobj.save("pname.mp3")
				os.system("mpg321 pname.mp3")
				audio2 = r2.listen(source)

				try:
					print('i think you said '+r2.recognize_google(audio2))
					webbrowser.open_new(url+r2.recognize_google(audio2))
				except sr.RequestError as e:
					print('Error ; {0}'.format(e))
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		test()
test()