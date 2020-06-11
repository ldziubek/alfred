import speech_recognition as sr
import os
import datetime
from audioFunctions import speak, record_audio


def note_recorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    with open("note.wav", "wb") as f:
        f.write(audio.get_wav_data())


def note_add():
    speak("Słucham!")
    note_recorder()
    speak("Czy zapisać?")
    command = record_audio()
    if "tak" in command:
        speak("Podaj nazwę")
        name = record_audio()
        listfile = "notelist.txt"
        with open(listfile, 'a') as f:
            f.write(name + "\n")
        os.rename("note.wav", "{}-{}.wav".format(datetime.date.today(), name))
        speak("Zapisano notatkę: {}".format(name))
    elif "odtwórz" in command:
        os.system("aplay note.wav")
        speak("Czy zapisać?")
        command = record_audio()
        if "tak" in command:
            speak("Podaj nazwę")
            name = record_audio()
            listfile = "notelist.txt"
            with open(listfile, 'a') as f:
                f.write(name + "\n")
            os.rename("note.wav", "{}-{}.wav".format(datetime.date.today(), name))
            speak("Zapisano notatkę: {}".format(name))
        elif "nie" in command:
            os.remove("note.wav")
            speak("Notatka nie została zapisana")
    elif "nie" in command:
        os.remove("note.wav")
        speak("Notatka nie została zapisana")
    else:
        return


def note_list():
    speak("Lista notatek:")
    with open("notelist.txt") as file:
        lines = [line.strip() for line in file]
    for i in lines:
        speak(i)
    speak("Czy chcesz otworzyć którąś notatkę?")
    command = record_audio()
    if "tak" in command:
        note_playback()
    elif command in lines:
        os.system("aplay {}-{}.wav".format(datetime.date.today(), command))
    elif "nie" in command:
        speak("Rozumiem")
    else:
        return


def note_playback():
    speak("Którą notatkę mam odtworzyć?")
    with open("notelist.txt") as file:
        lines = [line.strip() for line in file]
    command = record_audio()
    if command in lines:
        os.system("aplay {}-{}.wav".format(datetime.date.today(), command))
    else:
        speak("Nie znaleziono notatki.")


def note_remove():
    with open("notelist.txt") as file:
        lines = [line.strip() for line in file]
    speak("Którą notatkę mam usunąć?")
    command = record_audio()
    if command in lines:
        f = open("notelist.txt", "r")
        filecontent = f.read()
        f.close()
        newcontent = filecontent.replace("{}\n".format(command), "")
        f = open("notelist.txt", "w")
        f.write(newcontent)
        f.close()
        os.remove("{}-{}.wav".format(datetime.date.today(), command))
    else:
        speak("Nie znaleziono notatki.")
