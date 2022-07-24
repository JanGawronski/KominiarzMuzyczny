BOT_TOKEN: str = "ODg4NDcxMTc4NDA5MzA0MDk0.GYqb0E.3SIA104ofsKAkcHTZ9CQVYVl5s_iOzL5zPaN-s"
SPOTIFY_ID: str = "01f52e9b8c284885a43f19fd32a6b142"
SPOTIFY_SECRET: str = "cfe0e1c3655541699275f687f51f26b7"
NGROK_API: str = "2COHf2yAf14EgTWQd8nEnspOi0q_7QxgrMa97tq9fB8cfN9rZ"

BOT_PREFIX = "-"

EMBED_COLOR = 0x4dd4d0  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 25  #maximum of 25

COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = True

VC_TIMEOUT = 600 #seconds
VC_TIMOUT_DEFAULT = True  #default template setting for VC timeout true= yes, timeout false= no timeout
ALLOW_VC_TIMEOUT_EDIT = True  #allow or disallow editing the vc_timeout guild setting


STARTUP_MESSAGE = "Starting Bot..."
STARTUP_COMPLETE_MESSAGE = "Startup Complete"

NO_GUILD_MESSAGE = 'Dołącz na kanał głosowy lub pisz na czacie serwerowym'
USER_NOT_IN_VC_MESSAGE = "Dołącz na kanał głosowy"
WRONG_CHANNEL_MESSAGE = "Nieprawidłowy kanał głosowy"
NOT_CONNECTED_MESSAGE = "Bot nie jest na kanale głosowym"
ALREADY_CONNECTED_MESSAGE = "Bot już jest na kanale głosowym"
CHANNEL_NOT_FOUND_MESSAGE = "Nie można znaleźć kanału"
DEFAULT_CHANNEL_JOIN_FAILED = "Nie można dołączyć do domyślnego kanału"
INVALID_INVITE_MESSAGE = "Nieprawidłowe zaproszenie"

ADD_MESSAGE= "Żeby dodać bota kliknij [tutaj]" #brackets will be the link text

INFO_HISTORY_TITLE = "Zagrane utwory:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Chłop co to wrzucił: "
SONGINFO_DURATION = "Długość (jak pały): "
SONGINFO_SECONDS = "s"
SONGINFO_LIKES = "Polubienia: "
SONGINFO_DISLIKES = "Niepodobania: "
SONGINFO_NOW_PLAYING = "Teraz leci"
SONGINFO_QUEUE_ADDED = "Dodano do kolejki wariacie"
SONGINFO_SONGINFO = "Info o utworze"
SONGINFO_ERROR = "Niewspierana strona albo utwór +18"
SONGINFO_PLAYLIST_QUEUED = "Grajlista zakolejkowana"
SONGINFO_UNKNOWN_DURATION = "Pieron wie"

HELP_ADDBOT_SHORT = "Dodaje bota na inny serwer"
HELP_ADDBOT_LONG = "Daje link służący do dodanie bota na inny serwer"
HELP_CONNECT_SHORT = "Dołącza bota do kanału"
HELP_CONNECT_LONG = "Dołącza bota do kanału na którym jesteś"
HELP_DISCONNECT_SHORT = "Rozłącza bota z kanału głosowego"
HELP_DISCONNECT_LONG = "Rozłącza bota z kanału głosowego i zatrzymuje audio"

HELP_SETTINGS_SHORT = "Pokazuje i pozwala na zmianę ustawień"
HELP_SETTINGS_LONG = "Pokazuje i pozwala na zmianę ustawień bota na serwerze. Użycie {}settings nazwa_ustawienia wartość".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Pokazuje historie utworów"
HELP_HISTORY_LONG = "Pokazuje " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " ostatnich utworów"
HELP_PAUSE_SHORT = "Zatrzymuje odtwarzanie muzyki"
HELP_PAUSE_LONG = "Zatrzymuje odtwarzanie muzyki. Może być ono wznowione użyciem komendy wznawiającej \"-wznów\""
HELP_VOL_SHORT = "Zmienia procent głośności"
HELP_VOL_LONG = "Zmienia głośność odtwarzanie muzyki. Podana liczba (w zakresie od 1 do 100) określa procent głośności muzyki"
HELP_PREV_SHORT = "Wraca do poprzedniego utworu"
HELP_PREV_LONG = "Odtwarza ponownie poprzedni utwór"
HELP_RESUME_SHORT = "Wznawia odtwarzanie"
HELP_RESUME_LONG = "Wznawia odtwarzanie utworu wcześniej wstrzymanego komendą wstrzymującą \"-pauza\""
HELP_SKIP_SHORT = "Pomija utwór"
HELP_SKIP_LONG = "Pomija obecnie odtwarzany utwór i przechodzi do kolejnego"
HELP_SONGINFO_SHORT = "Info o obecnie granym utworze"
HELP_SONGINFO_LONG = "Pokazuje szczegółowe informacje o utworze i pokazuje do niego link"
HELP_STOP_SHORT = "Zatrzymuje muzykę"
HELP_STOP_LONG = "Zatrzymuje odtwarzanie utworu i czyści kolejkę"
HELP_MOVE_LONG = f"{BOT_PREFIX}przesuń [pozycja] [nowa pozycja]"
HELP_MOVE_SHORT = "Przesuwa utwór w kolejce"
HELP_YT_SHORT = "Gra wspierany plik na TwojejTubie"
HELP_YT_LONG = ("-g [link/tytuł utworu/słowa kluczowe/link do grajlisty/link do soundclouda/link do spotify/link do bandcampa/link do twittera]")
HELP_PING_SHORT = "Pong"
HELP_PING_LONG = "Sprawdza czy bot odpowiada"
HELP_CLEAR_SHORT = "Czyści kolejkę"
HELP_CLEAR_LONG = "Czyści kolejkę i pomija obecnie grający utwór"
HELP_LOOP_SHORT = "Zapętla obecnie grany utwór. Zmień włącz/wyłącz"
HELP_LOOP_LONG = "Zapętla obecnie grany utwór i zatrzymuje kolejkę. Użyj ponownie, aby wyłączyć pętlę"
HELP_QUEUE_SHORT = "Pokazuje utwory w kolejce"
HELP_QUEUE_LONG = "Pokazuje do 10 utworów w kolejce"
HELP_SHUFFLE_SHORT = "Przetasowuje kolejkę"
HELP_SHUFFLE_LONG = "Losowo sortuje utwory piosenkę"
HELP_CHANGECHANNEL_SHORT = "Zmiena kanał bota"
HELP_CHANGECHANNEL_LONG = "Zmienia kanał bota na kanał głosowy na którym ty jesteś"

HELP_SERVERMINECRAFT_SHORT = "Uruchamia minecraft serwer"
HELP_SERVERMINECRAFT_LONG = "Uruchamia jeden z dostępnych serwerów w minecraft"
HELP_SHOWSERVERLISTMINECRAFT_SHORT = "Pokazuje listę serwerów"
HELP_SHOWSERVERLISTMINECRAFT_LONG = "Pokazuje listę dostępnych serwerów w minecraft"
HELP_SHOWSERVERIPMINECRAFT_SHORT = "Pokazuje IP serwera minecraft"
HELP_SHOWSERVERIPMINECRAFT_LONG = "Pokazuje IP obecnie działającego serwera w minecraft"
HELP_TURNOFFMINECRAFTSERVER_SHORT = "Wyłącza serwer w minecraft"
HELP_TURNOFFMINECRAFTSERVER_LONG = "Wyłącza obecnie działający serwer w minecraft"
HELP_CONVERSATION_SHORT = "Uruchamia konwersację"
HELP_CONVERSATION_LONG = "Uruchamia konwersację z botem"

SERVERS = ['SkyFactoryOne', 'Serwer1.19', 'ATM7', 'medev']

ABSOLUTE_PATH = '' #do not modify