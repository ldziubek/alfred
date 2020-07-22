import os
import subprocess

import dictionary
from audioFunctions import speak


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
    if any(word in dictionary.quits for word in elements) and any(word in dictionary.lexicon for word in elements):
        return True
    return False


def play(utterance):
    elements = utterance.split(' ', 1)
    if any(word in dictionary.plays for word in elements) and any(word in dictionary.lexicon for word in elements):
        return True
    return False


def pause(utterance):
    elements = utterance.split(' ', 1)
    if any(word in dictionary.pauses for word in elements) and any(word in dictionary.lexicon for word in elements):
        return True
    return False


def nextSong(utterance):
    elements = utterance.split(' ', 1)
    if any(word in dictionary.nexts for word in elements) and any(word in dictionary.lexicon for word in elements):
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
