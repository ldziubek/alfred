Basic Polish language voice assistant for GNOME. You can use it to launch
software, kill it, check the time, shutdown/reboot your computer, lock the
screen, search in DuckDuckGo, search for objects in Google Maps.

Currently available commands:
Basic operations:
* "Hello" to activate command recognition
* "To wszystko" ends command recognition
* when command recognition is off, "finish" exits program
In command recognition mode:
* "gdzie jest [place name]" opens the place in Google Maps
* "która godzina" reads current time and date
* "pogoda", "prognoza", "pokaż prognozę pogody" show weather forecast. By default,
  it shows weather in Krakow. It can also show weather in Warszawa and Oświęcim
  if the city name is specified.
* "wyszukaj [phrase]", "znajdź [phrase]" runs search for a specified phrase in
  DuckDuckGo
* Certain keywords launch specific programs. You can also used them in accusative
  case.
  * "terminal" opens gnome terminal
  * "internet", "przeglądarka" launch default browser
  * "chrome", "google chrome" launch Google Chrome
  * "firefox" launches Mozilla Firefox
  * "e-mail", "poczta" launch default mail client
  * "gedit", "notatnik" launch gedit
  * "dokumenty", "pliki" launch Gnome File Manager
  * "kalkulator" launches Gnome Calculator
  * "aplikacja do notatek" launches Synology NoteStation
  * "spotify", "muzyka" launch Spotify
  * "atom" launches Atom
  * "wordfast" launches Wordfast
  * "library", "wideoteka" launches Lbry.tv client
* There are also keywords for certain webpages:
  * "quill" opens Quill Cloud platform
  * "ling", "słownik" open Ling.pl dictionary
  * "google translate", "translator" open Google Translate
  * "deepl" opens DeepL machine translation platform
  * "bank" opens banking site
  * "netflix", "serial", "film" open Netflix
  * "ha be o" opens HBO Go
  * "amazon", "prime" open Amazon Prime Video
  * "spotkanie", "kalendarz", "wydarzenie" open Gnome Calendar
* Some basic system commands:
  * "wyłącz komputer" shuts down the system
  * "restart", "resetuj", "uruchom ponownie komputer" reboot the system
  * "zablokuj", "zablokuj ekran" lock the screen
  * "odtwórz", "pauza", "wstrzymaj", "zatrzymaj" press spacebar
* Native voice note module:
  * "dodaj notatkę" records a short voice note (single utterance). You can then
    decide to save, remove or replay it
  * "usuń notatkę" asks for the name of note to remove
  * "lista notatek" reads the list of notes you've created
  * "odtwórz notatkę", "otwórz notatkę" asks for the name of note to play
* "dyktowanie" launches the dictation module (experimental)
  * "przecinek" enters comma
  * "kropka" enters full stop
  * "enter" enters a linebreak
  * "bez odbioru" quits dictation module
* "wiadomość" asks for subject, body and recipient (from a predefined list) and
  creates a message in default e-mail Client
* finally, there are some commands to quickly launch predefined sets of apps and
  pages:
  * "będę wystawiać faktury" opens a set of tools for invoicing translation work:
    OpenOffice, Gnome Calculator and Geary
  * "będę tłumaczyć" opens a set of tools used for translation:
    Google Chrome, Firefox, Geary and Synology NoteStation
  * "będę programować" opens a set of tools for coding:
    Gnome Terminal, Atom, Firefox and Synology NoteStation
