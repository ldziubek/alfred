#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functions import command_prompt
from functions import speak
import speech_recognition as sr
import time

mode = 'voice'


speak("Rozpoznawanie")
time.sleep(1.5)
r = sr.Recognizer()
while True:
    try:
        print("Nasłuchuję słowa kluczowego...")
        if mode == "voice":
            with sr.Microphone() as source:
                audio = r.listen(source)
            phrase = r.recognize_sphinx(audio)
        else:
            phrase = input()
        print("Sphinx rozpoznał wypowiedź: \n" + phrase)
        if "hello" in phrase:
            speak("W czym mogę pomóc?")
            command_prompt(mode)
        elif "check" in phrase:
            speak("Działam.")
        elif "finish" in phrase:
            speak("Do usłyszenia!")
            time.sleep(1)
            break
    except sr.UnknownValueError:
        print("Sphinx nie rozpoznał wypowiedzi.")
        pass
    except sr.RequestError as e:
        print("Sphinx - błąd; {0}".format(e))
        speak("Błąd żądania.")
        break
    except:
        print("Inny błąd.")
        speak("Wystąpił błąd.")
        break
