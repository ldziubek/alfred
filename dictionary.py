import projectClasses


quits = ("quit", "close", "exit", "zamknij")
search = ("search", "find", "wyszukaj", "znajdź")
cities = ("kraków", "krakowie", "oświęcim", "oświęcimiu", "warszawa", "warszawie", "jasień", "jasieniu")
weather = ("pogoda", "pogody", "pogodę", "prognoza", "prognozę")
plays = ("play", "graj", "odtwarzaj")
pauses = ("stop", "zatrzymaj", "wstrzymaj")
nexts = ("next", "dalej", "następny", "następne")


lexicon = {
    'terminal':projectClasses.TerminalConsole,
    'console':projectClasses.TerminalConsole,
    'browser':projectClasses.LaunchBrowser,
    'internet':projectClasses.LaunchBrowser,
    'przeglądarka':projectClasses.LaunchBrowser,
    'przeglądarkę':projectClasses.LaunchBrowser,
    'chrome':projectClasses.GoogleChrome,
    'google chrome':projectClasses.GoogleChrome,
    'krom':projectClasses.GoogleChrome,
    'firefox':projectClasses.MozillaFirefox,
    'firefoks':projectClasses.MozillaFirefox,
    'email':projectClasses.EmailClient,
    'outlook':projectClasses.EmailClient,
    'thunderbird':projectClasses.EmailClient,
    'evolution':projectClasses.EmailClient,
    'mailspring':projectClasses.EmailClient,
    'poczta':projectClasses.EmailClient,
    'pocztę':projectClasses.EmailClient,
    'poczty':projectClasses.EmailClient,
    'editor':projectClasses.TextEditor,
    'text':projectClasses.TextEditor,
    'exid':projectClasses.TextEditor,
    'gedit':projectClasses.TextEditor,
    'notepad':projectClasses.TextEditor,
    'kate':projectClasses.TextEditor,
    'notatnik':projectClasses.TextEditor,
    'file manager':projectClasses.FileManager,
    'nemo':projectClasses.FileManager,
    'nautilus':projectClasses.FileManager,
    'home':projectClasses.FileManager,
    'dokumenty':projectClasses.FileManager,
    'pliki':projectClasses.FileManager,
    'calculator':projectClasses.GnomeCalculator,
    'kalkulator':projectClasses.GnomeCalculator,
    'simple note':projectClasses.NoteApp,
    'simplenote':projectClasses.NoteApp,
    'evernote':projectClasses.NoteApp,
    'one note':projectClasses.NoteApp,
    'aplikacja do notatek':projectClasses.NoteApp,
    'aplikację do notatek':projectClasses.NoteApp,
    'spotify':projectClasses.Spotify,
    'music':projectClasses.Spotify,
    'muzykę':projectClasses.Spotify,
    'muzyka':projectClasses.Spotify,
    'intellij':projectClasses.IDE,
    'ideę':projectClasses.IDE,
    'idea':projectClasses.IDE,
    'intelidżej':projectClasses.IDE,
    'inteligo':projectClasses.IDE,
    'intelligent':projectClasses.IDE,
    'atom':projectClasses.IDE,
    'memsource':projectClasses.Memsource,
    'membersource':projectClasses.Memsource,
    'mapsource':projectClasses.Memsource,
    'mem source':projectClasses.Memsource,
    'quill':projectClasses.Quill,
    'platformę':projectClasses.Quill,
    'ling':projectClasses.Ling,
    'dictionary':projectClasses.Ling,
    'słownik':projectClasses.Ling,
    'google translate':projectClasses.GoogleMT,
    'translator':projectClasses.GoogleMT,
    'deepl':projectClasses.DeepL,
    'empty':projectClasses.DeepL,
    'deep l':projectClasses.DeepL,
    'dip l':projectClasses.DeepL,
    'dip el':projectClasses.DeepL,
    'wordfast':projectClasses.Wordfast,
    'cat stool':projectClasses.Wordfast,
    'cat tool':projectClasses.Wordfast,
    'word fast':projectClasses.Wordfast,
    'world fast':projectClasses.Wordfast,
    'bank':projectClasses.BankPage,
    'banku':projectClasses.BankPage,
    'nowy świat':projectClasses.NowySwiat,
    'radiospacja':projectClasses.Radiospacja,
    'radio spacja':projectClasses.Radiospacja,
    'podkasty':projectClasses.Podcasts,
    'podcasty':projectClasses.Podcasts,
    'radio':projectClasses.Radio,
    'netflix':projectClasses.Netflix,
    'movies':projectClasses.Netflix,
    'movie player':projectClasses.Netflix,
    'serial':projectClasses.Netflix,
    'film':projectClasses.Netflix,
    'hbo':projectClasses.HboGo,
    'ha be o':projectClasses.HboGo,
    'habeo':projectClasses.HboGo,
    'amazon':projectClasses.Amazon,
    'prime':projectClasses.Amazon,
    'event':projectClasses.NewEvent,
    'meeting':projectClasses.NewEvent,
    'spotkanie':projectClasses.NewEvent,
    'kalendarz':projectClasses.NewEvent,
    'wydarzenie':projectClasses.NewEvent,
    'shut down':projectClasses.ShutdownComputer,
    'wyłącz komputer':projectClasses.ShutdownComputer,
    'reboot':projectClasses.RebootComputer,
    'restart':projectClasses.RebootComputer,
    'uruchom ponownie komputer':projectClasses.RebootComputer,
    'resetuj komputer':projectClasses.RebootComputer,
    'lock':projectClasses.LockScreen,
    'zablokuj':projectClasses.LockScreen,
    'zablokuj ekran':projectClasses.LockScreen,
    'add note':projectClasses.AddNote,
    'add a note':projectClasses.AddNote,
    'dodaj notatkę':projectClasses.AddNote,
    'remove note':projectClasses.RemoveNote,
    'remove a note':projectClasses.RemoveNote,
    'usuń notatkę':projectClasses.RemoveNote,
    'list notes':projectClasses.ListNotes,
    'note list':projectClasses.ListNotes,
    'lista notatek':projectClasses.ListNotes,
    'playNotes':projectClasses.PlayNote,
    'play note':projectClasses.PlayNote,
    'play a note':projectClasses.PlayNote,
    'odtwórz notatkę':projectClasses.PlayNote,
    'otwórz notatkę':projectClasses.PlayNote,
    'webcomics':projectClasses.Webcomics,
    'cartoons':projectClasses.Webcomics,
    'komiks':projectClasses.Webcomics,
    'komiksy':projectClasses.Webcomics,
    'library':projectClasses.Lbry,
    'lajbry':projectClasses.Lbry,
    'wideoteka':projectClasses.Lbry,
    'wideotekę':projectClasses.Lbry,
    'która godzina':projectClasses.WhatsTheTime,
    'what is the time':projectClasses.WhatsTheTime,
    'dictation':projectClasses.DictiationTool,
    'dyktowanie':projectClasses.DictiationTool,
    'będę wystawiać faktury':projectClasses.AccountingSetup,
    'będę programować':projectClasses.CodingSetup,
    'będę tłumaczyć':projectClasses.TranslationSetup,
    'wiadomość':projectClasses.SendEmail,
    }
