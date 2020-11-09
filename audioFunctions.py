import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import time
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
