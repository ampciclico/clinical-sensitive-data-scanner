#!/usr/bin/env python3

import sys
import re
import os
import argparse

from patterns import (
    RUT_PATTERN,
    EMAIL_PATTERN,
    SENSITIVE_KEYWORDS
)

from file_handler import (
    get_text_files,
    read_file
)


def get_argument():
    parser = argparse.ArgumentParser(description="Clinical Sensitive Data Scanner")
    parser.add_argument("-d", "--directory", dest="target_directory", help="Directory to Scan")
    options = parser.parse_args()

    if options.target_directory is None:
        parser.print_help()
        sys.exit(1)

    return options.target_directory

def scan_file(file_path):
    try:
        content = read_file(file_path)
    except Exception as e:
        print(f"[!!] Archivo no legible o no existe {file_path}:{e}")
        return None

    ruts = sorted(set(re.findall(RUT_PATTERN, content)))
    emails = sorted(set(re.findall(EMAIL_PATTERN, content)))

    content_lower = content.lower()
    keyword_matches = []
    for keyword in SENSITIVE_KEYWORDS:
        if keyword.lower() in content_lower:
            keyword_matches.append(keyword)

    if ruts or emails or keyword_matches:    
        
        sensitive_data = {
                "metadata": {
                    "archivo": file_path
                    },
                "datos": {
                    "ruts": ruts,
                    "emails": emails,
                    "keywords": keyword_matches
                    }   
                }

        return sensitive_data
    return None

def display_results(files):
    
    print("=" * 50)
    print("Clinical Sensitive Data Scanner v0.1")
    print("=" * 50)
    print("\n------------------- DETALLES --------------------------\n")
     
    all_sensitive_data = {}    
    
    print(f"[!] Archivos encontrados y que seran analizados ---> [{len(files)}]\n")
    
    archivos = []

    for file in files: 
        sensitive_data = scan_file(file)
        if sensitive_data:
            datos = sensitive_data.get("datos", {})
            archivo = os.path.basename(file)    
            all_sensitive_data[archivo] = {
                "ruts": datos.get("ruts", []), 
                "emails": datos.get("emails", []),
                "keywords": datos.get("keywords", [])
            }
            archivos.append(archivo)

    print(f"Archivos comprometidos detectados: {'. '.join(a for a in archivos)}") 
    for archivo, datos in all_sensitive_data.items():
        ruts_output = '\n- ' + '\n- '.join(datos['ruts'])
        emails_output = '\n- ' + '\n- '.join(datos['emails'])
        keywords_output = '\n- ' + '\n- '.join(datos['keywords'])

        print(f"\nArchivo analizado ---> {archivo}") 
        print(f"\n[!] [RUTS]: {ruts_output}")
        print(f"\n[!] [EMAILS]: {emails_output}")
        print(f"\n[!] [KEYWORDS]: {keywords_output}")

def main():
    
    target_directory = get_argument()
    files = get_text_files(target_directory)
    display_results(files)

if __name__ == "__main__":
    main()
