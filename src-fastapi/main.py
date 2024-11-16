# main.py (FastAPI)
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, Response
import os
from pathlib import Path
from typing import List, Dict # added type hints
from fastapi.middleware.cors import CORSMiddleware
import uuid
from io import BytesIO
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# List of UUIDs
uuid_list = [
    "123e4567-e89b-12d3-a456-426614174000",
    "123e4567-e89b-12d3-a456-426614174001",
    "123e4567-e89b-12d3-a456-426614174002",
    "123e4567-e89b-12d3-a456-426614174003",
    "123e4567-e89b-12d3-a456-426614174004"
]

folders = [
    {"uuid": uuid_list[0], "name": "Documents"},
    {"uuid": uuid_list[1], "name": "Pictures"},
    {"uuid": uuid_list[2], "name": "Music"},
    {"uuid": uuid_list[3], "name": "Videos"},
    {"uuid": uuid_list[4], "name": "Downloads"}
]
files = [
    {"uuid": str(uuid.uuid4()), "name": "Puppy Video", "ext": "mp4", "size": "230 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Vacation Photo", "ext": "jpg", "size": "1.5 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Resume", "ext": "pdf", "size": "120 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Favorite Song", "ext": "mp3", "size": "5 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Project Presentation", "ext": "pptx", "size": "2 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Ebook", "ext": "epub", "size": "3 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Financial Spreadsheet", "ext": "xlsx", "size": "500 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Python Script", "ext": "py", "size": "50 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Thesis Document", "ext": "docx", "size": "1 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Design Mockup", "ext": "psd", "size": "10 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "House Blueprint", "ext": "dwg", "size": "8 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Game Installer", "ext": "exe", "size": "500 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Database Backup", "ext": "sql", "size": "20 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Project Archive", "ext": "zip", "size": "100 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Shell Script", "ext": "sh", "size": "10 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Profile Photo", "ext": "png", "size": "2 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Family Video", "ext": "avi", "size": "700 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Audio Recording", "ext": "wav", "size": "50 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Notes", "ext": "txt", "size": "5 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "System Backup", "ext": "bak", "size": "1 GB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Vector Drawing", "ext": "svg", "size": "300 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Custom Font", "ext": "ttf", "size": "200 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "3D Model", "ext": "obj", "size": "15 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Animated GIF", "ext": "gif", "size": "5 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "City Map", "ext": "kml", "size": "1 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Server Log", "ext": "log", "size": "500 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Configuration File", "ext": "cfg", "size": "10 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "SSL Certificate", "ext": "crt", "size": "2 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Private Key", "ext": "key", "size": "1 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Software Patch", "ext": "patch", "size": "100 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Firmware Update", "ext": "bin", "size": "4 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "App Installer", "ext": "msi", "size": "50 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Library File", "ext": "dll", "size": "1 MB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "Website Theme", "ext": "css", "size": "20 KB", "folderid": random.choice(uuid_list)},
    {"uuid": str(uuid.uuid4()), "name": "HTML Template", "ext": "html", "size": "30 KB", "folderid": random.choice(uuid_list)}
]

# Add a specific file to the files list
testfile_path = Path("ffxd.rar")
testfile_path = Path("09.rar")

if testfile_path.exists():
    print(f"Adding {testfile_path} to the files list.")
    files.append({
        "uuid": str(uuid.uuid4()),
        "name": testfile_path.stem,
        "ext": testfile_path.suffix[1:],  # Remove the leading dot
        "size": f"{testfile_path.stat().st_size / 1024:.2f} KB",  # Size in KB
        "folderid": random.choice(uuid_list)
    })  

# Endpoint to get file information
@app.get("/files")
def get_files():
    return files

@app.get("/folders/{uuid}/files")
def get_files(uuid):
    print(uuid)
    folder_files = []

    for file in files:
        if file["folderid"] == uuid:
            folder_files.append(file)

    return folder_files

# Endpoint to get folder information
@app.get("/folders")
def get_folders():
    return folders


# Endpoint to upload files

# Endpoint to download files

@app.get("/download/{file_uuid}")
async def download_file(file_uuid: str):
    file_info = next((file for file in files if file["uuid"] == file_uuid), None)
    if not file_info:
        print(f"File with ID {file_uuid} not found.")
        raise HTTPException(status_code=404, detail="File not found")

    if not os.path.exists(testfile_path):
        print(f"File {testfile_path} does not exist.")
        raise HTTPException(status_code=404, detail="File does not exist")

    filename = f"{file_info['name']}.{file_info['ext']}"
    print(f"Downloading {filename}...")
    #return FileResponse(testfile_path, media_type='application/octet-stream', filename=filename)

    # Return the file as a response
    with open(testfile_path, "rb") as f:
        file_bytes = f.read()

    bytes_io = BytesIO(file_bytes)
    bytes_io.seek(0)

    return Response(bytes_io.read(), media_type='application/octet-stream', headers={
        "Content-Disposition": f"attachment; filename={filename}"
    })