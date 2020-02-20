#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
import os
import pyttsx3
from gtts import gTTS
import subprocess
import webbrowser
import datetime
import time
import pyautogui
import vlc
import dictionary


def speak(audio_string):
    speak_on(audio_string)


def speak_off(audio_string):
    print(audio_string)
    engine = pyttsx3.init()
    pl_voice_id = 'polish'
    engine.setProperty('voice', pl_voice_id)
    engine.say(audio_string)
    engine.runAndWait()


def speak_on(audio_string):
    print(audio_string)
    tts = gTTS(text=audio_string, lang='pl')
    tts.save("audio.mp3")
    sound("audio.mp3")


def sound(sound):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(1)
    duration = player.get_length() / 1000
    time.sleep(duration)


def record_audio():
    for i in range(0, 3):
        print("Nasłuchiwanie...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            phrase = r.recognize_google(audio, language="pl-PL")
            print("Wypowiedź: " + phrase.lower())
            return phrase.lower()
        except sr.UnknownValueError:
            print("Nie udało się rozpoznać wypowiedzi")
            if i < 1:
                print(i)
                i += 1
                pass
            else:
                return "błąd rozpoznawania"
        except sr.RequestError as e:
            print("Nieudane żądanie do rozpoznawania mowy Google; {0}".format(e))
            return "błąd rozpoznawania"
        except:
            return "błąd rozpoznawania"


def dictation():
    while True:
        output = (record_audio() + " ")
        if output == "przecinek ":
            output.replace("przecinek", ",")
            pyautogui.typewrite(output)
            continue
        elif output == "kropka ":
            output.replace("kropka", ".")
            pyautogui.typewrite(output)
            continue
        elif output == "enter ":
            output.replace("enter ", "\n")
            pyautogui.typewrite(output)
            continue
        elif "bez odbioru" in output:
            speak("okej")
            return
        else:
            for i in output:
                if i == 'ą':
                    pyautogui.hotkey('altright', 'a')
                elif i == "ć":
                    pyautogui.hotkey('altright', 'c')
                elif i == "ę":
                    pyautogui.hotkey('altright', 'e')
                elif i == "ł":
                    pyautogui.hotkey('altright', 'l')
                elif i == "ń":
                    pyautogui.hotkey('altright', 'n')
                elif i == "ó":
                    pyautogui.hotkey('altright', 'o')
                elif i == "ś":
                    pyautogui.hotkey('altright', 's')
                elif i == "ź":
                    pyautogui.hotkey('altright', 'x')
                elif i == "ż":
                    pyautogui.hotkey('altright', 'z')
                else:
                    print(i)
                    pyautogui.press(i)


def run_program(progname):
    try:
        subprocess.Popen(progname)
    except FileNotFoundError:
        speak("Nie znaleziono programu.")
        pass


def kill_program(progname):
    try:
        print(progname)
        os.system("killall " + progname)
    except FileNotFoundError:
        speak("Nie znaleziono programu.")
        pass


def programOn(utterance):
    elements = utterance.split(' ', 1)
    if any(word in dictionary.lexicon for word in elements):
        return True
    return False


def programOff(utterance):
    elements = utterance.split(' ', 1)
    if any(word in dictionary.stops for word in elements) and any(word in dictionary.lexicon for word in elements):
        return True
    return False


def weatherInCity(utterance):
    elements = utterance.split(' ')
    if any(word in dictionary.cities for word in elements) and any(word in dictionary.weather for word in elements):
        return True
    return False


def weather(utterance):
    elements = utterance.split(' ')
    if any(word in dictionary.weather for word in elements):
        if not any(word in dictionary.cities for word in elements):
            return True
    return False


def command_prompt(parameter):
    while True:
        if parameter == 'voice':
            command = record_audio()
        elif parameter == 'text':
            command = input()
        else:
            command = record_audio()
        if all(word not in command for word in dictionary.stops):
            if command in dictionary.lexicon:
                word = dictionary.lexicon[command]
                word.launch()
            elif programOn(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.lexicon:
                        word = dictionary.lexicon[word]
                        word.launch()
            elif "gdzie jest" in command:
                command = command.split(" ", 2)
                location = command[2]
                speak("Pokazuję " + location)
                webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
            elif any(word in command for word in dictionary.search):
                command = command.split(" ", 1)
                keyword = command[1]
                speak("Wyszukuję " + keyword)
                webbrowser.open_new_tab("https://duckduckgo.com/?q=" + keyword)
            elif weatherInCity(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.cities:
                        projectClasses.WeatherForecast.launchCity(word)
            elif weather(command):
                projectClasses.WeatherForecast.launch()
            if "to wszystko" in command:
                speak("Dziękuję. Bez odbioru.")
                return
            if "błąd rozpoznawania" in command:
                speak("Błąd. Bez odbioru.")
                return
        else:
            if programOff(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.lexicon:
                        word = dictionary.lexicon[word]
                        word.kill()


def reformat_time():
    current_time = datetime.datetime.now().strftime("%T %a, %d %b %Y")
    if "Mon" in current_time:
        new_time = current_time.replace("Mon", "poniedziałek")
    elif "Tue" in current_time:
        new_time = current_time.replace("Tue", "wtorek")
    elif "Wed" in current_time:
        new_time = current_time.replace("Wed", "środa")
    elif "Thu" in current_time:
        new_time = current_time.replace("Thu", "czwartek")
    elif "Fri" in current_time:
        new_time = current_time.replace("Fri", "piątek")
    elif "Sat" in current_time:
        new_time = current_time.replace("Sat", "sobota")
    elif "Sun" in current_time:
        new_time = current_time.replace("Sun", "niedziela")
    else:
        new_time = current_time
    if "Jan" in new_time:
        new_time = new_time.replace("Jan", "styczeń")
    elif "Feb" in new_time:
        new_time = new_time.replace("Feb", "luty")
    elif "Mar" in new_time:
        new_time = new_time.replace("Mar", "marzec")
    elif "Apr" in new_time:
        new_time = new_time.replace("Apr", "kwiecień")
    elif "May" in new_time:
        new_time = new_time.replace("May", "maj")
    elif "Jun" in new_time:
        new_time = new_time.replace("Jun", "czerwiec")
    elif "Jul" in new_time:
        new_time = new_time.replace("Jul", "lipiec")
    elif "Aug" in new_time:
        new_time = new_time.replace("Aug", "sierpień")
    elif "Sep" in new_time:
        new_time = new_time.replace("Sep", "wrzesień")
    elif "Oct" in new_time:
        new_time = new_time.replace("Oct", "październik")
    elif "Nov" in new_time:
        new_time = new_time.replace("Nov", "listopad")
    elif "Dec" in new_time:
        new_time = new_time.replace("Dec", "grudzień")
    return new_time


import projectClasses
