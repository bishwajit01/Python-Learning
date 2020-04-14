'''
Created on Feb 9, 2020

@author: Bishwajit.
'''

import speech_recognition as sr
import webbrowser as wb

sr.Microphone(device_index=1)
r = sr.Recognizer()
r.energy_threshold = 5000
with sr.Microphone() as source:
    print("SAY SOMETHING::")
    audio = r.listen(source)
    try :
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        url_chrome = "https://www.google.com/search?q="
        search_url = url_chrome + text
        wb.open(search_url)
    except :
        print("SAY AGAIN LOUDLY AND CLEARLY!!!")
