import asyncio
import threading
from testbot import run_bot, run_bot_sync, client, bot_ready_event
from dotenv import find_dotenv, load_dotenv
import os
import time

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')

asyncio.set_event_loop(asyncio.new_event_loop())


bot_thread = threading.Thread(target=lambda: asyncio.run(run_bot_sync())) 
bot_thread.start()
bot_ready_event.wait()

print("Bot started")
print(client)

discordbot = client

discord_server_task = asyncio.create_task(client.get_guild(1287734077453111327))
time.sleep(3) # TBD
discord_server = discord_server_task.result()

def send_message(channelid, message):
    asyncio.run(client.send_message(channelid, message))

def get_server():
    return discord_server.result()

def create_text_channel():
    return asyncio.run(discord_server.create_text_channel(name="testxd", category=discord_server.categories[1], topic="root/folder1/folder2/folder3/folder4/filename.ext"))