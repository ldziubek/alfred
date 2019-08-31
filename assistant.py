#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functions import command_prompt
from functions import speak
import speech_recognition as sr
import sys
import time

mode = 'voice'
operatingSystem = sys.platform
print(operatingSystem)


speak("Rozpoznawanie")
time.sleep(1.5)
r = sr.Recognizer()
try:
    while True:
        print("Listening for keyword...")
        with sr.Microphone() as source:
            audio = r.listen(source)
        phrase = r.recognize_sphinx(audio)
        print("Sphinx thinks you said: \n" + phrase)
        if "hello" in phrase:
            speak("W czym mogę pomóc?")
            command_prompt(operatingSystem, mode)
        elif "finish" in phrase:
            speak("Do usłyszenia!")
            time.sleep(1)
            break
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
    speak("Nieznane wejście.")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    speak("Błąd żądania.")
except:
    print("Another error.")
    speak("Wystąpił błąd.")
