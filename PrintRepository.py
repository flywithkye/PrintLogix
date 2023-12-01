# Importing modules/libraries to communicate with a database using sql
import sqlite3
import os

# Import record class to create the records objects to contain each record's data
import Record as Record

# Class that allows for the adding, retrieval, removal and editng of the records in the system
class PrintRepository:
    # Class constructor for repository, initialzes path to database
    def __init__(self):
        # Storing referencing to when the database will be stored
        path = "database\\printlogix.db"

        # get the path to the directory this script is in
        scriptdir = os.path.dirname(__file__)
        # add the relative path to the database file from there
        self.db_path = os.path.join(scriptdir, path)
        # make sure the path exists and if not create it
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)                                                                                                                             


    # Method to create the table with desired fields for record storage if it does not exist yet 
    # using sql query commands
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


    # Method to add a given record's data to the database using sql query commands
    def add_record(self, record):
        # Connecting to the database at the given path
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO generalrecords (employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
                       (record.employee_name, record.printerModel, record.color, record.quantity, record.paper_size, record.paper_type, record.description, record.date, record.time, record.comments))

        conn.commit()
        conn.close()


    # Method to remove a record associated with the given record's id from the database using sql query commands
    def delete_record(self, recordId):
        # Connecting to the database at the given path
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        print(recordId)

        cursor.execute('DELETE FROM generalrecords WHERE id = ?', (recordId,))

        conn.commit()
        conn.close()
        print(recordId)
        
        
        
    # Method to retrieve data associated with a given record's id from the database using sql query commands
    def find_record(self, recordId):
        # Connecting to the database at the given path
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        print(recordId)

        cursor.execute('SELECT * FROM generalrecords WHERE id = ?', (recordId,))
        # Stores data retrieved from query
        data = cursor.fetchall()

        conn.commit()
        conn.close()
        print(recordId)
        
        return [Record.Record(id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments) 
                for id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments in data]



    # Method to update changes made to the given record's data in the database using sql query commands
    def edit_record(self, record):
        # Connecting to the database at the given path
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
        
        
        
    # Method to retrieve all records currently in the database using sql query commands
    def get_all_records(self):
        # Connecting to the database at the given path
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM generalrecords')
        # Stores data retrieved from query
        data = cursor.fetchall()

        conn.close()
        print(data)

        return [Record.Record(id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments) 
                for id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments in data]

        
        
        
        
