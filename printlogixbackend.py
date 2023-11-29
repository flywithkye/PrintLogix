import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class Record:
    def __init__(self, id, printerModel, employee_name, quantity, color, paper_size, date, time, paper_type, description, comments):
        self.id = id
        self.printerModel = printerModel
        self.employee_name = employee_name
        self.quantity = quantity
        self.color = color
        self.paper_size = paper_size
        self.date = date
        self.time = time
        self.paper_type = paper_type
        self.description = description
        self.comments = comments




class User:
    def __init__(self, name, username, password, role):
        self.name = name
        self.age = age


class PrintRepository:
    def __init__(self, db_path="C:/Users/TAREQUE ROBINSON/Desktop/AddRecord/printlogix.db"):
        self.db_path = db_path

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS genralrecords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                printerModel TEXT,
                employee_name INTEGER,
                quantity INTEGER,
                color TEXT,
                paper_size TEXT,
                date TEXT,
                time TEXT,
                paper_type TEXT,
                comments TEXT,
                description TEXT




            )
        ''')

        conn.commit()
        conn.close()

    def add_record(self, record):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO genralrecords (printerModel, employee_name, quantity, color, paper_size, comments, description, paper_type, date, time  ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (record.printerModel, record.employee_name, record.quantity, record.color, record.paper_size, record.comments, record.description, record.paper_type, record.date, record.time))

        conn.commit()
        conn.close()

    def delete_record(self, recordId):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        print(recordId)

        cursor.execute('DELETE FROM genralrecords WHERE id = ?', (recordId,))

        conn.commit()
        conn.close()
        print(recordId)



    def get_all_records(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM genralrecords')
        data = cursor.fetchall()

        conn.close()
        print(data)

        return [Record(id, printerModel, employee_name, quantity, color, paper_size, comments, description, paper_type, date, time) for id, printerModel, employee_name, quantity, color, paper_size, comments, description, paper_type, date, time in data]

class UserRepository:
    def __init__(self, db_path='printlogix.db'):
        self.db_path = db_path

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                password TEXT,
                role TEXT


            )
        ''')

        conn.commit()
        conn.close()

    def add_new_user(self, user):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (user.name, user.age))

        conn.commit()
        conn.close()

    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM records')
        data = cursor.fetchall()

        conn.close()

        return [Record(name, age) for _, name, age in data]


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Table Viewer")

        self.repository = PrintRepository()

        self.create_widgets()
        self.repository.create_table()

    def create_widgets(self):
        # Create and place the Treeview widget
        self.tree = ttk.Treeview(self.root, columns=('ID', 'PrinterModel', 'Employee' , 'quantity' , 'color', 'paper_size' , 'comments', 'description', 'paper_type', 'date', 'time', 'delete'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('PrinterModel', text='PrinterModel')
        self.tree.heading('Employee', text='Employee')
        self.tree.heading('quantity', text='quantity')
        self.tree.heading('color', text='color')
        self.tree.heading('paper_size', text='paper_size')
        self.tree.heading('comments', text='comments')
        self.tree.heading('description', text='description')
        self.tree.heading('paper_type', text='paper_type')
        self.tree.heading('date', text='date')
        self.tree.heading('time', text='time')
        self.tree.heading('delete', text='delete')




        self.tree.pack(padx=10, pady=10)

        # Create and place the button to display data
        display_button = tk.Button(self.root, text="Display Data", command=self.display_data)
        display_button.pack(pady=10)


        # Create and place entry fields
        # Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        # name_entry = Entry(root)
        # name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
        # age_entry = Entry(root)
        # age_entry.grid(row=1, column=1, padx=10, pady=10)


        # Create and place the entry fields for adding a record
        # self.Label(root, text="Name:")
        self.printer_model_entry = tk.Entry(self.root)
        self.printer_model_entry.pack(pady=5)
        
        self.employee_name_entry = tk.Entry(self.root)
        self.employee_name_entry.pack(pady=5)

        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(pady=5)

        self.color_entry = tk.Entry(self.root)
        self.color_entry.pack(pady=5)

        self.paper_size_entry = tk.Entry(self.root)
        self.paper_size_entry.pack(pady=5)

        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack(pady=5)

        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=5)

        self.paper_type_entry = tk.Entry(self.root)
        self.paper_type_entry.pack(pady=5)

        self.comments_entry = tk.Entry(self.root)
        self.comments_entry.pack(pady=5)

        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack(pady=5)

        # Create and place the button to add a record
        add_button = tk.Button(self.root, text="Add Record", command=self.add_record)
        add_button.pack(pady=10)

                # Create and place the button to add a record
        delete_button = tk.Button(self.root, text="Delete Record", command=self.delete_record)
        delete_button.pack(pady=10)


    def display_data(self):
        # Clear the existing table content
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Populate the table with retrieved data
        records = self.repository.get_all_records()
        for record in records:
            delete_button = tk.Button(self.root, text="Delete", command=lambda r=record.id: self.delete_record(r))
            self.tree.insert('', 'end', values=(record.id, record.printerModel, record.employee_name, record.quantity, record.color, record.paper_size, record.comments, record.description, record.paper_type, record.date, record.time))

    def add_record(self):
        printer_model = self.printer_model_entry.get()
        employee_name = self.employee_name_entry.get()
        quantity = self.quantity_entry.get()
        color = self.color_entry.get()
        paper_size = self.paper_size_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        paper_type = self.paper_type_entry.get()
        comments = self.comments_entry.get()
        description = self.description_entry.get()

        # if not name or not age:
        #     messagebox.showerror("Error", "Please fill in all fields.")
        #     return

        # try:
        #     age = int(age)
        # except ValueError:
        #     messagebox.showerror("Error", "Age must be a valid integer.")
        #     return
        # self, id ,  printerModel, employee_name, quantity, color, paper_size

        record = Record(
            id=123,
            printerModel=printer_model,
            employee_name=employee_name,
            quantity=quantity,
            color=color,
            paper_size=paper_size,
            date=date,
            time=time,
            paper_type=paper_type,
            comments=comments,
            description=description
            )

        self.repository.add_record(record)

        # # Clear the entry fields
        # self.name_entry.delete(0, tk.END)
        # self.age_entry.delete(0, tk.END)

        # Show a success message
        messagebox.showinfo("Success", "Record added successfully.")

    def delete_record(self):
        result = messagebox.askquestion("Delete Record", "Are you sure you want to delete this record?")
        if result == 'yes':
            self.repository.delete_record(13)
            self.display_data()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
