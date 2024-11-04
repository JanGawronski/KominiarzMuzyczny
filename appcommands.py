import discord
import config

bot = discord.Bot(intents=discord.Intents.default())


@bot.event
async def on_voice_state_update(member, before, after):
    if member == bot.user and after.channel is None:
        config.guild_to_audiocontroller[member.guild].playlist.playlist = []



@bot.slash_command(name = config.PLAY_COMMAND_NAME, description = config.PLAY_COMMAND_DESCRIPTION)
@discord.option("zapytanie", description = config.MEDIA_ARGUMENT_DESCRIPTION)
@discord.option("strona", description = config.SITE_ARGUMENT_DESCRIPTION, default = "ytsearch", choices = [
discord.OptionChoice(name = "youtube", value = "ytsearch"),
discord.OptionChoice(name = "soundcloud", value = "scsearch"),
discord.OptionChoice(name = "google", value = "gvsearch"),
discord.OptionChoice(name = "yahoo", value = "yvsearch")
])
@discord.guild_only()
async def play(ctx: discord.ApplicationContext, zapytanie: str, strona: str):

    await ctx.response.defer()
    await config.guild_to_audiocontroller[ctx.guild].play(ctx, zapytanie, strona)



@bot.slash_command(name = config.SKIP_COMMAND_NAME, description = config.SKIP_COMMAND_DESCRIPTION)
@discord.guild_only()
async def skip(ctx: discord.ApplicationContext):
    if len(config.guild_to_audiocontroller[ctx.guild].playlist.playlist) == 0:
        await ctx.response.send_message(content = config.QUEUE_IS_EMPTY_MESSAGE, ephemeral = True)
    else:
        config.guild_to_audiocontroller[ctx.guild].next(ctx)
        await ctx.response.send_message(content = config.SKIP_MESSAGE)
    


@bot.slash_command(name = config.PREVIOUS_SONG_COMMAND_NAME, description = config.PREVIOUS_SONG_COMMAND_DESCRIPTION)
@discord.guild_only()
async def previous_song(ctx: discord.ApplicationContext):
    if config.guild_to_audiocontroller[ctx.guild].playlist.history == []:
        await ctx.response.send_message(content = config.HISTORY_IS_EMPTY_MESSAGE, ephemeral = True)
    else:
        await config.guild_to_audiocontroller[ctx.guild].previous(ctx)
        await ctx.response.send_message(content = config.PREVIOUS_SONG_MESSAGE)



@bot.slash_command(name = config.LOOP_COMMAND_NAME, description = config.LOOP_COMMAND_DESCRIPTION)
@discord.guild_only()
async def loop(ctx: discord.ApplicationContext):
    if config.guild_to_audiocontroller[ctx.guild].playlist.loop == True:

        await ctx.response.send_message(content = config.DISABLE_LOOP_MESSAGE)
    else:
        
        await ctx.response.send_message(content = config.ENABLE_LOOP_MESSAGE)
    config.guild_to_audiocontroller[ctx.guild].playlist.toggleLoop()



@bot.slash_command(name = config.SHUFFLE_COMMAND_NAME, description = config.SHUFFLE_COMMAND_DESCRIPTION)
@discord.guild_only()
async def shuffle(ctx: discord.ApplicationContext):
    if len(config.guild_to_audiocontroller[ctx.guild].playlist.playlist) <= 1:

        await ctx.response.send_message(content = config.QUEUE_IS_EMPTY_MESSAGE, ephemeral = True)
    else:

        config.guild_to_audiocontroller[ctx.guild].playlist.shuffle()
        await ctx.response.send_message(content = config.SHUFFLE_MESSAGE)



@bot.slash_command(name = config.DISCONNECT_COMMAND_NAME, description = config.DISCONNECT_COMMAND_DESCRIPTION)
@discord.guild_only()
async def disconnect(ctx: discord.ApplicationContext):
    await ctx.response.send_message(content = config.DISCONNECTION_MESSAGE, ephemeral = True)
    try:
        await ctx.guild.voice_client.disconnect(force=True)
    except:
        pass



@bot.slash_command(name = config.CHANGE_CHANNEL_COMMAND_NAME, description = config.CHANGE_CHANNEL_COMMAND_DESCRIPTION)
@discord.guild_only()
async def change_channel(ctx: discord.ApplicationContext):

    if ctx.guild.voice_client is None or ctx.user.voice is None:

        await ctx.response.send_message(content = config.FAILED_TO_JOIN_VC_MESSAGE, ephemeral = True)
    elif ctx.guild.voice_client.channel == ctx.user.voice.channel:

        await ctx.response.send_message(content = config.CLIENT_AND_USER_IN_THE_SAME_CHANNEL_MESSAGE, ephemeral = True)
    else:

        await ctx.guild.voice_client.move_to(ctx.user.voice.channel)
        await ctx.response.send_message(content = config.CHANNEL_CHANGED_MESSAGE, ephemeral = True)



@bot.slash_command(name = config.CLEAR_QUEUE_COMMAND_NAME, description = config.CLEAR_QUEUE_COMMAND_DESCRIPTION)
@discord.guild_only()
async def clear_queue(ctx: discord.ApplicationContext):
    if len(config.guild_to_audiocontroller[ctx.guild].playlist.playlist) <= 1:

        await ctx.response.send_message(content = config.QUEUE_IS_EMPTY_MESSAGE, ephemeral = True)
    else:
    
        config.guild_to_audiocontroller[ctx.guild].playlist.clear_queue()
        await ctx.response.send_message(content = config.CLEAR_QUEUE_MESSAGE)



@bot.slash_command(name = config.CLEAR_HISTORY_COMMAND_NAME, description = config.CLEAR_HISTORY_COMMAND_DESCRIPTION)
@discord.guild_only()
async def clear_history(ctx: discord.ApplicationContext):
    if len(config.guild_to_audiocontroller[ctx.guild].playlist.history) == 0:

        await ctx.response.send_message(content = config.HISTORY_IS_EMPTY_MESSAGE, ephemeral = True)
    else:
    
        config.guild_to_audiocontroller[ctx.guild].playlist.clear_history()
        await ctx.response.send_message(content = config.CLEAR_HISTORY_MESSAGE)



@bot.slash_command(name = config.DISPLAY_QUEUE_COMMAND_NAME, description = config.DISPLAY_QUEUE_COMMAND_DESCRIPTION)
@discord.guild_only()
async def display_queue(ctx: discord.ApplicationContext):

    if len(config.guild_to_audiocontroller[ctx.guild].playlist.playlist) <= 1:

        await ctx.response.send_message(content = config.QUEUE_IS_EMPTY_MESSAGE, ephemeral = True)
    else:

        await config.guild_to_audiocontroller[ctx.guild].display_queue(ctx)



@bot.slash_command(name = config.DISPLAY_HISTORY_COMMAND_NAME, description = config.DISPLAY_HISTORY_COMMAND_DESCRIPTION)
@discord.guild_only()
async def display_history(ctx: discord.ApplicationContext):

    if len(config.guild_to_audiocontroller[ctx.guild].playlist.history) == 0:

        await ctx.response.send_message(content = config.HISTORY_IS_EMPTY_MESSAGE, ephemeral = True)
    else:

        await config.guild_to_audiocontroller[ctx.guild].display_history(ctx)
