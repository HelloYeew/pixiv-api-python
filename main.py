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
    print("1.Fetch Full Illustration Detail By ID")
    print("2.Fetch User Detail")
    print("3.Download all illustration from the artist")
    print("0.Exit")
    menu = input("Press number from menu to continue : ")
    if menu.isnumeric():
        menu = int(menu)
        if menu == 1:
            illustration_id = input("Illustration ID : ")
            fetch_illus_information(client, illustration_id)
        elif menu == 2:
            user_id = input("User ID : ")
            fetch_user_information(client, user_id)
        elif menu == 3:
            artist_id = input("Put an artist ID that you want to download : ")
            download_all_illustration(client, artist_id)
        elif menu == 0:
            print("Bye!")
            sys.exit()
        else:
            print("Incorrect input")
            print()
    else:
        print("Incorrect input")
        print()



