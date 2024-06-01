from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.txt", "rb") as key_file:
        key = key_file.read()
    return key

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                try:
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password:", decrypted_pass)
                except Exception as e:
                    print(f"Failed to decrypt password for user {user}: {e}")
    except FileNotFoundError:
        print("Password file not found.")

def add():
    name = input("Account name: ")
    pwd = input("Input password: ")

    with open('passwords.txt', 'a') as f:
        encrypted_pass = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pass + "\n")

# Ensure key.txt exists and contains a key
if not os.path.exists("key.txt"):
    write_key()

key = load_key()
fer = Fernet(key)

while True:
    mode = input("Would you like to view or add your passwords? \nType 'add' or 'view'\nIf you would like to quit type 'q': ").lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid input")
