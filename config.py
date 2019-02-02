import os

class Config():
    SECRET_KEY = os.environ.get('SEKRET_KEY') or 'you-will-never-guess-it'