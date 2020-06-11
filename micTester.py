import speech_recognition as sr

r = sr.Recognizer()
while True:
    print("Nasłuchuję słowa kluczowego...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    phrase = r.recognize_sphinx(audio)
    print("Sphinx rozpoznał wypowiedź: \n" + phrase)
    # phrase2 = r.recognize_google(audio, language="pl-PL")
    # print("Google rozpoznał wypowiedź: \n" + phrase2)
