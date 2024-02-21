import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '3306',
    'database': 'voterdb'
}



class Config:
    SECRET_KEY = os.urandom(32)
    DEBUG = True
