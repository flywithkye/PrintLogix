import sqlite3
import os

import User as User

class UserRepository:
    def __init__(self):
         # Storing referencing to when the database will be stored
        path = "database\\printlogix.db"

        # get the path to the directory this script is in
        scriptdir = os.path.dirname(__file__)
        # add the relative path to the database file from there
        self.db_path = os.path.join(scriptdir, path)
        # make sure the path exists and if not create it
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)


    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                username TEXT,
                password TEXT,
                role TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def add_new_user(self, user):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (name, username, password, role) VALUES (?, ?, ?, ?)', 
                       (user.name, user.username, user.password, user.role))

        conn.commit()
        conn.close()

    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users')
        data = cursor.fetchall()

        conn.close()

        return [User.User(id, name, username, password, role) for id,  name, username, password, role in data]