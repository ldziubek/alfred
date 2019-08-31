import smtplib
from functions import speak, record_audio
from urllib.request import urlopen


def sendmail():
    speak("Do kogo chcesz wysłać wiadomość?")
    recipient = record_audio()
    print(recipient)
    if "leszek" in recipient:
        speak("Co chcesz napisać?")
        content = record_audio()
        print(content)
        mail = smtplib.SMTP("serwer1784615.home.pl", 587)
        mail.ehlo()
        mail.starttls()
        mail.ehlo()
        mail.login("leszek@dziubek.biz.pl", "2vKCoc8^f^F&")
        mail.sendmail("Leszek Dziubek <leszek@dziubek.biz.pl>", "Leszek <leszek.dziubek@gmail.com>", content)
        mail.close()
        speak("Email has been sent.")


def internet_on():
    try:
        urlopen('https://www.google.com/', timeout=5)
        print("Są internety")
        return True
    except:
        print('Nie ma internetów')
        return False

sendmail()