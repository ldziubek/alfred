from functions import dictation
from functions import speak
import sys


operatingSystem = sys.platform


speak("Możesz zaczynać.")
dictation(operatingSystem)
