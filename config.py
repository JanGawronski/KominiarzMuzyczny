BOT_TOKEN = ""

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

guild_to_audiocontroller = {}

PATH_TO_COOKIES = "cookies.txt"

MAX_HISTORY_LENGTH = -1     #Set to -1 to disable limit


#Messages that will be send by bot to text channel:
FAILED_TO_JOIN_VC_MESSAGE = "Nie udało połączyć się z kanałem głosowym"
ADDED_TO_QUEUE_MESSAGE = "Dodano {} do kolejki"
ADDED_PLAYLIST_TO_QUEUE_MESSAGE = "Dodawanie grajlisty {} do kolejki rozpoczęte"
SONG_NOT_FOUND_MESSAGE = "Nie znaleziono utworu"
SKIP_MESSAGE = "Pominięto"
PREVIOUS_SONG_MESSAGE = "Cofnięto"
ENABLE_LOOP_MESSAGE = "Zapętlono obecny utwór"
DISABLE_LOOP_MESSAGE = "Wyłączono pętlę"
SHUFFLE_MESSAGE = "Przetasowano"
DISCONNECTION_MESSAGE = "Rozłączono"
CHANNEL_CHANGED_MESSAGE = "Zmieniono kanał"
CLIENT_AND_USER_IN_THE_SAME_CHANNEL_MESSAGE = "Bot już jest w wymaganym kanale"
CLEAR_QUEUE_MESSAGE = "Wyczyszczono kolejkę"
CLEAR_HISTORY_MESSAGE = "Wyczyszczono historię odtwarzania"
QUEUE_IS_EMPTY_MESSAGE  = "Kolejka jest pusta"
HISTORY_IS_EMPTY_MESSAGE = "Historia odtwarzania jest pusta"


#Names of commands that will be visible in bot's slash command menu:
PLAY_COMMAND_NAME = "graj"
SKIP_COMMAND_NAME = "pomiń"
PREVIOUS_SONG_COMMAND_NAME = "cofnij"
LOOP_COMMAND_NAME = "zapętl"
SHUFFLE_COMMAND_NAME = "przetasuj"
DISCONNECT_COMMAND_NAME = "rozłącz"
CHANGE_CHANNEL_COMMAND_NAME = "zmień_kanał"
CLEAR_QUEUE_COMMAND_NAME = "wyczyść_kolejkę"
CLEAR_HISTORY_COMMAND_NAME = "wyczyść_historię"
DISPLAY_QUEUE_COMMAND_NAME = "kolejka"
DISPLAY_HISTORY_COMMAND_NAME = "historia_odtwarzania"


#Descriptions of commands that will be visible in bot's slash command menu:
PLAY_COMMAND_DESCRIPTION = "Odtwarza muzykę"
MEDIA_ARGUMENT_DESCRIPTION = "Zapytanie do strony (domyślnie jutuba) lub link"
SITE_ARGUMENT_DESCRIPTION = "Strona na której ma wyszukać utworu"
SKIP_COMMAND_DESCRIPTION = "Niezwłocznie przechodzi do następnego utworu"
PREVIOUS_SONG_COMMAND_DESCRIPTION = "Odtwarza poprzedni utwór"
LOOP_COMMAND_DESCRIPTION = "Zapętla/Odpętla"
SHUFFLE_COMMAND_DESCRIPTION = "Przetasowuje kolejkę"
DISCONNECT_COMMAND_DESCRIPTION = "Rozłącza bota z kanałem głosowym"
CHANGE_CHANNEL_COMMAND_DESCRIPTION = "Przechodzi do kanału żądającego"
CLEAR_QUEUE_COMMAND_DESCRIPTION = "Czyści kolejkę"
CLEAR_HISTORY_COMMAND_DESCRIPTION = "Czyści historię odtwarzania"
DISPLAY_QUEUE_COMMAND_DESCRIPTION = "Wyświetla kolejkę odtwarzania"
DISPLAY_HISTORY_COMMAND_DESCRIPTION = "Wyświetla historię odtwarzania"


#Strings used in embed that bot sends when new song starts playing:
NOW_PLAYING_EMBED_STRING = "Teraz odtwarzane"
DURATION_EMBED_STRING = "Czas trwania"
QUEUE_LENGTH_EMBED_STRING = "Kolejka"
AUTHOR_EMBED_STRING = "Autor"
UPLOADER_EMBED_STRING = "Udostępnił"
IS_LIVE_EMBED_VALUE = "Na żywo"


#Strings used in embed that displays queue
QUEUE_EMBED_STRING = "Kolejka odtwarzania"


#Strings used in embed that displays history
HISTORY_EMBED_STRING = "Historia odtwarzania"