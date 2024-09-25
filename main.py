from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from src.botutils import StorageBot
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')

app = FastAPI()

storage_bot = StorageBot()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        return file.read()

@app.get("/send_message")
async def send_message_route():
    channel_id = 1287734078124068866  # Replace with your channel ID
    message = "Hello from Jupyter!"
    await storage_bot.send_message(channelid=channel_id, message=message)
    return JSONResponse({"message": "Message sent to Discord!"})

@app.get("/create_channel") 
async def create_channel_route():
    channel = await storage_bot.create_text_channel(name="new-channel-from-api", category_name="tables", topic="This channel was created from an API!")
    return JSONResponse({"message": f"Text channel '{channel}' created!"})