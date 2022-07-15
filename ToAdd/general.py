from ast import alias
from asyncio.windows_events import NULL
import discord, os, ngrok, asyncio, sys
from config import config
from discord.ext import commands
from discord.ext.commands import has_permissions
from musicbot import utils
from musicbot.audiocontroller import AudioController
from musicbot.utils import guild_to_audiocontroller, guild_to_settings
from win10toast import ToastNotifier
from mcipc.query import Client
ng = ngrok.Client(config.NGROK_API)

async def ainput():
    return await asyncio.get_event_loop().run_in_executor(
                        None, sys.stdin.readline)

def IsMinecraftServerOnline():
    try:
        with Client('127.0.0.1', 25565) as client:
            client.stats()
    except:
        return False
    else: 
        return True


class General(commands.Cog):
    """ A collection of the commands for moving the bot around in you server.

            Attributes:
                bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot

    # logic is split to uconnect() for wide usage
    @commands.command(name='connect', description=config.HELP_CONNECT_LONG, help=config.HELP_CONNECT_SHORT, aliases=['c','połącz','pł'])
    async def _connect(self, ctx):  # dest_channel_name: str
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        await audiocontroller.uconnect(ctx)

    @commands.command(name='disconnect', description=config.HELP_DISCONNECT_LONG, help=config.HELP_DISCONNECT_SHORT, aliases=['dc','rozłącz','rz'])
    async def _disconnect(self, ctx, guild=False):
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        await audiocontroller.udisconnect()

    @commands.command(name='reset', description=config.HELP_DISCONNECT_LONG, help=config.HELP_DISCONNECT_SHORT, aliases=['rs', 'restart'])
    async def _reset(self, ctx):
        current_guild = utils.get_guild(self.bot, ctx.message)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} Połączono z {}".format(" ", ctx.author.voice.channel.name))

    @commands.command(name='changechannel', description=config.HELP_CHANGECHANNEL_LONG, help=config.HELP_CHANGECHANNEL_SHORT, aliases=['cc','zmieńkanał','zk'])
    async def _change_channel(self, ctx):
        current_guild = utils.get_guild(self.bot, ctx.message)

        vchannel = await utils.is_connected(ctx)
        if vchannel == ctx.author.voice.channel:
            await ctx.send("{} nie kombinuj, przecież bot jest na {}".format(" ", vchannel.name))
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} zmieniono na {}".format(" ", ctx.author.voice.channel.name))

    @commands.command(name='ping', description=config.HELP_PING_LONG, help=config.HELP_PING_SHORT)
    async def _ping(self, ctx):
        await ctx.send("Pong")

    @commands.command(name='setting', description=config.HELP_SHUFFLE_LONG, help=config.HELP_SETTINGS_SHORT, aliases=['settings', 'set','ustawienia','ust'])
    @has_permissions(administrator=True)
    async def _settings(self, ctx, *args):

        sett = guild_to_settings[ctx.guild]

        if len(args) == 0:
            await ctx.send(embed=await sett.format())
            return

        args_list = list(args)
        args_list.remove(args[0])

        response = await sett.write(args[0], " ".join(args_list), ctx)

        if response is None:
            await ctx.send("`Jak takiego ustawienia nie ma`")
        elif response is True:
            await ctx.send("No i git")

    @commands.command(name='addbot', description=config.HELP_ADDBOT_LONG, help=config.HELP_ADDBOT_SHORT, aliases=['dodajbota'])
    async def _addbot(self, ctx):
        embed = discord.Embed(title="Zaproś", description=config.ADD_MESSAGE +
                              "(https://discordapp.com/oauth2/authorize?client_id={}&scope=bot>)".format(self.bot.user.id))

        await ctx.send(embed=embed)

    @commands.command(name='runserver', description=config.HELP_SERVERMINECRAFT_LONG, help=config.HELP_SERVERMINECRAFT_SHORT, aliases=['uruchomserwer','włączserwer','serverrun'])
    async def _runserver(self, ctx, file):
        if config.LAUNCHINGSERVERENABLED is True:
            if IsMinecraftServerOnline() is False:
                if file in config.SERVERS:
                    os.startfile("shortcuts\\"+file+".lnk")
                    os.startfile("shortcuts\\MinecraftServer.bat")
                    await ctx.send("Serwer się uruchamia. Sprawdź IP serwera komendą -serverip")
                    print("Minecraft server "+file+" started")
                else:
                    await ctx.send("Nie znaleziono takiego serwera")
                    print("Minecraft server "+file+" not found")
            else:
                    for i in ng.endpoints.list():
                        await ctx.send('Serwer jest już włączony i dostępny pod adresem '+i.hostport)
        else: 
            await ctx.send("Funkcja obecnie wyłączona")
            print("Request of Minecraft server start was denied")
    @commands.command(name='showserverlist', description=config.HELP_SHOWSERVERLISTMINECRAFT_LONG, help=config.HELP_SHOWSERVERLISTMINECRAFT_SHORT, aliases=['listaserwerów','serverlist'])
    async def _showserverlist(self, ctx):
        for i in config.SERVERS:
            await ctx.send(i)
    @commands.command(name='showminecraftserverip', description=config.HELP_SHOWSERVERIPMINECRAFT_LONG, help=config.HELP_SHOWSERVERIPMINECRAFT_SHORT, aliases=['ipserwera','serverip','showserverip'])
    async def _showminecraftserverip(self, ctx):
        if config.LAUNCHINGSERVERENABLED is True:   
            for i in ng.endpoints.list():
                await ctx.send(i.hostport)
        else: 
            await ctx.send("Funkcja obecnie wyłączona")
    @commands.command(name='turnoffserver', description=config.HELP_TURNOFFMINECRAFTSERVER_LONG, help=config.HELP_TURNOFFMINECRAFTSERVER_SHORT, aliases=['wyłączserwer','killserver','shutdownserver'])
    async def _turnoffminecraftserver(self, ctx):
        if IsMinecraftServerOnline():
            os.system("taskkill /f /im  java.exe")
        os.system("taskkill /f /im  ngrok.exe")
        await ctx.send("Serwer wyłączony")
    @commands.command(name='conversation', description=config.HELP_CONVERSATION_LONG, help=config.HELP_CONVERSATION_SHORT, aliases=['konwersacja','konserwacja'])
    async def _conversation(self, ctx):
        print('Conversation started at '+ctx.message.guild.name)
        toast = ToastNotifier()
        toast.show_toast(
        "KominiarzMuzyczny",
        "Została rozpoczęta konwersacja na "+ctx.message.guild.name,
        duration = 20,
        icon_path = ".../Matirak.ico",
        threaded = True,
        )
        global context
        context = ctx
        working = True
        while working:
            try:
                line = await ainput()
                line = line.strip()
                if line == 'break':
                    print('Broke with '+ctx.message.guild.name)
                    working = False
                elif line.startswith(('C:\\','C:/')):
                    await ctx.send(file=discord.File(line))
                else:
                    await ctx.send(line)
            except:
                print('An error occurred')
    @commands.command(name='save')
    async def _save(self,ctx):
        for attachment in ctx.message.attachments:
            #await attachment.save(attachment.filename)
            await ctx.send(attachment.url)
def setup(bot):
    bot.add_cog(General(bot))
