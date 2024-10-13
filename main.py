# main.py (FastAPI)
from fastapi import FastAPI, UploadFile, File
import os
from pathlib import Path
from typing import List, Dict # added type hints
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)


files = [
    {"name": "file1.txt", "size": "2 KB"},
    {"name": "file2.jpg", "size": "5 MB"},
    {"name": "file3.pdf", "size": "500 KB"}
]

# Endpoint to get file information
@app.get("/files")
def get_files():
    return files