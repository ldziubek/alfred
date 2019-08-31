#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
import os
import pyttsx3
from gtts import gTTS
import dictionary
import subprocess
import webbrowser
import datetime
import time
import pyautogui
import vlc


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
    tts = gTTS(text=audio_string, lang='pl')
    tts.save("audio.mp3")
    sound("audio.mp3")
    #p = vlc.MediaPlayer("audio.mp3")
    #p.play()
    #os.system("mpg321 audio.mp3")


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
        print("Listening...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            phrase = r.recognize_google(audio, language="pl-PL")
            print("You said: " + phrase.lower())
            return phrase.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            if i < 1:
                print(i)
                i += 1
                pass
            else:
                return "błąd rozpoznawania"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "błąd rozpoznawania"
        except:
            return "błąd rozpoznawania"


def dictation(opersys):
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
            if opersys == 'darwin':
                for i in output:
                    if i == 'ą':
                        pyautogui.hotkey('option', 'a')
                    elif i == "ć":
                        pyautogui.hotkey('option', 'c')
                    elif i == "ę":
                        pyautogui.hotkey('option', 'e')
                    elif i == "ł":
                        pyautogui.hotkey('option', 'l')
                    elif i == "ń":
                        pyautogui.hotkey('option', 'n')
                    elif i == "ó":
                        pyautogui.hotkey('option', 'o')
                    elif i == "ś":
                        pyautogui.hotkey('option', 's')
                    elif i == "ź":
                        pyautogui.hotkey('option', 'x')
                    elif i == "ż":
                        pyautogui.hotkey('option', 'z')
                    else:
                        pyautogui.press(i)
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


class Program:
    def __init__(self, name, linuxpath, macpath, system):
        self.name = name
        self.linuxpath = linuxpath
        self.macpath = macpath
        self.system = system

    def run(self):
        speak("Włączam " + self.name)
        if self.system == 'linux':
            run_program(self.linuxpath)
        elif self.system == 'darwin':
            run_program(self.macpath)


def command_prompt(opersys, parameter):
    while True:
        if parameter == 'voice':
            command = record_audio()
        elif parameter == 'text':
            command = input()
        else:
            command = input()
        if all(word not in command for word in dictionary.stops):
            if any(word in command for word in dictionary.browsers):
                speak("Włączam przeglądarkę.")
                webbrowser.open_new_tab("https://duckduckgo.com/")
            elif any(word in command for word in dictionary.terminals):
                terminal = Program("Terminal", "gnome-terminal",
                                   "/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal", opersys)
                terminal.run()
            elif any(word in command for word in dictionary.chromes):
                chrome = Program("Google Chrome", "google-chrome",
                                 "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", opersys)
                chrome.run()
            elif any(word in command for word in dictionary.firefox):
                firefox = Program("Firefox", "firefox", "/Applications/Firefox.app/Contents/MacOS/firefox", opersys)
                firefox.run()
            elif any(word in command for word in dictionary.emailClients):
                mailspring = Program("Mailspring", "mailspring",
                                     "/Applications/Mailspring.app/Contents/MacOS/mailspring", opersys)
                mailspring.run()
            elif any(word in command for word in dictionary.fileManagers):
                filemanager = Program("Menedżer plików", "nautilus",
                                      "/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder", opersys)
                filemanager.run()
            elif any(word in command for word in dictionary.textEditors):
                texteditor = Program("Edytor tekstu", "gedit",
                                     "/Applications/TextEdit.app/Contents/MacOS/TextEdit", opersys)
                texteditor.run()
            elif any(word in command for word in dictionary.franz):
                speak("Włączam komunikator")
                if opersys == 'linux':
                    os.system("flatpak run com.meetfranz.Franz")
                elif opersys == 'darwin':
                    run_program("/Applications/Franz.app/Contents/MacOS/Franz")
            elif any(word in command for word in dictionary.IDEs):
                speak("Włączam środowisko programistyczne")
                if opersys == 'linux':
                    os.system("flatpak run io.atom.Atom")
                elif opersys == 'darwin':
                    run_program("/Applications/IntelliJ IDEA CE.app/Contents/MacOS/idea")
            elif any(word in command for word in dictionary.calculators):
                calculator = Program("kalkulator", "gnome-calculator",
                                     "/Applications/Calculator.app/Contents/MacOS/Calculator", opersys)
                calculator.run()
            elif any(word in command for word in dictionary.noteTakers):
                notemaker = Program("aplikację do notatek", "synology-note-station",
                                     "/Applications/Simplenote.app/Contents/MacOS/Simplenote", opersys)
                notemaker.run()
            elif any(word in command for word in dictionary.spotifys):
                speak("Włączam spotifaj")
                if opersys == 'linux':
                    os.system("flatpak run com.spotify.Client")
                elif opersys == 'darwin':
                    run_program("/Applications/Spotify.app/Contents/MacOS/Spotify")
            elif any(word in command for word in dictionary.newEvents):
                speak("Otwieram kalendarz.")
                if opersys == 'linux':
                    run_program("gnome-calendar")
                elif opersys == 'darwin':
                    webbrowser.open_new_tab("https://calendar.google.com/calendar/r/eventedit?pli=1")
            elif any(word in command for word in dictionary.wordfasts):
                wordfast = Program("Wordfast", "/home/leszek/wf.lin64/wordfast", "", opersys)
                wordfast.run()
            elif any(word in command for word in dictionary.tasklists):
                wunderlist = Program("listę zadań", "wunderlistux",
                                     "/Applications/Firefox.app/Contents/MacOS/firefox", opersys)
                wunderlist.run()
            elif any(word in command for word in dictionary.memsources):
                speak("Otwieram MemSource.")
                webbrowser.open_new_tab("https://cloud.memsource.com/web/project/list")
            elif any(word in command for word in dictionary.netflixes):
                speak("Otwieram Netfliksa.")
                webbrowser.open_new_tab("http://www.netflix.com/browse")
            elif any(word in command for word in dictionary.quills):
                speak("Otwieram platformę Quill.")
                webbrowser.open_new_tab("https://app.quill-cloud.com/")
            elif any(word in command for word in dictionary.banks):
                speak("Otwieram stronę banku.")
                webbrowser.open_new_tab("https://www.pekao24.pl/")
            elif any(word in command for word in dictionary.lings):
                speak("Otwieram słownik.")
                webbrowser.open_new_tab("http://www.ling.pl/")
            elif any(word in command for word in dictionary.googlemts):
                speak("Otwieram tłumacza Google.")
                webbrowser.open_new_tab("https://translate.google.pl/")
            elif any(word in command for word in dictionary.deepls):
                speak("Otwieram DeepL.")
                webbrowser.open_new_tab("https://www.deepl.com/translator")
            elif any(word in command for word in dictionary.webcomics):
                speak("Otwieram Twoje ulubione komiksy.")
                webbrowser.open_new_tab("https://leasticoulddo.com/")
                webbrowser.open_new_tab("https://www.lfg.co/")
                webbrowser.open_new_tab("http://www.tabletitans.com/")
                webbrowser.open_new_tab("http://www.konradokonski.com/KWD/")
                webbrowser.open_new_tab("http://www.totempole666.com/")
                webbrowser.open_new_tab("http://www.smbc-comics.com/index.php/")
            elif any(word in command for word in dictionary.shutdowns):
                speak("Wyłączam komputer.")
                os.system("shutdown -h now")
            elif any(word in command for word in dictionary.reboots):
                speak("Uruchamiam ponownie komputer.")
                os.system("shutdown -r now")
            elif any(word in command for word in dictionary.lockScreens):
                speak("Blokuję ekran.")
                if opersys == 'linux':
                    os.system("dbus-send --type=method_call --dest=org.gnome.ScreenSaver \ /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock")
                elif opersys == 'darwin':
                    subprocess.call(
                        '/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend',
                        shell=True)
            elif any(word in command for word in dictionary.playPauses):
                pyautogui.press('space')
            elif "która godzina" in command:
                speak(reformat_time())
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
            elif "dyktowanie" in command:
                speak("Możesz zaczynać")
                dictation(opersys)
            elif any(word in command for word in dictionary.addNotes):
                notetaker.note_add()
            elif any(word in command for word in dictionary.removeNotes):
                notetaker.note_remove()
            elif any(word in command for word in dictionary.listNotes):
                notetaker.note_list()
            elif any(word in command for word in dictionary.addNotes):
                notetaker.note_add()
            if "to wszystko" in command:
                speak("Dziękuję. Bez odbioru.")
                return
            if "błąd rozpoznawania" in command:
                speak("Błąd. Bez odbioru.")
                return
        else:
            if any(word in command for word in dictionary.browsers):
                speak("Zamykam przeglądarkę.")
                os.system("killall firefox")
                os.system("killall chrome")
            elif any(word in command for word in dictionary.emailClients):
                speak("Zamykam klienta poczty.")
                os.system("killall mailspring")
            elif any(word in command for word in dictionary.textEditors):
                speak("Zamykam edytor tekstu.")
                os.system("killall xed")
                os.system("killall textedit")
            elif any(word in command for word in dictionary.franz):
                speak("Zamykam komunikator.")
                os.system("killall franz")
            elif any(word in command for word in dictionary.IDEs):
                speak("Zamykam ideę.")
                os.system("killall atom")
            elif any(word in command for word in dictionary.calculators):
                speak("Zamykam kalkulator.")
                os.system("killall gnome-calculator ")
                os.system("killall calculator")
            elif any(word in command for word in dictionary.noteTakers):
                speak("Zamykam aplikację do notatek.")
                os.system("killall synology-note-station")
            elif any(word in command for word in dictionary.spotifys):
                speak("Zamykam Spotifaj.")
                os.system("killall spotify")
            if any(word in command for word in dictionary.wordfasts):
                speak("Zamykam Wordfasta.")
                os.system("killall wordfast")


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


import notetaker
