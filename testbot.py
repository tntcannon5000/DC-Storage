import os
import discord
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print('------')

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