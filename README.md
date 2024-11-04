# Kominiarz Muzyczny
Bot uses only slash commands and can play from every source [yt-dlp](https://github.com/yt-dlp/yt-dlp) can.

## How to run
### Tokens
To run this bot you have to create Discord Application on [Discord Developer portal](https://discord.com/developers/applications) and enter API token in bot config. You can also get simillar token from spotify to enable bot to fetch titles from spotify (it still source songs from spotify, but get titles and search for them on Soundcloud). 
### Environment
I recommend Python 3.12, but any >=3.10 will probably do. Needed packages for Python are stated in setup files. I strongly recommend using [Python Virtual Environment](https://docs.python.org/3/library/venv.html) for which setup files are prepared.
### Cookies
Although cookies.txt file in not required for bot run, it is recommended as it enables bot to play e.g. YouTube videos marked as +18. More about this file is on yt-dlp Github repo.
