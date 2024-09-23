from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import asyncio
from testbot import client, run_bot
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')

app = FastAPI()

# Start the bot in the background
run_bot()

# Define a function to send a message
async def send_message_to_channel(channel_id, message):
    await client.send_message(channel_id, message)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        return file.read()

@app.get("/test")
async def test_function():
    channel_id = 1287734078124068866  # Replace with your channel ID
    message = "Hello from Jupyter!"
    await client.send_message(channel_id, message)
    return JSONResponse({"message": "Message sent to Discord!"})
