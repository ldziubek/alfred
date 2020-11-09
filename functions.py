#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pyautogui

from audioFunctions import record_audio, speak


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
        new_time = new_time.replace("Jan", "stycznia")
    elif "Feb" in new_time:
        new_time = new_time.replace("Feb", "lutego")
    elif "Mar" in new_time:
        new_time = new_time.replace("Mar", "marca")
    elif "Apr" in new_time:
        new_time = new_time.replace("Apr", "kwietnia")
    elif "May" in new_time:
        new_time = new_time.replace("May", "maja")
    elif "Jun" in new_time:
        new_time = new_time.replace("Jun", "czerwca")
    elif "Jul" in new_time:
        new_time = new_time.replace("Jul", "lipca")
    elif "Aug" in new_time:
        new_time = new_time.replace("Aug", "sierpnia")
    elif "Sep" in new_time:
        new_time = new_time.replace("Sep", "września")
    elif "Oct" in new_time:
        new_time = new_time.replace("Oct", "października")
    elif "Nov" in new_time:
        new_time = new_time.replace("Nov", "listopada")
    elif "Dec" in new_time:
        new_time = new_time.replace("Dec", "grudnia")
    return new_time
