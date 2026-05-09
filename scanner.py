#!/usr/bin/env python3

import re

from patterns import (
    RUT_PATTERN,
    EMAIL_PATTERN,
    SENSITIVE_KEYWORDS
)

from file_handler import (
    get_text_files,
    read_file
)


def scan_file(file_path):
    content = read_file(file_path)

    ruts = re.findall(RUT_PATTERN, content)
    emails = re.findall(EMAIL_PATTERN, content)

    keyword_matches = []
    
    for keyword in SENSITIVE_KEYWORDS:
        if keyword.lower() in content.lower():
            keyword_matches.append(keyword)

    if ruts or emails or keyword_matches: 
        
        print("=" * 50)
        print("Clinical Sensitive Data Scanner v0.1")
        print("=" * 50)
        print(f"\n[+] Ruta de archivo analizado: \n--> {file_path}\n")

        print(f"\tNumero de RUTs encontrados: {len(ruts)}")
        print(f"\tNumero de Emails encontrados: {len(emails)}")
        print(f"\tNumero de Keywords sensibles encontrados: {len(keyword_matches)}")

        print("\n\t---------------- DETALLES ---------------\n")
        
        print("\t[RUT]")
        for rut in ruts:
            print(f"\t- {rut}")
        
        print("\n\t[EMAIL]")
        for email in emails:
            print(f"\t- {email}")
        
        print("\n\t[KEYWORDS]")
        for keyword in keyword_matches:
            print(f"\t- {keyword}")

        print("\n---------------------------------------------\n")
 
        return True
    return False 

def main():

    target_directory = input("Ingrese directorio a escanear: ")

    files = get_text_files(target_directory)

    
    conteo = 0
    
    for file_path in files:
        result = scan_file(file_path)
        if result:
            conteo += 1
    

    print("Resumen final:")     
    print(f"\n[*] Archivos encontrados: {len(files)}")
    print(f"[!]Archivos con hallazgos: {conteo}")

if __name__ == "__main__":
    main()
