import webbrowser
import os
import pyautogui
import subprocess
import shlex

import functions
from audioFunctions import speak, record_audio
import notetaker


class Program:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def run(self):
        speak("Włączam " + self.name)
        programFunctions.run_program(self.path)

    def kill(self):
        speak("Wyłączam " + self.name)
        programFunctions.kill_program(self.path)


class TerminalConsole:
    def __init__(self, name):
        self.name = name

    def launch():
        terminalConsole = Program("Terminal", "gnome-terminal")
        terminalConsole.run()

    def kill():
        terminalConsole = Program("Terminal", "gnome-terminal")
        terminalConsole.kill()


class TextEditor:
    def __init__(self, name):
        self.name = name

    def launch():
        os.system("xdg-mime query default text/plain  > output.txt")
        file = open("output.txt", "r")
        programname = ("gtk-launch " + file.read())
        file.close()
        texteditor = Program("Edytor tekstu", shlex.split(programname))
        texteditor.run()


class LaunchBrowser:
    def __init__(self, name):
        self.name = name

    def launch():
        os.system("xdg-settings get default-web-browser > output.txt")
        file = open("output.txt", "r")
        programname = ("gtk-launch " + file.read())
        file.close()
        browser = Program("przeglądarkę", shlex.split(programname))
        browser.run()


class GoogleChrome:
    def __init__(self, name):
        self.name = name

    def launch():
        chrome = Program("Google Chrome", "google-chrome")
        chrome.run()

    def kill():
        texteditor = Program("Google Chrome", "google-chrome")
        texteditor.kill()


class MozillaFirefox:
    def __init__(self, name):
        self.name = name

    def launch():
        firefox = Program("Firefox", "firefox")
        firefox.run()

    def kill():
        texteditor = Program("Firefox", "firefox")
        texteditor.kill()


class EmailClient:
    def __init__(self, name):
        self.name = name

    def launch():
        os.system("xdg-settings get default-url-scheme-handler mailto > output.txt")
        file = open("output.txt", "r")
        programname = ("gtk-launch " + file.read())
        file.close()
        mailspring = Program("Geary", shlex.split(programname))
        mailspring.run()


class FileManager:
    def __init__(self, name):
        self.name = name

    def launch():
        filemanager = Program("menedżer plików", shlex.split("xdg-open ."))
        filemanager.run()


class GnomeCalculator:
    def __init__(self, name):
        self.name = name

    def launch():
        gnomeCalculator = Program("kalkulator", "gnome-calculator")
        gnomeCalculator.run()

    def kill():
        gnomeCalculator = Program("kalkulator", "gnome-calculator")
        gnomeCalculator.kill()


class NoteApp:
    def __init__(self, name):
        self.name = name

    def launch():
        notemaker = Program("aplikację do notatek", "joplin-desktop")
        notemaker.run()

    def kill():
        notemaker = Program("aplikację do notatek", "joplin")
        notemaker.kill()


class Spotify:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Włączam spotifaj")
        subprocess.Popen(shlex.split("flatpak run com.spotify.Client"))

    def play():
        subprocess.Popen(shlex.split("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play"))

    def pause():
        subprocess.Popen(shlex.split("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop"))

    def next():
        subprocess.Popen(shlex.split("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"))


class Radio:
    def __init__(self, name):
        self.name = name

    def launch():
        radiospacja = Program("Rhythmbox", "rhythmbox")
        radiospacja.run()

    def kill():
        radiospacja = Program("Rhythmbox", "rhythmbox")
        radiospacja.kill()

    def play():
        subprocess.Popen(shlex.split("rhythmbox-client --play"))

    def pause():
        subprocess.Popen(shlex.split("rhythmbox-client --pause"))

    def next():
        subprocess.Popen(shlex.split("rhythmbox-client --next"))


class NowySwiat:
    def __init__(self, name):
        self.name = name

    def launch():
        nowySwiat = Program("Rhythmbox", shlex.split("rhythmbox-client --play-uri='https://n02.rcs.revma.com/ypqt40u0x1zuv?fbclid=IwAR2DIX_Rw0Iez5LhjHV3w1j7-OtQdYpTzv7zJQiUhghYfEMtAe8vXSxQnCA&rj-ttl=5&rj-tok=AAABczTq2r4Ae2FGwl_zCrzS8g'"))
        nowySwiat.run()

    def kill():
        nowySwiat = Program("Rhythmbox", "rhythmbox")
        nowySwiat.kill()

    def play():
        subprocess.Popen(shlex.split("rhythmbox-client --play"))

    def pause():
        subprocess.Popen(shlex.split("rhythmbox-client --pause"))


class Radiospacja:
    def __init__(self, name):
        self.name = name

    def launch():
        radiospacja = Program("Rhythmbox", shlex.split("rhythmbox-client --play-uri='https://play.adtonos.com/radiospacjapl'"))
        radiospacja.run()

    def kill():
        radiospacja = Program("Rhythmbox", "rhythmbox")
        radiospacja.kill()

    def play():
        subprocess.Popen(shlex.split("rhythmbox-client --play"))

    def pause():
        subprocess.Popen(shlex.split("rhythmbox-client --pause"))


class Podcasts:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Włączam podkasty")
        subprocess.Popen(shlex.split("flatpak run org.gnome.Podcasts"))


class IDE:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Włączam środowisko programistyczne")
        subprocess.Popen(shlex.split("flatpak run io.atom.Atom"))


class Memsource:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram MemSource.")
        webbrowser.open_new_tab("https://cloud.memsource.com/web/project/list")


class Quill:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram platformę Quill.")
        webbrowser.open_new_tab("https://app.quill-cloud.com/")


class Ling:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram słownik.")
        webbrowser.open_new_tab("http://www.ling.pl/")


class GoogleMT:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram tłumacza Google.")
        webbrowser.open_new_tab("https://translate.google.pl/")


class DeepL:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram DeepL.")
        webbrowser.open_new_tab("https://www.deepl.com/translator")


class Wordfast:
    def __init__(self, name):
        self.name = name

    def launch():
        wordfast = Program("Wordfast", "/home/leszekdziubek/Pobrane/Wordfast_Pro_5.8.0/Wordfast_Pro-5.8.0")
        wordfast.run()


class BankPage:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram stronę banku.")
        webbrowser.open_new_tab("https://www.pekao24.pl/")


class Netflix:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram Netfliksa.")
        webbrowser.open_new_tab("http://www.netflix.com/browse")

    def play():
        print("weszło")
        pyautogui.press('space')


class HboGo:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram HBO GO.")
        webbrowser.open_new_tab("https://hbogo.pl/")


class Amazon:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram Amazon Prajm")
        webbrowser.open_new_tab("https://www.primevideo.com/")


class NewEvent:
    def __init__(self, name):
        self.name = name

    def launch():
        calendar = Program("kalendarz", "gnome-calendar")
        calendar.run()

    def kill():
        calendar = Program("kalendarz", "gnome-calendar")
        calendar.kill()


class ShutdownComputer:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Czy na pewno wyłączyć komputer?")
        command = record_audio()
        if "tak" in command:
            speak("Wyłączam komputer.")
            os.system("shutdown -h now")
        else:
            speak("W porządku, anuluję operację.")
            return


class RebootComputer:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Czy uruchomić ponownie komputer?")
        command = record_audio()
        if "tak" in command:
            speak("OK.")
            os.system("shutdown -r now")
        else:
            speak("W porządku, anuluję operację.")
            return


class LockScreen:
    def __init__(self, name):
        self.name = name

    def launch():
        os.system("xdg-screensaver lock")


class AddNote:
    def __init__(self, name):
        self.name = name

    def launch():
        notetaker.note_add()


class RemoveNote:
    def __init__(self, name):
        self.name = name

    def launch():
        notetaker.note_remove()


class ListNotes:
    def __init__(self, name):
        self.name = name

    def launch():
        notetaker.note_list()


class PlayNote:
    def __init__(self, name):
        self.name = name

    def launch():
        notetaker.note_playback()


class Webcomics:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram Twoje ulubione komiksy.")
        webbrowser.open_new_tab("https://leasticoulddo.com/")
        webbrowser.open_new_tab("https://www.lfg.co/")
        webbrowser.open_new_tab("http://www.tabletitans.com/")
        webbrowser.open_new_tab("http://www.konradokonski.com/KWD/")
        webbrowser.open_new_tab("http://www.totempole666.com/")
        webbrowser.open_new_tab("http://www.smbc-comics.com/index.php/")


class WeatherForecast:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Otwieram prognozę pogody.")
        webbrowser.open_new_tab("https://duckduckgo.com/?q=weather+krak%C3%B3w&t=ffab&ia=weather")

    def launchCity(arg):
        speak("Otwieram prognozę pogody.")
        if arg == "krakowie":
            webbrowser.open_new_tab("https://duckduckgo.com/?q=weather+krak%C3%B3w&t=ffab&ia=weather")
        elif arg == "kraków":
            webbrowser.open_new_tab("https://duckduckgo.com/?q=weather+krak%C3%B3w&t=ffab&ia=weather")
        elif arg == "warszawie":
            webbrowser.open_new_tab("https://duckduckgo.com/?q=weather+warszawa&t=ffab&ia=weather")
        elif arg == "warszawa":
            webbrowser.open_new_tab("https://duckduckgo.com/?q=weather+warszawa&t=ffab&ia=weather")
        elif arg == "oświęcimiu":
            webbrowser.open_new_tab("https://www.weatheronline.pl/Malopolskie/Oswiecim.htm")
        elif arg == "oświęcim":
            webbrowser.open_new_tab("https://www.weatheronline.pl/Malopolskie/Oswiecim.htm")
        elif arg == "jasień":
            webbrowser.open_new_tab("https://www.weatheronline.pl/Pomorskie/Bytow.htm")
        elif arg == "jasieniu":
            webbrowser.open_new_tab("https://www.weatheronline.pl/Pomorskie/Bytow.htm")


class Lbry:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Włączam lajbry")
        subprocess.Popen(shlex.split("flatpak run io.lbry.lbry-app"))


class WhatsTheTime:
    def __init__(self, name):
        self.name = name

    def launch():
        speak(functions.reformat_time())
        print("zrobione")


class DictiationTool:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Możesz zaczynać")
        functions.dictation()


class AccountingSetup:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Do usług.")
        programFunctions.run_program("soffice")
        programFunctions.run_program("geary")
        programFunctions.run_program("gnome-calculator")


class CodingSetup:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Do usług.")
        programFunctions.run_program("gnome-terminal")
        programFunctions.run_program("synology-note-station")
        programFunctions.run_program("firefox")
        subprocess.Popen(shlex.split("flatpak run io.atom.Atom"))


class TranslationSetup:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Do usług.")
        programFunctions.run_program("google-chrome")
        programFunctions.run_program("synology-note-station")
        programFunctions.run_program("geary")
        programFunctions.run_program("firefox")


class SendEmail:
    def __init__(self, name):
        self.name = name

    def launch():
        speak("Podaj temat.")
        subject = record_audio()
        print(subject)
        speak("Podaj odbiorcę")
        recipient = record_audio()
        print(recipient)
        try:
            with open("recipients.txt") as f:
                emailContacts = dict(line.strip().split(":") for line in f)
        except FileNotFoundError:
            print("Lista odbiorców niedostępna.")
            emailContacts = {}
        if recipient in emailContacts:
            recipientAddress = emailContacts[recipient]
            print(recipientAddress)
            speak("Podaj treść")
            mailBody = record_audio()
            print(mailBody)
            speak("Przygotowano wiadomość do odbiorcy: " + recipient + " o temacie: " + subject + " i treści: " + mailBody + ". Czy otworzyć w programie pocztowym?")
            decision = record_audio()
            if decision == "tak":
                polecenie = "xdg-email --subject \'{!s}\' --body \'{!s}\' \'{!s}\'".format(subject, mailBody, recipientAddress)
                subprocess.Popen(shlex.split(polecenie))
            else:
                speak("Kasuję wiadomość.")
        else:
            speak("Nie rozpoznano odbiorcy")

import programFunctions
