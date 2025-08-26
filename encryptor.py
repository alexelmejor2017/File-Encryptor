import sys
import os
import tkinter as tk
from tkinter import filedialog
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet

RAW_KEY = "" # Place your 32 bit key here

def make_cipher(raw_key):
    raw_bytes = raw_key.encode('utf-8')
    if len(raw_bytes) != 32:
        print(f"Error: key is {len(raw_bytes)} bytes. Must be exactly 32.")
        sys.exit(1)
    b64key = urlsafe_b64encode(raw_bytes)
    return Fernet(b64key)

def encrypt_and_replace(cipher, filename):
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' not found.")
        return
    with open(filename, 'rb') as f:
        plaintext = f.read()
    token = cipher.encrypt(plaintext)
    out_name = filename + '.alex'
    with open(out_name, 'wb') as f:
        f.write(token)
    os.remove(filename)
    print(f"Encrypted '{filename}' → '{out_name}'")

def decrypt_and_replace(cipher, filename):
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' not found.")
        return
    if not filename.endswith('.alex'):
        print(f"Skipping '{filename}': not a .alex file.")
        return
    with open(filename, 'rb') as f:
        token = f.read()
    try:
        plaintext = cipher.decrypt(token)
    except Exception as e:
        print(f"Decryption failed for '{filename}': {e}")
        return
    out_name = filename[:-5]
    with open(out_name, 'wb') as f:
        f.write(plaintext)
    os.remove(filename)
    print(f"Decrypted '{filename}' → '{out_name}'")

def select_files(mode):
    root = tk.Tk()
    root.withdraw()
    if mode == 'encrypt':
        filetypes = [("All files", "*.*")]
    else:
        filetypes = [("Alex files", "*.alex")]
    paths = filedialog.askopenfilenames(
        title=f"Select files to {mode}",
        filetypes=filetypes
    )
    root.destroy()
    return list(paths)

def main():
    cipher = make_cipher(RAW_KEY)

    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    if mode not in ('encrypt', 'decrypt'):
        print("Invalid choice. Must be 'encrypt' or 'decrypt'.")
        sys.exit(1)

    files = select_files(mode)
    if not files:
        print("No files selected. Exiting.")
        sys.exit(0)

    for filepath in files:
        if mode == 'encrypt':
            encrypt_and_replace(cipher, filepath)
        else:
            decrypt_and_replace(cipher, filepath)

if __name__ == '__main__':
    main()
