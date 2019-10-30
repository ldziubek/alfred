import webbrowser
import os
import pyautogui
import notetaker
import functions
import subprocess
import shlex


class Program:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def run(self):
        functions.speak("Włączam " + self.name)
        functions.run_program(self.path)

    def kill(self):
        functions.speak("Wyłączam " + self.name)
        functions.kill_program(self.path)


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
        mailspring = Program("Mailspring", shlex.split(programname))
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
        notemaker = Program("aplikację do notatek", "synology-note-station")
        notemaker.run()

    def kill():
        notemaker = Program("aplikację do notatek", "synology-note-station")
        notemaker.kill()


class Spotify:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Włączam spotifaj")
        subprocess.Popen(shlex.split("flatpak run com.spotify.Client"))


class IDE:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Włączam środowisko programistyczne")
        subprocess.Popen(shlex.split("flatpak run io.atom.Atom"))


class Memsource:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram MemSource.")
        webbrowser.open_new_tab("https://cloud.memsource.com/web/project/list")


class Quill:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram platformę Quill.")
        webbrowser.open_new_tab("https://app.quill-cloud.com/")


class Ling:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram słownik.")
        webbrowser.open_new_tab("http://www.ling.pl/")


class GoogleMT:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram tłumacza Google.")
        webbrowser.open_new_tab("https://translate.google.pl/")


class DeepL:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram DeepL.")
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
        functions.speak("Otwieram stronę banku.")
        webbrowser.open_new_tab("https://www.pekao24.pl/")


class Netflix:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram Netfliksa.")
        webbrowser.open_new_tab("http://www.netflix.com/browse")


class HboGo:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram HBO GO.")
        webbrowser.open_new_tab("https://hbogo.pl/")


class Amazon:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram Amazon Prajm")
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
        functions.speak("Wyłączam komputer.")
        os.system("shutdown -h now")


class RebootComputer:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Uruchamiam ponownie komputer.")
        os.system("shutdown -r now")


class LockScreen:
    def __init__(self, name):
        self.name = name

    def launch():
        os.system("dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock")


class PlayPause:
    def __init__(self, name):
        self.name = name

    def launch():
        pyautogui.press('space')


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


class Franz:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Włączam komunikator")
        subprocess.Popen(shlex.split("flatpak run com.meetfranz.Franz"))


class Webcomics:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Otwieram Twoje ulubione komiksy.")
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
        functions.speak("Otwieram prognozę pogody.")
        webbrowser.open_new_tab("https://duckduckgo.com/?q=weather+krak%C3%B3w&t=ffab&ia=weather")

    def launchCity(arg):
        functions.speak("Otwieram prognozę pogody.")
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
        functions.speak("Włączam lajbry")
        subprocess.Popen(shlex.split("flatpak run io.lbry.lbry-app"))


class WhatsTheTime:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak(functions.reformat_time())


class DictiationTool:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Możesz zaczynać")
        functions.dictation()


class AccountingSetup:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Do usług.")
        functions.run_program("soffice")
        functions.run_program("mailspring")
        functions.run_program("gnome-calculator")


class CodingSetup:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Do usług.")
        functions.run_program("gnome-terminal")
        functions.run_program("synology-note-station")
        functions.run_program("firefox")
        subprocess.Popen(shlex.split("flatpak run io.atom.Atom"))


class TranslationSetup:
    def __init__(self, name):
        self.name = name

    def launch():
        functions.speak("Do usług.")
        functions.run_program("google-chrome")
        functions.run_program("synology-note-station")
        functions.run_program("mailspring")
        functions.run_program("firefox")
        subprocess.Popen(shlex.split("flatpak run com.meetfranz.Franz"))
