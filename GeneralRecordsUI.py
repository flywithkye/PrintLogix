import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg
from PIL import ImageTk
from tkinter import messagebox as mgbx
from datetime import datetime as dt
import re

import PrintRepository as prtrepo
import Record as Record

class GeneralRecordsUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.box = None
                
        # Initializing Print Repository
        self.printrepository = prtrepo.PrintRepository()
        self.printrepository.create_table()
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        error_red = "#FF0000"
        white = "#ffffff"        
        gray = "#F0F0F0"
        black = "#000000"
        
        self.main_view = tk.Frame(self, bg=white)
        self.main_view.pack(side="left", fill="both", expand=True)
        self.title_frame = tk.Frame(master=self.main_view, bg=white)
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(24, 0))

        self.genTitleLbl = ctk.CTkLabel(master=self.title_frame, width=50, text="General Print Records - Administrator - admin1234", fg_color=white, font=("Arial Black", 24), text_color=dark_green)
        self.genTitleLbl.pack(anchor="n")    
              
        self.search_container = tk.Frame(master=self.main_view, height=50, bg=gray)
        self.search_container.pack(fill="x", pady=(19, 0), padx=32)    
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white
        self.SortBox = ctk.CTkComboBox(master=self.search_container, width=140, state="readonly", values=["Sort By", "Record ID", "Date Ascending", "Date Descending"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.SortBox.pack(side="right", padx=(16, 15), pady=15)
        self.SortBox.set("Sort By")
        
        self.SearchEntry = ctk.CTkEntry(master=self.search_container, width=305, placeholder_text="Search Records", border_color="#2A8C55", border_width=2)
        self.SearchEntry.pack(side="right", padx=(13, 0), pady=15)
            
        self.buttons_frame = tk.Frame(master=self.search_container, bg=gray)
        self.buttons_frame.grid_propagate(0)
        self.buttons_frame.pack(side="left")
        
        self.addRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Add Record",  command=lambda: self.OpenButtonWindow(NewRecord(self.printrepository)), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.addRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
        
        self.editRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Edit Record", command=lambda: self.OpenButtonWindow(EditRecord(self.printrepository)), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.editRecsBtn.pack(anchor="se", side="left", padx=(21, 0))
                
        self.exportRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Export Records", command=lambda: self.OpenButtonWindow(ExportGRecords()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
        self.exportRecsBtn.pack(anchor="se", side="left", padx=(21, 0))
                 
        self.columns = ["Record ID", "Employee Name", "Printer Model", "Colored / B&W", "Quantity", "Page Size", "Page Type", "Description", "Date", "Time", "Comments"]
        self.table_data = [
            self.columns,        
        ] 

        self.table_frame = CTkXYFrame(master=self.main_view, width=1100, height=650, fg_color="#fff")
        self.table_frame.pack(expand=True, fill="both", padx=(25, 18), pady=20)
        self.table_frame.pack(anchor="w", side="left")
        self.table = ctkt(master=self.table_frame, values=self.table_data, row=30, corner_radius=6, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
        self.table.edit_row(0, text_color=white, hover_color="#2A8C55")
        self.table.pack()
        self.table.pack(anchor="w", side="left")
        
        self.UpdateTable()
    
        
    def UpdateTable(self):
        self.table.update_values(values=self.columns)
        self.table_data = []
        self.table_data.append(self.columns)
        
        records = self.printrepository.get_all_records()        
        for record in records:
            self.table_data.append([record.id, record.employee_name, record.printerModel, record.color, record.quantity,  record.paper_size, record.paper_type, record.description, record.date, record.time, record.comments])

        self.table.update_values(values=self.table_data)
       
       
        
    def OpenButtonWindow(self, classtype):
        if self.box != None:                
            if self.box.window.winfo_exists() != True:                      
                # show Toplevel
                self.box = classtype
                    
                # set it modal (to wait for value)
                self.box.window.focus_force()
                #self.box.window.focus_set()   # take over input focus,
                self.box.window.grab_set()    # disable other windows while I'm open,
                self.box.window.wait_window() # and wait here until win destroyed
        else:
            # show Toplevel
            self.box = classtype
                
            # set it modal (to wait for value)
            self.box.window.focus_force()
            #self.box.window.focus_set()   # take over input focus,
            self.box.window.grab_set()    # disable other windows while I'm open,
            self.box.window.wait_window() # and wait here until win destroyed

            # get value from Toplevel
            """print(type(self.box.entry_value))
            self.SearchEntry.delete(0 ,'end')
            self.SearchEntry.insert(0, self.box.entry_value)"""
            
        self.UpdateTable()
            
            
             
        

class NewRecord:
    entry_value = '' # ignore this
    
    def __init__(self, printrepository):
        # Storing repository
        self.repo = printrepository
        
        # Storing images
        icon_img = "images\\logo.ico"
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        white = "#ffffff"        
        gray = "#F0F0F0"
        black = "#000000"
        
        self.window = tk.Toplevel()
        self.window.iconbitmap(icon_img)      
        self.window.wm_title("Add New Record")
   
        window_height = 580
        window_width = 385
        screen_width = self.window.winfo_screenwidth()
        #screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = 35
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            
        self.window.resizable(False,False)        
        
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white
        
        """self.recordidframe = tk.Frame(self.window)
        self.recordidframe.pack(anchor='center', side='top', pady=10)
        self.label = tk.Label(self.recordidframe, text='Record ID: ', font=("Arial Black", 12), fg="#2A8C55")
        self.label.pack(side="left")      
        self.idinfolbl = tk.Label(self.recordidframe, font=("Arial", 12))
        self.idinfolbl.pack(side="left") 
        self.idinfolbl.configure(text= "#" + str(51)) """
        
        self.employeeframe = tk.Frame(self.window, width=80)
        self.employeeframe.pack(anchor='nw', side='top', pady=(20,10))
        self.label = tk.Label(self.employeeframe, text='Employee: ')
        self.label.pack(side="left", padx=15)        
        self.EmployeeBox = ctk.CTkComboBox(self.employeeframe, width=150, state="readonly", values=["Select Employee", "Jane Doe", "Jamie Dodger", "James Potter"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.EmployeeBox.pack(side="right")
        self.EmployeeBox.set("Select Employee")
        
        self.printerframe = tk.Frame(self.window, width=80)
        self.printerframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.printerframe, text='Printer Model: ')
        self.label.pack(side="left", padx=15)        
        self.PrintModelBox = ctk.CTkComboBox(self.printerframe, width=150, state="readonly", values=["Select Model", "Xerox C70", "Sharp MXM 456"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PrintModelBox.pack(side="right")
        self.PrintModelBox.set("Select Model")
        
        self.radiobuttonsframe = tk.Frame(self.window, width=80)
        self.radiobuttonsframe.pack(anchor='nw', side='top', pady=10)
        self.radio_var = tk.StringVar()
        self.coloredbtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Colored", variable=self.radio_var, value="Colored")
        self.coloredbtn.pack(side="left", padx=(25, 10))
        self.blackwhitebtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Black & White", variable=self.radio_var, value="Black & White")
        self.blackwhitebtn.pack(side="left")
        
        self.pagesframe = tk.Frame(self.window, width=80)
        self.pagesframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagesframe, text='Quantity: ')
        self.label.pack(side="left", padx=15)      
        self.pagesentry = ctk.CTkEntry(master=self.pagesframe, width=50, border_color="#2A8C55", border_width=2)
        self.pagesentry.pack(side="right", padx=18)
        
        self.pagesizeframe = tk.Frame(self.window, width=80)
        self.pagesizeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagesizeframe, text='Page Size: ')
        self.label.pack(side="left", padx=15)        
        self.PageSizeBox = ctk.CTkComboBox(self.pagesizeframe, width=150, state="readonly", values=["Select Paper Size", "Legal", "Letter", "Tabloid", "A4"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageSizeBox.pack(side="right", padx=11)
        self.PageSizeBox.set("Select Paper Size")
        
        self.pagetypeframe = tk.Frame(self.window, width=80)
        self.pagetypeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagetypeframe, text='Page Type: ')
        self.label.pack(side="left", padx=15)        
        self.PageTypeBox = ctk.CTkComboBox(self.pagetypeframe, width=150, state="readonly", values=["Select Paper Type", "Standard Paper", "Cougar Card", "Glossy Card", "Matte Card", "Linen Card", "Parchment Card"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageTypeBox.pack(side="right", padx=6)
        self.PageTypeBox.set("Select Paper Type")        
        
        self.descriptionframe = tk.Frame(self.window, width=80)
        self.descriptionframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.descriptionframe, text='Description: ')
        self.label.pack(side="left", padx=15)        
        self.DescrBox = ctk.CTkComboBox(self.descriptionframe, width=150, state="readonly", values=["Select an Option", "Internal", "External"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.DescrBox.pack(side="right")
        self.DescrBox.set("Select an Option")
        
        
        self.datetimeframe = tk.Frame(self.window, width=80)
        self.datetimeframe.pack(anchor='nw', side='top', pady=12)
        self.label = tk.Label(self.datetimeframe, text='Date:')
        self.label.pack(side="left", padx=(15,10))      
        self.dateentry = ctk.CTkEntry(master=self.datetimeframe, width=83, border_color="#2A8C55", border_width=2)
        self.dateentry.pack(side="left")
        time = dt.now()
        datestamp = time.strftime('%d/%m/%Y')        
        self.dateentry.insert(0, datestamp)
        
        self.label = tk.Label(self.datetimeframe, text='Time:')
        self.label.pack(side="left", padx=(18,10))      
        self.hrsentry = ctk.CTkEntry(master=self.datetimeframe, width=29, border_color="#2A8C55", border_width=2)
        self.hrsentry.pack(side="left")        
        hours = time.strftime('%I')
        self.hrsentry.insert(0, hours)
        self.label = tk.Label(self.datetimeframe, text=':', font=("Arial Bold", 12))
        self.label.pack(side="left", padx=1)      
        self.minsentry = ctk.CTkEntry(master=self.datetimeframe, width=29, border_color="#2A8C55", border_width=2)
        self.minsentry.pack(side="left")        
        mins = time.strftime('%M')
        self.minsentry.insert(0, mins)       
        self.PMBox = ctk.CTkComboBox(self.datetimeframe, width=59, state="readonly", values=["AM", "PM"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PMBox.pack(side="left", padx=8)
        pm = time.strftime('%p')
        self.PMBox.set(pm)
        
        
        self.commentsframe = tk.Frame(self.window)
        self.commentsframe.pack(anchor='nw', side='top', padx=15, pady=(13,5))
        self.label = tk.Label(self.commentsframe, text='Comments: ')
        self.label.pack(anchor='nw', side="top", pady=(0,5))   
        self.commentsbox = ctk.CTkTextbox(self.commentsframe, width=350, height=60, border_color="#2A8C55", border_width=2)  
        self.commentsbox.pack(anchor='nw', side="bottom", padx=3)      
        
        
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=20)
        self.addrecbtn = ctk.CTkButton(self.buttonframe, text="Create", command=self.AddNewRecord, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.addrecbtn.pack(side='left', padx=15)
        self.cancelbtn = ctk.CTkButton(self.buttonframe, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=15)
        
        

        """self.frame = ttk.Frame(self.window)
        self.frame.pack(side='bottom')
        
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(side='left')

        self.button = ttk.Button(self.frame, text="Ok", command=self.name_input_box_exit)
        self.button.pack(side='left')"""

    def window_exit(self):
        # get value from widget and assign to variable        
        """self.entry_value = self.entry.get()
        print(self.entry_value)"""

        self.window.destroy()    
        
    def AddNewRecord(self):        
        #Error checking first here        
        valid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        errorLst = []
        
        self.employee_name = self.EmployeeBox.get()
        if self.employee_name != "Select Employee":
            valid[0] = 1
        else:
            errorLst.append("- Please Choose an Employee.")
        
        self.printer_model = self.PrintModelBox.get()
        if self.printer_model != "Select Model":
            valid[1] = 1
        else:
            errorLst.append("- Please Choose a Model.")
            
        self.color = self.radio_var.get()
        if self.color != "":
            valid[2] = 1
        else:
            errorLst.append("- Please Choose a Color Type.")
        
        self.quantity = self.pagesentry.get()
        if self.quantity.isdigit() != False:
            if int(self.quantity) > 0:
                valid[3] = 1
            else:
                errorLst.append("- Invalid number of Pages.")
        else:
            errorLst.append("- Invalid number of Pages.")
        
        self.paper_size = self.PageSizeBox.get()
        if self.paper_size != "Select Paper Size":
            valid[4] = 1
        else:
            errorLst.append("- Please Select a Paper Size.")
            
        self.paper_type = self.PageTypeBox.get()
        if self.paper_type != "Select Paper Type":
            valid[5] = 1
        else:
            errorLst.append("- Please Select a Paper Type.")
            
        self.description = self.DescrBox.get()
        if self.description != "Select an Option":
            valid[6] = 1
        else:
            errorLst.append("- Please Pick a Description.")
            
        self.date = self.dateentry.get()    
        format = "%d/%m/%Y"         
        # checking if format matches the date 
        res = True        
        # using try-except to check for truth value
        try:
            res = bool(dt.strptime(self.date, format))
            valid[7] = 1
        except ValueError:            
            errorLst.append("- Invalid date. Must be DD/MM/YYYY.")
        
        self.time = self.hrsentry.get() + ":" + self.minsentry.get() + " " + self.PMBox.get()
        try:
            if int(self.hrsentry.get()) <= 12 and int(self.hrsentry.get()) > 0 and self.hrsentry.get().isdigit() != False:
                valid[8] = 1
            if int(self.minsentry.get()) <= 59 and self.minsentry.get().isdigit() != False:
                valid[9] = 1
        except ValueError:     
            errorLst.append("- Invalid time. Must be in format (12hr)HH:MM PM/AM.")
        if valid[8] == 0 or valid[9] == 0:
            if errorLst[len(errorLst)-1] != "- Invalid time. Must be in format (12hr)HH:MM PM/AM.":
                errorLst.append("- Invalid time. Must be in format (12hr)HH:MM PM/AM.")
            
        self.comments = self.commentsbox.get("1.0", 'end-1c')
        
        if valid == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:        
            self.new_record = Record.Record(
                id = 1,
                employee_name = self.employee_name,
                printerModel = self.printer_model,
                color = self.color,
                quantity = self.quantity,
                paper_size = self.paper_size,
                paper_type = self.paper_type,
                description = self.description,
                date = self.date,
                time = self.time,
                comments = self.comments
            )
            
            print(f'[{self.new_record.employee_name}, {self.new_record.printerModel}, {self.new_record.color}, {self.new_record.quantity}, {self.new_record.paper_size}, {self.new_record.paper_type}, {self.new_record.description}, {self.new_record.date}, {self.new_record.time}, {self.new_record.comments}]')
            
            self.repo.add_record(self.new_record)        
            
            self.window_exit()        
            mgbx.showinfo("Success", "Record created successfully.")
        
        else:
            mgbx.showerror('Error', 'Error with Input.\nPlease address the following:\n' + "\n".join(errorLst))
        
        
 
        
class EditRecord:
    def __init__(self, printrepository):
        # Storing repository
        self.repo = printrepository
        self.time = ''       
        
        # Storing images
        icon_img = "images\\logo.ico"
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        white = "#ffffff"        
        gray = "#F0F0F0"
        black = "#000000"
        
        self.window = tk.Toplevel()
        self.window.iconbitmap(icon_img)      
        self.window.wm_title("Edit Record")        
        
        window_height = 620
        window_width = 385
        screen_width = self.window.winfo_screenwidth()
        #screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = 35
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            
        self.window.resizable(False,False) 
        
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white
        
        self.recordidframe = tk.Frame(self.window)
        self.recordidframe.pack(anchor='nw', side='top', pady=15)
        self.label = tk.Label(self.recordidframe, text='Enter Record ID#:', font=("Arial Black", 11), fg="#2A8C55")
        self.label.pack(side="left", padx=(20,12))
        self.idinfoentry = ctk.CTkEntry(master=self.recordidframe, width=60, border_color="#2A8C55", border_width=2)
        self.idinfoentry.pack(side="left") 
        self.findbtn = ctk.CTkButton(self.recordidframe, text="Find", command=self.FindRecord, width=69, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.findbtn.pack(side='left', padx=15)           
                
        self.employeeframe = tk.Frame(self.window, width=80)
        self.employeeframe.pack(anchor='nw', side='top', pady=(20,10))
        self.label = tk.Label(self.employeeframe, text='Employee: ')
        self.label.pack(side="left", padx=15)        
        self.EmployeeBox = ctk.CTkComboBox(self.employeeframe, width=150, state="readonly", values=["Select Employee", "Jane Doe", "Jamie Dodger", "James Potter"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.EmployeeBox.pack(side="right")
        self.EmployeeBox.set("Select Employee")
        
        self.printerframe = tk.Frame(self.window, width=80)
        self.printerframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.printerframe, text='Printer Model: ')
        self.label.pack(side="left", padx=15)        
        self.PrintModelBox = ctk.CTkComboBox(self.printerframe, width=150, state="readonly", values=["Select Model", "Xerox C70", "Sharp MXM 456"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PrintModelBox.pack(side="right")
        self.PrintModelBox.set("Select Model")
        
        self.radiobuttonsframe = tk.Frame(self.window, width=80)
        self.radiobuttonsframe.pack(anchor='nw', side='top', pady=10)
        self.radio_var = tk.StringVar()
        self.coloredbtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Colored", variable=self.radio_var, value="Colored")
        self.coloredbtn.pack(side="left", padx=(25, 10))
        self.blackwhitebtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Black & White", variable=self.radio_var, value="Black & White")
        self.blackwhitebtn.pack(side="left")
        
        self.pagesframe = tk.Frame(self.window, width=80)
        self.pagesframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagesframe, text='Quantity: ')
        self.label.pack(side="left", padx=15)      
        self.pagesentry = ctk.CTkEntry(master=self.pagesframe, width=50, border_color="#2A8C55", border_width=2)
        self.pagesentry.pack(side="right", padx=18)
        
        self.pagesizeframe = tk.Frame(self.window, width=80)
        self.pagesizeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagesizeframe, text='Page Size: ')
        self.label.pack(side="left", padx=15)        
        self.PageSizeBox = ctk.CTkComboBox(self.pagesizeframe, width=150, state="readonly", values=["Select Paper Size", "Legal", "Letter", "Tabloid", "A4"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageSizeBox.pack(side="right", padx=11)
        self.PageSizeBox.set("Select Paper Size")
        
        self.pagetypeframe = tk.Frame(self.window, width=80)
        self.pagetypeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagetypeframe, text='Page Type: ')
        self.label.pack(side="left", padx=15)        
        self.PageTypeBox = ctk.CTkComboBox(self.pagetypeframe, width=150, state="readonly", values=["Select Paper Type", "Standard Paper", "Cougar Card", "Glossy Card", "Matte Card", "Linen Card", "Parchment Card"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageTypeBox.pack(side="right", padx=6)
        self.PageTypeBox.set("Select Paper Type")        
        
        self.descriptionframe = tk.Frame(self.window, width=80)
        self.descriptionframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.descriptionframe, text='Description: ')
        self.label.pack(side="left", padx=15)        
        self.DescrBox = ctk.CTkComboBox(self.descriptionframe, width=150, state="readonly", values=["Select an Option", "Internal", "External"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.DescrBox.pack(side="right")
        self.DescrBox.set("Select an Option")
        
        self.datetimeframe = tk.Frame(self.window, width=80)
        self.datetimeframe.pack(anchor='nw', side='top', pady=12)
        self.label = tk.Label(self.datetimeframe, text='Date:')
        self.label.pack(side="left", padx=(15,10))      
        self.dateentry = ctk.CTkEntry(master=self.datetimeframe, width=83, border_color="#2A8C55", border_width=2)
        self.dateentry.pack(side="left")
        
        self.label = tk.Label(self.datetimeframe, text='Time:')
        self.label.pack(side="left", padx=(18,10))      
        self.hrsentry = ctk.CTkEntry(master=self.datetimeframe, width=29, border_color="#2A8C55", border_width=2)
        self.hrsentry.pack(side="left")        
        self.label = tk.Label(self.datetimeframe, text=':', font=("Arial Bold", 12))
        self.label.pack(side="left", padx=1)      
        self.minsentry = ctk.CTkEntry(master=self.datetimeframe, width=29, border_color="#2A8C55", border_width=2)
        self.minsentry.pack(side="left")             
        self.PMBox = ctk.CTkComboBox(self.datetimeframe, width=59, state="readonly", values=["AM", "PM"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PMBox.pack(side="left", padx=8)

        
        
        self.commentsframe = tk.Frame(self.window)
        self.commentsframe.pack(anchor='nw', side='top', padx=15, pady=(13,5))
        self.label = tk.Label(self.commentsframe, text='Comments: ')
        self.label.pack(anchor='nw', side="top", pady=(0,5))   
        self.commentsbox = ctk.CTkTextbox(self.commentsframe, width=350, height=60, border_color="#2A8C55", border_width=2)  
        self.commentsbox.pack(anchor='nw', side="bottom", padx=3)          
        
        
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=18)
        self.saverecbtn = ctk.CTkButton(self.buttonframe, text="Save", state="disabled", command=self.SaveRecordChanges, font=("Arial Bold", 15), height=27, width=100, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.saverecbtn.pack(side='left', padx=(18,0))
        self.deleterecbtn = ctk.CTkButton(self.buttonframe, state="disabled", text="Delete", command=self.RemoveRecord, font=("Arial Bold", 15), height=27, width=105, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.deleterecbtn.pack(side='left', padx=18)  
        self.cancelbtn = ctk.CTkButton(self.buttonframe, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, width=100, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=(0,18))


    def window_exit(self):
        self.window.destroy()  
        
        
    def FindRecord(self):
        #Error checking on entry field
        if self.idinfoentry.get().isdigit() != False:
            self.recordLst = self.repo.find_record(self.idinfoentry.get())
            if len(self.recordLst) < 1:
                mgbx.showerror('Error', 'Error: Record not Found.')

            else:
                self.saverecbtn.configure(state="normal")
                self.deleterecbtn.configure(state="normal")
                
                self.record = self.recordLst[0]
                mgbx.showinfo("Success", "Record Found.")
            
                self.EmployeeBox.set(self.record.employee_name)
                self.PrintModelBox.set(self.record.printerModel)

                if self.record.color == "Black & White":
                    self.coloredbtn.selection_clear()
                    self.blackwhitebtn.select()
                else:
                    self.blackwhitebtn.selection_clear()
                    self.coloredbtn.select()
                    
                self.pagesentry.delete(0 ,'end')
                self.pagesentry.insert(0, self.record.quantity)
                self.PageSizeBox.set(self.record.paper_size)
                self.PageTypeBox.set(self.record.paper_type)
                self.DescrBox.set(self.record.description)
                self.dateentry.delete(0 ,'end')
                self.dateentry.insert(0, self.record.date)
                self.time = re.split(':| ', self.record.time)
                self.hrsentry.delete(0 ,'end')
                self.hrsentry.insert(0, self.time[0]) 
                self.minsentry.delete(0 ,'end')
                self.minsentry.insert(0, self.time[1])
                self.PMBox.set(self.time[2])
                self.commentsbox.delete(1.0,'end')
                self.commentsbox.insert(1.0, self.record.comments)
            
        else:
            mgbx.showerror('Error', 'Error: Invalid or Empty Record ID.')        


        
    def RemoveRecord(self):
        #Error checking first here
        
        result = mgbx.askquestion("Confirm", "Delete Record #" + self.idinfoentry.get() + "? This cannot be undone.")
        if result == 'yes':
            self.repo.delete_record(self.idinfoentry.get()) 
            self.window_exit()        
            mgbx.showinfo("Success", "Record deleted successfully.")

    
    
    def SaveRecordChanges(self):    
        #Error checking first here        
        valid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        errorLst = []
        
        self.employee_name = self.EmployeeBox.get()
        if self.employee_name != "Select Employee":
            valid[0] = 1
        else:
            errorLst.append("- Please Choose an Employee.")
        
        self.printer_model = self.PrintModelBox.get()
        if self.printer_model != "Select Model":
            valid[1] = 1
        else:
            errorLst.append("- Please Choose a Model.")
            
        self.color = self.radio_var.get()
        if self.color != "":
            valid[2] = 1
        else:
            errorLst.append("- Please Choose a Color Type.")
        
        self.quantity = self.pagesentry.get()
        if self.quantity.isdigit() != False:
            if int(self.quantity) > 0:
                valid[3] = 1
            else:
                errorLst.append("- Invalid number of Pages.")
        else:
            errorLst.append("- Invalid number of Pages.")
        
        self.paper_size = self.PageSizeBox.get()
        if self.paper_size != "Select Paper Size":
            valid[4] = 1
        else:
            errorLst.append("- Please Select a Paper Size.")
            
        self.paper_type = self.PageTypeBox.get()
        if self.paper_type != "Select Paper Type":
            valid[5] = 1
        else:
            errorLst.append("- Please Select a Paper Type.")
            
        self.description = self.DescrBox.get()
        if self.description != "Select an Option":
            valid[6] = 1
        else:
            errorLst.append("- Please Pick a Description.")
            
        self.date = self.dateentry.get()    
        format = "%d/%m/%Y"         
        # checking if format matches the date 
        res = True        
        # using try-except to check for truth value
        try:
            res = bool(dt.strptime(self.date, format))
            valid[7] = 1
        except ValueError:            
            errorLst.append("- Invalid date. Must be DD/MM/YYYY.")
        
        self.time = self.hrsentry.get() + ":" + self.minsentry.get() + " " + self.PMBox.get()
        try:
            if int(self.hrsentry.get()) <= 12 and int(self.hrsentry.get()) > 0 and self.hrsentry.get().isdigit() != False:
                valid[8] = 1
            if int(self.minsentry.get()) <= 59 and self.minsentry.get().isdigit() != False:
                valid[9] = 1
        except ValueError:     
            errorLst.append("- Invalid time. Must be in format (12hr)HH:MM PM/AM.")
        if valid[8] == 0 or valid[9] == 0:
            if errorLst[len(errorLst)-1] != "- Invalid time. Must be in format (12hr)HH:MM PM/AM.":
                errorLst.append("- Invalid time. Must be in format (12hr)HH:MM PM/AM.")
            
        self.comments = self.commentsbox.get("1.0", 'end-1c')
        
        if valid == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:          
            result = mgbx.askquestion("Confirm", "Save Changes?")
            if result == 'yes':        
                self.record = Record.Record(
                    id = self.record.id,
                    employee_name = self.employee_name,
                    printerModel = self.printer_model,
                    color = self.color,
                    quantity = self.quantity,
                    paper_size = self.paper_size,
                    paper_type = self.paper_type,
                    description = self.description,
                    date = self.date,
                    time = self.time,
                    comments = self.comments
                )
                
                print(f'[{self.record.employee_name}, {self.record.printerModel}, {self.record.color}, {self.record.quantity}, {self.record.paper_size}, {self.record.paper_type}, {self.record.description}, {self.record.date}, {self.record.time}, {self.record.comments}]')
                
                self.repo.edit_record(self.record)        
                
                self.window_exit()        
                mgbx.showinfo("Success", "Record updated successfully.")
        else:
            mgbx.showerror('Error', 'Error with Input.\nPlease address the following:\n' + "\n".join(errorLst))
        
        
        
class ExportGRecords:
    def __init__(self):
        # Storing images
        icon_img = "images\\logo.ico"
        folder_img_data = pImg.open("images\\folder_icon.png")
        folder_img_data = folder_img_data.resize((21, 21))
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        white = "#ffffff"        
        gray = "#F0F0F0"
        black = "#000000"
        
        self.window = tk.Toplevel()
        self.window.iconbitmap(icon_img)      
        self.window.wm_title("Export General Records")       
        
        window_height = 150
        window_width = 385
        screen_width = self.window.winfo_screenwidth()
        #screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = 110
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            
        self.window.resizable(False,False) 
        
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white       
        
        self.linkframe = tk.Frame(self.window)
        self.linkframe.pack(anchor='nw', side='top', padx=15, pady=(17,0))
        self.label = tk.Label(self.linkframe, text='Select Output Directory & File Name: ')
        self.label.pack(anchor='nw', side="top", pady=(0,3))   
        self.innerframe = tk.Frame(self.linkframe)
        self.innerframe.pack(anchor='nw', side="bottom")
        self.linkentry = ctk.CTkEntry(master=self.innerframe, width=299, border_color="#2A8C55", border_width=2)
        self.linkentry.pack(side="left", padx=(3,10))
        folder_img = ImageTk.PhotoImage(image=folder_img_data)
        self.folderBtn = ctk.CTkButton(master=self.innerframe, command=self.OpenFileExplorer, width=40, image=folder_img, text="", text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.folderBtn.pack(side="right")
        
        
        
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=(0,23))
        self.exportbtn = ctk.CTkButton(self.buttonframe, width=170, text="Export To Excel", command=self.StartExport, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.exportbtn.pack(side='left', padx=15)
        self.cancelbtn = ctk.CTkButton(self.buttonframe, width=110, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=15)
              

    def window_exit(self):
        self.window.destroy()  
        
    def OpenFileExplorer(self):
        pass
    
    def StartExport(self):
        pass