# main.py (FastAPI)
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, Response
import os
from pathlib import Path
from typing import List, Dict # added type hints
from fastapi.middleware.cors import CORSMiddleware
import uuid
from io import BytesIO

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

files = [
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"},
    {"uuid": str(uuid.uuid4()), "name": "file1", "ext": "txt", "size": "2 KB"}
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
        "size": f"{testfile_path.stat().st_size / 1024:.2f} KB"  # Size in KB
    })  

# Endpoint to get file information
@app.get("/files")
def get_files():
    return files

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
    