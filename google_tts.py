from gttS import gTTS
import os
text = " I am Rakshith"
language = 'en'
speech= gTTS(text= text, lang= language, slow= False)
os.system("start test.mp3")
speech.save("test.mp3")
os.system("start test.mp3")
