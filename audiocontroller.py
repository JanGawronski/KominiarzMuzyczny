import discord
from yt_dlp import YoutubeDL
import sponsorblock
import config
import playlist
import asyncio
import pyshorteners
import datetime
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = None
if config.SPOTIFY_CLIENT_ID != "" and config.SPOTIFY_CLIENT_SECRET != "":
    try:
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET))
    except:
        pass
sb = sponsorblock.Client()
urlshortener = pyshorteners.Shortener()


class YoutubeLogger:

    def info(msg):
        with open("discord.log", "a", encoding = "utf-8") as file:
            file.write(f"{str(datetime.datetime.now())[:-3]}:INFO:yt_dlp:{msg}\n")
    
    def warning(msg):
        with open("discord.log", "a", encoding = "utf-8") as file:
            file.write(f"{str(datetime.datetime.now())[:-3]}:WARNING:yt_dlp:{msg}\n")
    
    def error(msg):
        with open("discord.log", "a", encoding = "utf-8") as file:
            file.write(f"{str(datetime.datetime.now())[:-3]}:ERROR:yt_dlp:{msg}\n")


    def debug(msg):
        with open("discord.log", "a", encoding = "utf-8") as file:
            file.write(f"{str(datetime.datetime.now())[:-3]}:DEBUG:yt_dlp:{msg}\n")


class AudioCotroller:

    def __init__(self, guild, client):
        self.guild = guild
        self.playlist = playlist.Playlist()
        self.client = client


    async def connect(self, user):
        if self.guild.voice_client is None:
            if user.voice is not None:
                await user.voice.channel.connect()
            else:
                raise Exception



    async def play(self, ctx, query, site):

        if self.guild.voice_client is None and ctx.user.voice is None:
            await ctx.followup.send(config.FAILED_TO_JOIN_VC_MESSAGE, ephemeral = True)
            self.playlist.playlist = []
            return

        #try:
        playlist_data = self.process_song(query, site)
        #except:
        #    await ctx.followup.send(config.SONG_NOT_FOUND_MESSAGE, ephemeral = True)
        #    return


        try:
            await self.connect(ctx.user)
        except:
            await ctx.followup.send(config.FAILED_TO_JOIN_VC_MESSAGE, ephemeral = True)
            self.playlist.playlist = []
            return
        

        if playlist_data is None:
            
            if not self.guild.voice_client.is_playing():

                await self.play_audiosource(ctx, True)
            else:

                await ctx.followup.send(config.ADDED_TO_QUEUE_MESSAGE.format(self.playlist.playlist[-1]["title"]))
        else:
            
            await ctx.followup.send(config.ADDED_PLAYLIST_TO_QUEUE_MESSAGE.format(playlist_data["title"]))        

            if not self.guild.voice_client.is_playing():
                await self.play_audiosource(ctx)
            

            await asyncio.to_thread(self.process_playlist, playlist_data["songs"], playlist_data["is_spotify"])

    
    async def play_audiosource(self, ctx, followup = False):
        
        #Checks if url from Soundcloud expired
        if "soundcloud" in self.playlist.playlist[0]["webpage_url"]:
            try:
                r = requests.get(self.playlist.playlist[0]["url"])
                if r.status_code != 200:
                    self.playlist.playlist[0] = self.process_song(self.playlist.playlist[0]["webpage_url"], to_return = True)
            except:
                pass

        #Creates discord embed to send
        embed = discord.Embed(title = self.playlist.playlist[0]["title"] 
                              if self.playlist.playlist[0]["track"] is None else self.playlist.playlist[0]["track"],
                              url = self.playlist.playlist[0]["webpage_url"])
        
        if self.playlist.playlist[0]["short_url"] is not None:
            embed.set_author(name = config.NOW_PLAYING_EMBED_STRING, url = self.playlist.playlist[0]["short_url"])
        else:
            embed.set_author(name = config.NOW_PLAYING_EMBED_STRING)

        if self.playlist.playlist[0]["thumbnail"] is not None:
            embed.set_thumbnail(url = self.playlist.playlist[0]["thumbnail"])

        if self.playlist.playlist[0]["artist"] is not None:
            embed.add_field(name = config.AUTHOR_EMBED_STRING, value = self.playlist.playlist[0]["artist"], inline = True)
        elif self.playlist.playlist[0]["uploader"] is not None:
            embed.add_field(name = config.UPLOADER_EMBED_STRING , value = self.playlist.playlist[0]["uploader"], inline = True)
        
        if len(self.playlist.playlist) - 1 > 0:
            embed.add_field(name = config.QUEUE_LENGTH_EMBED_STRING, value = len(self.playlist.playlist) - 1, inline = True)

        if self.playlist.playlist[0]["is_live"]:
            embed.add_field(name = config.DURATION_EMBED_STRING, value = config.IS_LIVE_EMBED_VALUE, inline = True)
        elif self.playlist.playlist[0]["long_string_duration"] is not None:
            embed.add_field(name = config.DURATION_EMBED_STRING, value = self.playlist.playlist[0]["long_string_duration"] , inline = True)
        
        if followup:
            await ctx.followup.send(embed = embed)
        else:
            await ctx.channel.send(embed = embed)
        

        self.guild.voice_client.play(discord.FFmpegOpusAudio(
            source = self.playlist.playlist[0]["url"],
            before_options = self.playlist.playlist[0]["before_options"],
            options = self.playlist.playlist[0]["options"]), 
            after = lambda e: self.next(ctx, e))


    def process_song(self, query, site = "ytsearch", to_return = False):
        
        song_info = None
        if "\\" in query:
            query = query.replace("\\", "/")

        try:
            if "/" not in query:

                #Handles non link queries
                if ":" in query:
                    query = query.replace(":", " ")

                with YoutubeDL({'format': 'bestaudio/best', 'quiet': False, "cookiefile": config.PATH_TO_COOKIES, "logger": YoutubeLogger, 'default_search': site}) as ydl:
                    song_info = ydl.extract_info(f"\"{query}\"", download=False)["entries"][0]

                #Redirects unavailable songs from Soundcloud to YouTube
                if "preview" in song_info["url"] and "soundcloud" in song_info["webpage_url"]:
                    with YoutubeDL({'format': 'bestaudio/best', 'quiet': False, "cookiefile": config.PATH_TO_COOKIES, "logger": YoutubeLogger, 'default_search': "ytsearch"}) as ydl:
                        song_info = ydl.extract_info(f"\"{query}\"", download=False)["entries"][0]
            else:
                
                #Handles Spotify playlists and albums
                if "spotify.com/" in query and spotify is not None:
                    if "/track/" in query:
                        
                        query = spotify.track(query)
                        self.process_song(query = query, site = "scsearch")
                        return
                    
                    elif "/playlist/" in query:
                        
                        query = spotify.playlist(query)
                        self.process_song(query["tracks"]["items"][0]["track"]["name"])

                        return {"title": query["name"], "songs": query["tracks"]["items"][1:], "is_spotify": True}

                    elif "/album/" in query:

                        query = spotify.album_tracks(query)
                        self.process_song(query["items"][0])

                        return {"title": query["name"], "songs": query["items"][1:], "is_spotify": True}
                        
                #Handles non-Spotify links
                with YoutubeDL({'format': 'bestaudio/best', 'quiet': False, "cookiefile": config.PATH_TO_COOKIES, "logger": YoutubeLogger, "extract_flat": "in_playlist"}) as ydl:
                    song_info = ydl.extract_info(query, download=False)
        except:
            try:
                
                #Redirects unavailable songs from YouTube to WebArchive
                for prefix in ["youtu.be/", "youtube.com/watch?v="]:
                    if prefix in query:
                        query = "ytarchive:" + query[query.find(prefix) + len(prefix):]
                        break
                else:
                    raise Exception

                with YoutubeDL({'format': 'bestaudio/best', 'quiet': False, "cookiefile": config.PATH_TO_COOKIES, "logger": YoutubeLogger, "extract_flat": "in_playlist", "socket_timeout": 3}) as ydl:
                        song_info = ydl.extract_info(query, download=False)

                song_info["webpage_url"] = "https://www.youtube.com/watch?v=" + song_info["id"]
            except:

                raise Exception


        if song_info.get("url") is None and song_info.get("_type") != "playlist":
            raise Exception
        

        if song_info.get("_type") == "playlist":

            for song_index in range(len(song_info["entries"])):
                try:
                    self.process_song(song_info["entries"][song_index]["url"])
                
                except:
                    continue
            
                return {"title": song_info["title"], "songs": song_info["entries"][song_index + 1:], "is_spotify": False}
        

        before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        options = "-vn"

        #Searches Sponsorblock database and cuts segments
        try:
            segments = sb.get_skip_segments(song_info["webpage_url"])
            cut_times = ""

            for segment in segments:

                if segment.category in ["sponsor", "selfpromo", "interaction", "intro", "outro", "preview", "music_offtopic"] and segment.start != segment.end:
                    
                    cut_times += f"between(t,{str(segment.start)},{str(segment.end)})+"

                    if isinstance(song_info.get("duration"), (int, float)):
                        song_info["duration"] -= segment.end - segment.start
            
            if cut_times.endswith("+"):
                cut_times = cut_times[:-1]
            
            if song_info.get("duration") > 1200:
                cut_times = ""
            
            if cut_times != "":
                options = f"-vn -af \"aselect=\'not({cut_times})\',asetpts=N/SR/TB\""
            print(cut_times)
        except:
            pass



        if isinstance(song_info.get("duration"), (int, float)):

            song_info["duration"] = round(song_info["duration"])
            m, s = divmod(song_info["duration"], 60)

            if m < 60:
                song_info["short_string_duration"] = f"{m:d}:{s:02d}"
            
            h, m = divmod(m, 60)

            if h >= 1:
                song_info["short_string_duration"] = f"{h:d}:{m:02d}:{s:02d}"
            
            song_info["long_string_duration"] = f"{h:d}:{m:02d}:{s:02d}"


        else:
            song_info["duration"] = None
            song_info["short_string_duration"] = ""
            song_info["long_string_duration"] = None


        
        if not song_info.get("is_live"):
            try:
                song_info["short_url"] = urlshortener.tinyurl.short(song_info.get("url"))
            except:
                song_info["short_url"] = song_info["url"]
                


        song = {k: song_info[k] for k in ["title", "url"]}
        song["before_options"] = before_options
        song["options"] = options
        song["thumbnail"] = song_info.get("thumbnail")
        song["uploader"] = song_info.get("uploader")
        song["artist"] = song_info.get("artist")
        song["track"] = song_info.get("track")
        song["duration"] = song_info.get("duration")
        song["short_string_duration"] = song_info.get("short_string_duration")
        song["long_string_duration"] = song_info.get("long_string_duration")
        song["is_live"] = song_info.get("is_live")
        song["webpage_url"] = song_info.get("webpage_url")
        song["short_url"] = song_info["short_url"]

        if to_return:
            return song

        self.playlist.add(song)


    def process_playlist(self, songs, is_spotify):

        if is_spotify:

            for song in songs:
                
                if self.guild.voice_client is None:
                    return
                try:
                    self.process_song(song["track"]["name"], "scsearch")
                except:
                    pass


        else:
            for song in songs:

                if self.guild.voice_client is None:
                    return
                try:
                    self.process_song(song["url"])
                except:
                    pass
    
    


    def next(self, ctx, e = None):

        if e is not None:
            YoutubeLogger.error(e)

        if self.guild.voice_client is None:
            return

        if self.guild.voice_client.is_playing():
            if self.playlist.loop:
                self.playlist.loop == "Skip, but still True"

            self.guild.voice_client.stop()
            return
        else:

            self.playlist.next()


        if len(self.playlist.playlist) == 0:
            discon = asyncio.run_coroutine_threadsafe(self.guild.voice_client.disconnect(force=True), self.client.loop)
            try:
                discon.result()
            except:
                pass
            return
        
        
        playing = asyncio.run_coroutine_threadsafe(self.play_audiosource(ctx), self.client.loop)
        try:
            playing.result()
        except:
            pass

    

    async def previous(self, ctx):
        self.playlist.previous()
        if self.guild.voice_client is None:
            await self.connect(ctx.user)
            await self.play_audiosource(ctx)
        else:
            self.next(ctx)



    async def display_queue(self, ctx):

        embeds = []
        fields = []
        
        index = 1
        for song in self.playlist.playlist[1:]:
            fields.append(discord.EmbedField(name = "", value = "{}. {} [{}]".format(str(index), song["title"], song["short_string_duration"])))
            index += 1

        queue_duration = 0

        for song in self.playlist.playlist[1:]:
            if isinstance(song["duration"], (int, float)):
                queue_duration += song["duration"]
        
        if queue_duration > 0:
        
            m, s = divmod(queue_duration, 60)
            if m < 60:
                queue_duration = f" [{m:d}:{s:02d}]"
            else:
                h, m = divmod(m, 60)
                queue_duration = f" [{h:d}:{m:02d}:{s:02d}]"
        else:

            queue_duration = ""

        
        embeds.append(discord.Embed(title = self.playlist.playlist[0]["title"] + f" [{config.NOW_PLAYING_EMBED_STRING}]",
                              url = self.playlist.playlist[0]["webpage_url"],
                              fields = fields[:25]))
        

        fields_appended = 25
        while fields_appended < len(fields):
            embeds.append(discord.Embed(fields = fields[fields_appended:fields_appended + 25]))
            fields_appended += 25



        embeds[0].set_author(name = config.QUEUE_EMBED_STRING + queue_duration)

        if self.playlist.playlist[0]["thumbnail"] is not None:
            embeds[0].set_thumbnail(url = self.playlist.playlist[0]["thumbnail"])
        

        chars_sent = 0
        embeds_sent = 0
        await ctx.response.send_message(embeds = embeds)


    async def display_history(self, ctx):

        embeds = []
        fields = []

        index = 1
        for song in self.playlist.history:
            fields.append(discord.EmbedField(name = "", value = "{}. {}".format(str(index), song["title"])))
            index += 1

        fields_appended = 0
        while fields_appended < len(fields):
            embeds.append(discord.Embed(fields = fields[fields_appended:fields_appended + 25]))
            fields_appended += 25

        embeds[0].set_author(name = config.HISTORY_EMBED_STRING)

        await ctx.response.send_message(embeds = embeds)