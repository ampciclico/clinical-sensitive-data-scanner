#!/usr/bin/env python3

from pathlib import Path


def get_text_files(directory):
    path = Path(directory)
    
    return list(path.rglob("*.txt"))

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as error:
        print(f"[ERROR] No se pudo leer {file_path}: {error}")
        return ""
