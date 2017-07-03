#import library for speech recognition
import speech_recognition as sr

# This test code is based on the following code on github:
# https://github.com/Uberi/speech_recognition -> Examples -> microphone_recognition.py
# 15 may 2017
class SpeechRecognition(object):

		def isPassButter(self):
				while (True):
						r = sr.Recognizer()
						with sr.Microphone() as source:
								print("What is my purpose?")
								audio = r.listen(source)
						try:
								gString = r.recognize_google(audio)
								if (gString == "pass the butter" or gString == "pasta butter"):
										print("PASS THE BUTTER!!")
										return True
								except sr.UnknownValueError:
										print("I could not understand what you were saying...")
										return False
								except sr.RequestError as e:        #if something goes wrong...
										print("The following error had occured from the Google Recognition Service: {0}".format(e))
										return False
