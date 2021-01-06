from discord.ext.commands import Bot as BotBase
from discord import Embed

PREFIX = "$"
OWNER_IDS = [368886902394191872]

class NeroBot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, TOKEN):
        print("Starting...")
        super().run(TOKEN, reconnect=True)
        
    async def on_connect(self):
        print("Nero in connected")
        
    async def on_disconnect(self):
        print("Nero is offline")
        
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("Nero is ready")

            channel = self.get_channel(793304369588076544)
            embed = Embed(title="Now online!", description="Nero is now online!", colour=0xC70039)
            embed.add_field(name="Hello everyone", value="I greet all my masters, i'm here to help you", inline=False)
            await channel.send(embed = embed)
        else:
            print("Nero reconected")

Nero = NeroBot()