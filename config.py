BOT_TOKEN = ""

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

guild_to_audiocontroller = {}

PATH_TO_COOKIES = "cookies.txt"

MAX_HISTORY_LENGTH = -1     #Set to -1 to disable limit


#Messages that will be send by bot to text channel:
FAILED_TO_JOIN_VC_MESSAGE = "Failed to join a voice channel"
ADDED_TO_QUEUE_MESSAGE = "Added {} to queue"
ADDED_PLAYLIST_TO_QUEUE_MESSAGE = "Adding {} to queue"
SONG_NOT_FOUND_MESSAGE = "Failed to find requested song"
SKIP_MESSAGE = "Skipped"
PREVIOUS_SONG_MESSAGE = "Rewinded"
ENABLE_LOOP_MESSAGE = "Looped"
DISABLE_LOOP_MESSAGE = "Unlooped"
SHUFFLE_MESSAGE = "Shuffled"
DISCONNECTION_MESSAGE = "Disconnected"
CHANNEL_CHANGED_MESSAGE = "Changed channel"
CLIENT_AND_USER_IN_THE_SAME_CHANNEL_MESSAGE = "Bot already is on requested channel"
CLEAR_QUEUE_MESSAGE = "Cleared queue"
CLEAR_HISTORY_MESSAGE = "Cleared history"
QUEUE_IS_EMPTY_MESSAGE  = "Queue is empty"
HISTORY_IS_EMPTY_MESSAGE = "History is empty"


#Names of commands that will be visible in bot's slash command menu:
PLAY_COMMAND_NAME = "play"
SKIP_COMMAND_NAME = "skip"
PREVIOUS_SONG_COMMAND_NAME = "rewind"
LOOP_COMMAND_NAME = "loop"
SHUFFLE_COMMAND_NAME = "shuffle"
DISCONNECT_COMMAND_NAME = "disconnect"
CHANGE_CHANNEL_COMMAND_NAME = "change_channel"
CLEAR_QUEUE_COMMAND_NAME = "clear_queue"
CLEAR_HISTORY_COMMAND_NAME = "clear_history"
DISPLAY_QUEUE_COMMAND_NAME = "queue"
DISPLAY_HISTORY_COMMAND_NAME = "history"


#Descriptions of commands that will be visible in bot's slash command menu:
PLAY_COMMAND_DESCRIPTION = "Plays music"
MEDIA_ARGUMENT_DESCRIPTION = "Search phrase for site (YouTube by default) or link"
SITE_ARGUMENT_DESCRIPTION = "Site where to look for a song"
SKIP_COMMAND_DESCRIPTION = "Immediately skips to next track"
PREVIOUS_SONG_COMMAND_DESCRIPTION = "Plays previous track"
LOOP_COMMAND_DESCRIPTION = "Loops/Unloops"
SHUFFLE_COMMAND_DESCRIPTION = "Shuffles queue"
DISCONNECT_COMMAND_DESCRIPTION = "Disconnects bot from a voice channel"
CHANGE_CHANNEL_COMMAND_DESCRIPTION = "Moves to requested channel"
CLEAR_QUEUE_COMMAND_DESCRIPTION = "Clears queue"
CLEAR_HISTORY_COMMAND_DESCRIPTION = "Clears history"
DISPLAY_QUEUE_COMMAND_DESCRIPTION = "Displays queue"
DISPLAY_HISTORY_COMMAND_DESCRIPTION = "Displays history"


#Strings used in embed that bot sends when new song starts playing:
NOW_PLAYING_EMBED_STRING = "Now playing"
DURATION_EMBED_STRING = "Duration"
QUEUE_LENGTH_EMBED_STRING = "Queue"
AUTHOR_EMBED_STRING = "Author"
UPLOADER_EMBED_STRING = "Uploaded"
IS_LIVE_EMBED_VALUE = "Live"


#Strings used in embed that displays queue
QUEUE_EMBED_STRING = "Queue"


#Strings used in embed that displays history
HISTORY_EMBED_STRING = "History"