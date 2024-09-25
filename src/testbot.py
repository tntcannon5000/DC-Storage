import os
import discord
from dotenv import load_dotenv
import asyncio
import threading

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot_ready_event = threading.Event()


class MyClient(discord.Client):    
    async def on_ready(self):
        print('Logged on as', self.user)
        print('------')
        bot_ready_event.set()
        
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

    async def on_message_edit(self, before, after):
        await after.reply('You edited a message!')

    async def send_message(self, channelid, message):
        channel = self.get_channel(channelid)
        if channel:
            await channel.send(message)
        else:
            print(f"Channel with id {channelid} not found")
        
        return channel
    
    async def get_guild(self, id: int) -> discord.Guild | None:
        return super().get_guild(id)


client = MyClient(intents=discord.Intents.all())

# Create a function to start the bot asynchronously
async def start_bot():
    await client.start(TOKEN)
    

# Create a function to stop the bot
async def stop_bot():
    await client.close()

# Create an asyncio task to run the bot in the background
def run_bot():
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())

def run_bot_sync():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())