import os

DEBUG = 1

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'