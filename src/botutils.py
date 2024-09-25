from src.testbot import run_bot, run_bot_sync, client, bot_ready_event
import asyncio
from dotenv import find_dotenv, load_dotenv
import os
import time
import threading

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')

class StorageBot:
    def __init__(self):
        bot_thread = threading.Thread(target=lambda: asyncio.run(run_bot_sync())) 
        bot_thread.start()
        bot_ready_event.wait()
        print("Bot started")
        self.discord_server = asyncio.run_coroutine_threadsafe(self.set_discord_server(), loop=client.loop).result()
        print("Discord server is " + str(self.discord_server))

    async def send_message(self, channelid, message):
        asyncio.run_coroutine_threadsafe(client.send_message(channelid, message), client.loop)
        #await client.send_message(channelid, message)

    async def get_category(self, name):
        for category in self.discord_server.categories:
            print(category.name)
            if category.name == name:
                return category
        return None

    async def create_text_channel(self, name, category_name, topic):
        #discord_server = await client.get_guild(1287734077453111327)
        return asyncio.run_coroutine_threadsafe(self.discord_server.create_text_channel(name=name, category=await self.get_category(category_name), topic=topic), client.loop).result()

    async def set_discord_server(self):
        self.discord_server = await client.get_guild(1287734077453111327)
        return self.discord_server