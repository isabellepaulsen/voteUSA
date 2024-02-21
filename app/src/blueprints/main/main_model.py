import bcrypt
import mysql.connector
from src.config import db_config
from typing import Dict
from flask_login import UserMixin

def get_user_auth(email) -> Dict:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='get_user_auth', args=[email])
    try:
        results = [x.fetchall() for x in cursor.stored_results()][0][0]
        results =  {'user_id': results[0], 'email': email, 'password': results[1], 'salt': results[2], 'role':results[3]}
    except:
        results = {}
    finally: 
        cursor.close()
        connection.close()
        return results
        
# Inspriation from https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/ 
def hash_password(password : str, salt : str):
    """Hash password based on given salt

    Args:
        password (string): raw password in plaintext
        salt (string): salt to hash with

    Returns:
        string: hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))


def insert_user(name1, name2, name3, age, address1, address2, city, state, zip, ID1, ID2, email, password, role):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='insert_user', args=[name1, name2, name3, age, address1, address2, city, state, zip, ID1, ID2, email, hashed_pw, salt, role])
    #results = [x.fetchall() for x in cursor.stored_results()][0][0]
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    print(get_user_auth('et@e'))


class User(UserMixin):
    def __init__(self, email):
        self.email = email

