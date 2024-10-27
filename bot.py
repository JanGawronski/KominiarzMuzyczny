from appcommands import bot
from audiocontroller import AudioCotroller
import config
import logging

@bot.event
async def on_ready():

    for guild in bot.guilds:
        await register(guild)

    print(f"{bot.user} is ready")



@bot.event
async def on_guild_join(guild):
    await register(guild)


async def register(guild):

    config.guild_to_audiocontroller[guild] = AudioCotroller(guild, bot)
    print(f"Joined {guild}")
    

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot.run(config.BOT_TOKEN)