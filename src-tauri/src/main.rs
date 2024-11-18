// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::process::Command;

fn main() {
    Command::new("python")
        .arg("-m")
        .arg("uvicorn")
        .arg("main:app")  // Just reference the module directly
        .arg("--reload")
        .current_dir("../src-fastapi")  // Change the working directory to src-fastapi
        .spawn()
        .expect("Failed to start uvicorn server");

    dcstoragetauri_lib::run()
}