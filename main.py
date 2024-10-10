# main.py (FastAPI backend)
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent # for getting current directory, can adjust

app = FastAPI()

# ... (Other imports if needed)

# Serving static files (if you're serving the 'dist' directory directly with FastAPI)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "dist/assets")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "dist")) # update template path

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) # server index.html

# File upload endpoint
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    uploads_dir = BASE_DIR / "uploads"
    uploads_dir.mkdir(exist_ok=True) # makes uploads directory if doesnt exist yet
    file_location = uploads_dir / file.filename
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


# Get files endpoint
@app.get("/files/")
async def get_files():
    files = []
    uploads_dir = BASE_DIR / "uploads"
    if uploads_dir.exists():
        for filename in os.listdir(uploads_dir):
            size = os.path.getsize(uploads_dir / filename)
            files.append({"name": filename, "size": size})
    return files