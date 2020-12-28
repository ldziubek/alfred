import webbrowser

import projectClasses
import dictionary
from audioFunctions import speak, record_audio
from programFunctions import programOn, weatherInCity, weather, programOff, play, pause, nextSong


def command_prompt(parameter):
    while True:
        if parameter == 'voice':
            command = record_audio()
        elif parameter == 'text':
            command = input()
        else:
            command = record_audio()
        if all(word not in command for word in (dictionary.quits + dictionary.plays + dictionary.pauses + dictionary.nexts)):
            if command in dictionary.lexicon:
                word = dictionary.lexicon[command]
                word.launch()
            elif programOn(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.lexicon:
                        word = dictionary.lexicon[word]
                        word.launch()
            elif "gdzie" in command:
                command = command.split(" ", 2)
                location = command[2]
                speak("Pokazuję " + location)
                webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + "/&amp;")
            elif "co umiesz" in command:
                speak("Pokazuję listę funkcji")
                webbrowser.open_new_tab("https://github.com/ldziubek/alfred/blob/master/README.md")
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
            elif play(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.lexicon:
                        word = dictionary.lexicon[word]
                        word.play()
            elif pause(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.lexicon:
                        word = dictionary.lexicon[word]
                        word.pause()
            elif nextSong(command):
                elements = command.split(" ")
                for word in elements:
                    if word in dictionary.lexicon:
                        word = dictionary.lexicon[word]
                        word.next()
