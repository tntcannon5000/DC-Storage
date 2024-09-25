import asyncio
import threading
from src.testbot import run_bot, run_bot_sync, client, bot_ready_event
from dotenv import find_dotenv, load_dotenv
import os
import time

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')

bot_thread = threading.Thread(target=lambda: asyncio.run(run_bot_sync())) 
bot_thread.start()
bot_ready_event.wait()

print("Bot started")
print(client)

discordbot = client

# Fetch the discord server in the bot's event loop using run_coroutine_threadsafe
async def fetch_discord_server():
    # Wait for the bot to be ready before fetching the guild
    while not client.is_ready():
        print("Waiting for bot to be ready...")
        await asyncio.sleep(1)

    # Fetch the guild asynchronously
    discord_server = await client.get_guild(1287734077453111327)
    print(discord_server)
    return discord_server

# Schedule the coroutine in the bot's event loop and get the result
future = asyncio.run_coroutine_threadsafe(fetch_discord_server(), client.loop)
discord_server = future.result()  # Block until the result is available

async def send_message(channelid, message):
    #asyncio.run(client.send_message(channelid, message))
    await client.send_message(channelid, message)

def create_text_channel():
    return asyncio.run(discord_server.create_text_channel(name="testxd", category=discord_server.categories[1], topic="root/folder1/folder2/folder3/folder4/filename.ext"))