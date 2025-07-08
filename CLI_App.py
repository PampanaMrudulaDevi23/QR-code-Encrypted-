import os
import sys
import datetime
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
NOTES_FILE = "notes.enc"

# Generate or load encryption key
def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return key

# Encrypt and save a note
def write_note():
    note = input("Write your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_note = f"[{timestamp}]\n{note}\n\n"
    encrypted_note = fernet.encrypt(full_note.encode())

    with open(NOTES_FILE, 'ab') as file:
        file.write(encrypted_note + b'\n')

    print("Note saved securely.")

# Read and decrypt all notes
def read_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return

    with open(NOTES_FILE, 'rb') as file:
        for line in file:
            try:
                decrypted = fernet.decrypt(line.strip())
                print(decrypted.decode())
            except Exception as e:
                print("Failed to decrypt a note:", e)

# Main CLI loop
def main():
    while True:
        print("\nEncrypted Notes App")
        print("1. Write a note")
        print("2. Read notes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            write_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    key = load_or_create_key()
    fernet = Fernet(key)
    main()
