import os
from configparser import ConfigParser

def get_db_connection():
    config = ConfigParser()
    config.read('config/config.ini')
    return {
        'host': config.get('database', 'host'),
        'user': config.get('database', 'user'),
        'password': config.get('database', 'password')
    }

def login(username, password):
    if username == os.getenv("APP_USERNAME") and password == os.getenv("APP_PASSWORD"):
        print("Login successful.")
    else:
        print("Login failed.")

if __name__ == "__main__":
    login("greenuser", "green123")
