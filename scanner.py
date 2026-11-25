#!/usr/bin/env python3

import re
import os
import argparse
from termcolor import colored
import signal
import sys
import json

from patterns import (
    RUT_PATTERN,
    EMAIL_PATTERN,
    SENSITIVE_KEYWORDS
)

from file_handler import (
    get_text_files,
    read_file
)

def signal_handler(sig, frame):
    print(colored(f"\n[!] Scanner detenido por el usuario\n", "red"))
    
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

def get_argument():
    parser = argparse.ArgumentParser(description="Clinical Sensitive Data Scanner")
    parser.add_argument("-d", "--directory", required=True, dest="target_directory", help="Directory to Scan")
    parser.add_argument("-o", "--output", help="Genera un reporte en Json")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    
    args = parser.parse_args()
    if not args.json and args.output:
        parser.error("-o/--output requiere --json")

    return args


def display_results(files, args):
 
    all_sensitive_data = {}    
    archivos = []

    files_with_findings = 0 # contabiliza cuántos archivos contienen información sensible:

    for file in files: 
        sensitive_data = scan_file(file)
        if sensitive_data:
            
            files_with_findings += 1 # en cada pasada True, se agrega +1

            datos = sensitive_data.get("datos", {})
            archivo = os.path.basename(file)    
            all_sensitive_data[archivo] = {
                "ruts": datos.get("ruts", []), 
                "emails": datos.get("emails", []),
                "keywords": datos.get("keywords", [])
            }
            archivos.append(archivo)
     
    if not args.json:
        
        print(f"[!] Archivos encontrados y que seran analizados ---> [{len(files)}]\n")

        print(colored("=" * 50, "yellow"))
        print(colored("Clinical Sensitive Data Scanner v0.1", "red"))
        print(colored("=" * 50, "yellow"))
        print("\n------------------- DETALLES --------------------------\n")
         
        print(f"Archivos comprometidos detectados: {', '.join(archivos)}") 
        for archivo, datos in all_sensitive_data.items():
            ruts_output = '\n- ' + '\n- '.join(datos['ruts'])
            emails_output = '\n- ' + '\n- '.join(datos['emails'])
            keywords_output = '\n- ' + '\n- '.join(datos['keywords'])

            print(f"\nArchivo analizado ---> {archivo}") 
            print(colored(f"\n[!] [RUTS]: {ruts_output}", "red"))
            print(colored(f"\n[!] [EMAILS]: {emails_output}", "blue"))
            print(colored(f"\n[!] [KEYWORDS]: {keywords_output}", "cyan"))

    else:
        
        output = {
            "summary": {
            "files_scanned": len(files),
            "files_with_findings": files_with_findings
                        },
            "results": all_sensitive_data
                }

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=4, ensure_ascii=False)

            print(f"[+] Reporte en json guardado como --> {args.output}")
        else:
            print(json.dumps(output, indent=4, ensure_ascii=False))
    
    # sección resumen en JSON con estadísticas globales del escaneo:
    # Permite conocer inmediatamente cuántos archivos fueron analizados.
    # Permite conocer cuántos archivos contienen datos sensibles.
    # Separa metadatos del reporte de los resultados del escaneo.
    # Facilita futuras ampliaciones del formato JSON.
    # Acerca la estructura a formatos utilizados en herramientas profesionales de análisis y monitoreo.
   
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

def main():
    
    args = get_argument()
    files = get_text_files(args.target_directory)
    display_results(files, args)

if __name__ == "__main__":
    main()
