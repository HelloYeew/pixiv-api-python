import subprocess
import sys
import urllib.request
import os

def check_library():
    print("Start checking important library to run a program...")

    # check pixiv api
    print("Checking Pixiv API...")
    try:
        import pixivapi
    except ImportError:
        print("Google API Python Client not found.")
        print("Run install command : pip install pixiv-api")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pixiv-api'])
        print("Pixiv API install complete!")
    finally:
        import pixivapi

    # check tqdm
    print("Checking tqdm...")
    try:
        import tqdm
    except ImportError:
        print("tqdm not found.")
        print("Run install command : -m pip install tqdm")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'tqdm'])
        print("tqdm install complete!")
    finally:
        import tqdm


def check_internet(url='http://www.google.com', timeout=3):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False


def check_token():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.pickle'):
                return True
