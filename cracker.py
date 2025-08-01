#!/usr/bin/env python3

import PyPDF2
import sys

def crack_pdf(pdf_path, wordlist_path):
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            if not reader.is_encrypted:
                print("[+] PDF is not encrypted.")
                return
            with open(wordlist_path, "r", errors='ignore') as wordlist:
                for i, password in enumerate(wordlist):
                    password = password.strip()
                    try:
                        if reader.decrypt(password):
                            print(f"[+] Password found: {password}")
                            return
                        else:
                            print(f"[-] Attempt {i+1}: {password} - Incorrect")
                    except Exception as e:
                        print(f"[!] Error: {e}")
                        continue
            print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[-] File not found. Check the path.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 cracker.py <encrypted.pdf> <wordlist.txt>")
        sys.exit(1)
    crack_pdf(sys.argv[1], sys.argv[2])
