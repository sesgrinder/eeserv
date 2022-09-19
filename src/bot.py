import discord
from discord import ui
from discord.ext import commands
import asyncio


from collections import Counter, defaultdict
import utils
import local_param

description = """
Almighty bot \n
"""

@utils.listify
def _get_extensions(param):
    yield 'modules.basic_mod'
    yield 'modules.jokes'
    yield 'modules.8ball'
    if param.get('release') == "development":
        yield 'modules.debug'
        yield 'modules.test'
    
class EEServ(commands.AutoShardedBot):
    user: discord.ClientUser
    log_handler: any
    bot_app_inf: discord.AppInfo

    commands_stat: Counter[str]
    socket_stat: Counter[str]
    command_type_used: Counter[bool]

    def __init__ (self,param):
        allowed_mention = discord.AllowedMentions(roles=False, everyone=False, users=True)
        intents = discord.Intents(
            guilds = True,
            members = True,
            bans=True,
            emojis=True,
            voice_states=True,
            messages=True,
            reactions=True,
            message_content=True)
        super().__init__(
            command_prefix = '?',
            description = description,
            pm_help = None,
            allowed_mention = allowed_mention,
            intents = intents,
            enable_debug_events = True,
            heartbeat_timeout = 200.0,
            chunk_guild_at_startup = False
        )

        self.param = param # param: Parameters class holding custom settings
    
    async def on_ready(self):
        for ext in _get_extensions(self.param):
            await self.load_extension(ext)

        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def start_bot(self)->None:
        await self.start(self.param.get("token"))
        await self.change_presence(status=local_param.get_status(self.param.get("status"))) #[FIXME]: Get an activity for this client

    async def close_bot(self)->None:
        await self.close()
        await self.session.close()
    