from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import find_dotenv, load_dotenv
import os
import asyncio
import threading
from testbot import bot, run_bot, send_message

load_dotenv(find_dotenv())

app = FastAPI()

# Start the bot in a separate thread
bot_thread = threading.Thread(target=run_bot)
bot_thread.start()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        return file.read()

@app.get("/test")
async def test_function():
    channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))  # Make sure to add this to your .env file
    await send_message(channel_id, "Hello from FastAPI!")
    return JSONResponse({"message": "Message sent to Discord!"})
