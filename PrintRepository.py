import sqlite3
import os

import Record as Record

class PrintRepository:
    def __init__(self):
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
            CREATE TABLE IF NOT EXISTS generalrecords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,                
                employee_name TEXT,
                printerModel TEXT,
                color TEXT,
                quantity INTEGER,
                paper_size TEXT,
                paper_type TEXT,
                description TEXT,
                date TEXT,
                time TEXT,
                comments TEXT
                )
        ''')

        conn.commit()
        conn.close()



    def add_record(self, record):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO generalrecords (employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
                       (record.employee_name, record.printerModel, record.color, record.quantity, record.paper_size, record.paper_type, record.description, record.date, record.time, record.comments))

        conn.commit()
        conn.close()



    def delete_record(self, recordId):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        print(recordId)

        cursor.execute('DELETE FROM generalrecords WHERE id = ?', (recordId,))

        conn.commit()
        conn.close()
        print(recordId)
        
        
        
    def find_record(self, recordId):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        print(recordId)

        cursor.execute('SELECT * FROM generalrecords WHERE id = ?', (recordId,))
        data = cursor.fetchall()

        conn.commit()
        conn.close()
        print(recordId)
        
        return [Record.Record(id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments) 
                for id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments in data]




    def edit_record(self, record):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        print(record)

        cursor.execute('''
            UPDATE generalrecords SET
            employee_name = ?,
            printerModel = ?,
            color = ?,
            quantity = ?,
            paper_size = ?,
            paper_type = ?,
            description = ?,
            date = ?,
            time = ?,
            comments = ?
            WHERE id = ?
        ''', (
            record.employee_name, record.printerModel, record.color, record.quantity, 
            record.paper_size, record.paper_type, record.description, record.date, 
            record.time, record.comments, record.id
        ))

        conn.commit()
        conn.close()
        
        
        
    def get_all_records(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM generalrecords')
        data = cursor.fetchall()

        conn.close()
        print(data)

        return [Record.Record(id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments) 
                for id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments in data]

        
        
        
        
