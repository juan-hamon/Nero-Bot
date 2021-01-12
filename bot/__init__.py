import os
from asyncio import sleep
from discord import Intents
from discord.ext.commands import Bot
from discord import Embed
from settings import GUILD, LOG_CHANNEL, OWNER_ID

PREFIX = "$"
OWNER_IDS = [OWNER_ID]
COGS = []

def load_cogs():
    for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                COGS.append(filename[:-3])

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class NeroBot(Bot):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents = Intents.all())
    
    def setup(self):  
        for cog in COGS:
            self.load_extension(f'cogs.{cog}')
            print(f"{cog} cog loaded")
        print("Setup complete!")

    def run(self, TOKEN):
        print("Starting...")
        print("Running setup...")
        self.setup()
        print("Running bot...")
        super().run(TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("Nero is connected!")
    
    async def on_disconnect(self):
        print("Nero is offline")
    
    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(GUILD)
            while not self.cogs_ready.all_ready():
                await sleep(0.5)
            self.ready = True
            print("Nero is ready!")
            channel = self.get_channel(LOG_CHANNEL)
            embed = Embed(title="Now online!", description="Nero is now online!", colour=0xC70039)
            embed.add_field(name="Hello everyone", value="I greet all my masters, i'm here to help you.", inline=False)
            await channel.send(embed = embed)
        else:
            print("Nero reconected")

load_cogs()
Nero = NeroBot()