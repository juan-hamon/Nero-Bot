import os
from discord import Intents
from discord.ext.commands import Bot as BotBase
from discord import Embed

PREFIX = "$"
OWNER_IDS = [368886902394191872]

class NeroBot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents = Intents.all())
    
    def setup(self):
        #se cargan los cogs de forma automática utilizandolos como modulos
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                self.load_extension(f'cogs.{filename[:-3]}')
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
            self.ready = True
            print("Nero is ready!")
            channel = self.get_channel(796792514861989888)
            embed = Embed(title="Now online!", description="Nero is now online!", colour=0xC70039)
            embed.add_field(name="Hello everyone", value="I greet all my masters, i'm here to help you", inline=False)
            await channel.send(embed = embed)
        else:
            print("Nero reconected")

Nero = NeroBot()