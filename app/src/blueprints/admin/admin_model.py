import mysql.connector
from typing import List, Dict
from src.config import db_config
def get_test_table() -> List[Dict]:

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE Role="Admin"')
    results = cursor.fetchone()
    cursor.close()
    connection.close()

    return results