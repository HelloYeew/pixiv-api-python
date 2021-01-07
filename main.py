import sys
from check import *
# from for_dev import *
import getpass
import os

print("Booting program...")
print()

# check internet connection
print("Checking internet connection...")
connection = check_internet()
if connection == True:
    print("Connection complete!")
else:
    print("Connection failed! Please check your internet connection.")
    sys.exit()
print()

# check requirement
check_library()
print()
print("Checking directory...")
print(f"Current directory: {os.getcwd()}")
print()

# check login via token
# print("Checking login profile...")
# if check_token():
#     print("Token Available. Proceed to login")
# else:
#     print("No token available")

# menu function


# turn on and turn off dev mode here
dev = True

# login
from pixivapi import Client
client = Client()
while True:
    print("Welcome to Pixiv!")
    print("--Login--")
    username = input("Username : ")
    password = input("Password : ")
    try:
        client.login(username, password)
        print("Login Complete!")
        break
    except Exception as e:
        print(f"Error : {e}")

from function import *

# Main Menu
while True:
    print("What you want to do:")
    print("1.Fetch Illustration Detail")
    menu = input("Press number from menu to continue : ")
    if menu.isnumeric():
        menu = int(menu)
        if menu == 1:
            fetch_illus_information(client)
        else:
            print("Incorrect input")
            print()
    else:
        print("Incorrect input")
        print()



