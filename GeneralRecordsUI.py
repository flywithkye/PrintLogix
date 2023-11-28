import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg
from PIL import ImageTk

from tkinter import ttk
from datetime import datetime as dt


class GeneralRecordsUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.box = None
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
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
        self.filterBox = ctk.CTkComboBox(master=self.search_container, width=125, values=["Filter", "Internal Print", "Employee"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.filterBox.pack(side="right", padx=(16, 15), pady=15)
        self.SortBox = ctk.CTkComboBox(master=self.search_container, width=125, values=["Sort By", "Record ID", "Date Ascending", "Date Descending"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.SortBox.pack(side="right", padx=(16, 0), pady=15)
        
        self.SearchEntry = ctk.CTkEntry(master=self.search_container, width=305, placeholder_text="Search Records", border_color="#2A8C55", border_width=2)
        self.SearchEntry.pack(side="right", padx=(13, 0), pady=15)
            
        self.buttons_frame = tk.Frame(master=self.search_container, bg=gray)
        self.buttons_frame.grid_propagate(0)
        self.buttons_frame.pack(side="left")
        
        self.addRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Add Record",  command=lambda: self.OpenButtonWindow(NewRecord()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.addRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
        
        self.editRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Edit Record", command=lambda: self.OpenButtonWindow(EditRecord()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.editRecsBtn.pack(anchor="se", side="left", padx=(21, 0))
                
        self.exportRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Export Records", command=lambda: self.OpenButtonWindow(ExportGRecords()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
        self.exportRecsBtn.pack(anchor="se", side="left", padx=(21, 0))
                 
        
        table_data = [
            ["Record ID", "Employee Name", "Printer Model", "Colored or B&W","Number of Pages", "Page Type", "Print Type", "Date", "Time", "Description"],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored', '12', 'Legal', 'Internal', '10/12/23','1:45 PM', 'School Project'],
            ['3833', 'John Doe', 'Xerox C17', 'Colored', '2', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['5629', 'Jane Allen', 'Xerox C17', 'B&W', '12', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored', '12', 'Letter', 'Internal', '10/12/23','11:00 AM', 'School Project'],
            ['3833', 'Jamie Dodger', 'Xerox C17', 'B&W', '12', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['3834', 'Jane Doe', 'Xerox C17', 'B&W', '12', 'Tabloid', 'Wasted', '16/7/23','2:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'B&W', '12', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['1343', 'Jane Doe', 'Xerox C17', 'B&W', '45', 'Letter', 'Wasted', '10/12/23','7:35 AM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored', '7', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['5633', 'Yelan Smith', 'Xerox C17', 'B&W', '12', 'Tabloid', 'Internal', '10/12/23','10:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored', '11', 'Letter', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['8814', 'Jane Doe', 'Xerox C17', 'B&W', '132', 'Letter', 'Wasted', '10/12/23','2:35 PM', 'School Project'],
            ['3833', 'James Potter', 'Xerox C17', 'Colored', '12', 'Legal', 'Internal',  '10/15/23','2:35 PM', 'School Project'],
            ['3663', 'Jane Doe', 'Xerox C17', 'B&W', '12', 'Legal', 'Wasted', '10/12/23','8:35 AM', 'School Project'],
            ['3835', 'Jane Doe', 'Xerox C17', 'B&W', '12', 'Legal', 'Wasted', '10/12/23','2:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored', '34', 'Tabloid', 'Internal', '10/12/23','5:35 PM', 'School Project'],
            ['7833', 'Jane Doe', 'Xerox C17', 'B&W', '12', 'Letter', 'Internal', '5/12/23','2:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'B&W','12', 'Letter', 'Internal', '10/12/23','11:00 AM', 'School Project'],
            ['3833', 'Jamie Dodger', 'Xerox C17', 'Colored', '12', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['3834', 'Jane Doe', 'Xerox C17', 'Colored', '12', 'Tabloid', 'Internal', '16/7/23','2:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored', '12', 'Legal', 'Wasted', '10/12/23','2:35 PM', 'School Project'],
            ['1343', 'Jane Doe', 'Xerox C17', 'Colored', '45', 'Letter', 'Internal', '10/12/23','7:35 AM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'Colored','7', 'Legal', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['5633', 'Yelan Smith', 'Xerox C17', 'Colored','12', 'Tabloid', 'Wasted', '10/12/23','10:35 PM', 'School Project'],
            ['3833', 'Jane Doe', 'Xerox C17', 'B&W', '11', 'Letter', 'Internal', '10/12/23','2:35 PM', 'School Project'],
            ['8814', 'Jane Doe', 'Xerox C17', 'B&W', '132', 'Letter', 'Internal', '10/12/23','2:35 PM', 'School Project'],
           
        ] 

        self.table_frame = CTkXYFrame(master=self.main_view, width=1100, height=650, fg_color="#fff")
        self.table_frame.pack(expand=True, fill="both", padx=(25, 18), pady=20)
        self.table_frame.pack(anchor="w", side="left")
        self.table = ctkt(master=self.table_frame, values=table_data, corner_radius=7, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
        self.table.edit_row(0, text_color=white, hover_color="#2A8C55")
        self.table.pack()
        self.table.pack(anchor="w", side="left")
        

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
             
        

class NewRecord:
    entry_value = '' # ignore this
    
    def __init__(self):
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
        
        self.recordidframe = tk.Frame(self.window)
        self.recordidframe.pack(anchor='center', side='top', pady=10)
        self.label = tk.Label(self.recordidframe, text='Record ID: ', font=("Arial Black", 12), fg="#2A8C55")
        self.label.pack(side="left")      
        self.idinfolbl = tk.Label(self.recordidframe, font=("Arial", 12))
        self.idinfolbl.pack(side="left") 
        self.idinfolbl.configure(text= "#" + str(51)) 
        
        self.employeeframe = tk.Frame(self.window, width=80)
        self.employeeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.employeeframe, text='Employee: ')
        self.label.pack(side="left", padx=15)        
        self.EmployeeBox = ctk.CTkComboBox(self.employeeframe, width=150, values=["Select Employee", "Jane Doe", "Jamie Dodger", "James Potter"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.EmployeeBox.pack(side="right")
        
        self.printerframe = tk.Frame(self.window, width=80)
        self.printerframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.printerframe, text='Printer Model: ')
        self.label.pack(side="left", padx=15)        
        self.PrintModelBox = ctk.CTkComboBox(self.printerframe, width=150, values=["Select Model", "Xerox C70", "Sharp MXM 456"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PrintModelBox.pack(side="right")
        
        self.radiobuttonsframe = tk.Frame(self.window, width=80)
        self.radiobuttonsframe.pack(anchor='nw', side='top', pady=10)
        self.radio_var = tk.IntVar(value=0)
        self.coloredbtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Colored", variable=self.radio_var, value=0)
        self.coloredbtn.pack(side="left", padx=(25, 10))
        self.blackwhitebtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Black & White", variable=self.radio_var, value=1)
        self.blackwhitebtn.pack(side="left")
        
        self.pagesframe = tk.Frame(self.window, width=80)
        self.pagesframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagesframe, text='# of Pages: ')
        self.label.pack(side="left", padx=15)      
        self.pagesentry = ctk.CTkEntry(master=self.pagesframe, width=50, border_color="#2A8C55", border_width=2)
        self.pagesentry.pack(side="right")
        
        self.pagetypeframe = tk.Frame(self.window, width=80)
        self.pagetypeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagetypeframe, text='Page Type: ')
        self.label.pack(side="left", padx=15)        
        self.PageTypeBox = ctk.CTkComboBox(self.pagetypeframe, width=150, values=["Select Page Type", "Legal", "Letter", "Tabloid", "A4"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageTypeBox.pack(side="right")
        
        self.printtypeframe = tk.Frame(self.window, width=80)
        self.printtypeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.printtypeframe, text='Print Type: ')
        self.label.pack(side="left", padx=15)        
        self.PageTypeBox = ctk.CTkComboBox(self.printtypeframe, width=150, values=["Select Print Type", "Internal", "Wasted"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageTypeBox.pack(side="right")
        
        self.datetimeframe = tk.Frame(self.window, width=80)
        self.datetimeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.datetimeframe, text='Date:')
        self.label.pack(side="left", padx=(15,10))      
        self.dateentry = ctk.CTkEntry(master=self.datetimeframe, width=83, border_color="#2A8C55", border_width=2)
        self.dateentry.pack(side="left")
        time = dt.now()
        datestamp = time.strftime('%d/%m/%Y')
        self.dateentry.insert(0, datestamp)
        self.label = tk.Label(self.datetimeframe, text='Time:')
        self.label.pack(side="left", padx=10)      
        self.timeentry = ctk.CTkEntry(master=self.datetimeframe, width=87, border_color="#2A8C55", border_width=2)
        self.timeentry.pack(side="left")        
        timestamp = time.strftime('%I:%M:%S %p')
        self.timeentry.insert(0, timestamp)
        
        self.descriptionframe = tk.Frame(self.window)
        self.descriptionframe.pack(anchor='nw', side='top', padx=15, pady=(15,5))
        self.label = tk.Label(self.descriptionframe, text='Description: ')
        self.label.pack(anchor='nw', side="top", pady=(0,5))   
        self.desctxtbox = ctk.CTkTextbox(self.descriptionframe, width=350, height=80, border_color="#2A8C55", border_width=2)  
        self.desctxtbox.pack(anchor='nw', side="bottom", padx=3)      
        
        
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=20)
        self.addrecbtn = ctk.CTkButton(self.buttonframe, text="Add Record", command=self.AddNewRecord, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
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
        pass
        
        
 
        
class EditRecord:
    def __init__(self):
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
        
        window_height = 595
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
        self.employeeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.employeeframe, text='Employee: ')
        self.label.pack(side="left", padx=15)        
        self.EmployeeBox = ctk.CTkComboBox(self.employeeframe, width=150, values=["Select Employee", "Jane Doe", "Jamie Dodger", "James Potter"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.EmployeeBox.pack(side="right")
        
        self.printerframe = tk.Frame(self.window, width=80)
        self.printerframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.printerframe, text='Printer Model: ')
        self.label.pack(side="left", padx=15)        
        self.PrintModelBox = ctk.CTkComboBox(self.printerframe, width=150, values=["Select Model", "Xerox C70", "Sharp MXM 456"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PrintModelBox.pack(side="right")
        
        self.radiobuttonsframe = tk.Frame(self.window, width=80)
        self.radiobuttonsframe.pack(anchor='nw', side='top', pady=10)
        self.radio_var = tk.IntVar(value=0)
        self.coloredbtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Colored", variable=self.radio_var, value=0)
        self.coloredbtn.pack(side="left", padx=(25, 10))
        self.blackwhitebtn = ctk.CTkRadioButton(master=self.radiobuttonsframe, text="Black & White", variable=self.radio_var, value=1)
        self.blackwhitebtn.pack(side="left")
        
        self.pagesframe = tk.Frame(self.window, width=80)
        self.pagesframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagesframe, text='# of Pages: ')
        self.label.pack(side="left", padx=15)      
        self.pagesentry = ctk.CTkEntry(master=self.pagesframe, width=50, border_color="#2A8C55", border_width=2)
        self.pagesentry.pack(side="right")
        
        self.pagetypeframe = tk.Frame(self.window, width=80)
        self.pagetypeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.pagetypeframe, text='Page Type: ')
        self.label.pack(side="left", padx=15)        
        self.PageTypeBox = ctk.CTkComboBox(self.pagetypeframe, width=150, values=["Select Page Type", "Legal", "Letter", "Tabloid", "A4"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageTypeBox.pack(side="right")
        
        self.printtypeframe = tk.Frame(self.window, width=80)
        self.printtypeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.printtypeframe, text='Print Type: ')
        self.label.pack(side="left", padx=15)        
        self.PageTypeBox = ctk.CTkComboBox(self.printtypeframe, width=150, values=["Select Print Type", "Internal", "Wasted"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.PageTypeBox.pack(side="right")
        
        self.datetimeframe = tk.Frame(self.window, width=80)
        self.datetimeframe.pack(anchor='nw', side='top', pady=10)
        self.label = tk.Label(self.datetimeframe, text='Date:')
        self.label.pack(side="left", padx=(15,10))      
        self.dateentry = ctk.CTkEntry(master=self.datetimeframe, width=83, border_color="#2A8C55", border_width=2)
        self.dateentry.pack(side="left")
        time = dt.now()
        datestamp = time.strftime('%d/%m/%Y')
        self.dateentry.insert(0, datestamp)
        self.label = tk.Label(self.datetimeframe, text='Time:')
        self.label.pack(side="left", padx=10)      
        self.timeentry = ctk.CTkEntry(master=self.datetimeframe, width=87, border_color="#2A8C55", border_width=2)
        self.timeentry.pack(side="left")        
        timestamp = time.strftime('%I:%M:%S %p')
        self.timeentry.insert(0, timestamp)
        
        self.descriptionframe = tk.Frame(self.window)
        self.descriptionframe.pack(anchor='nw', side='top', padx=15, pady=(15,5))
        self.label = tk.Label(self.descriptionframe, text='Description: ')
        self.label.pack(anchor='nw', side="top", pady=(0,5))   
        self.desctxtbox = ctk.CTkTextbox(self.descriptionframe, width=350, height=80, border_color="#2A8C55", border_width=2)  
        self.desctxtbox.pack(anchor='nw', side="bottom", padx=3)      
        
        
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=18)
        self.saverecbtn = ctk.CTkButton(self.buttonframe, text="Save Record", command=self.SaveRecordChanges, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.saverecbtn.pack(side='left', padx=15)
        self.cancelbtn = ctk.CTkButton(self.buttonframe, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=15)

    def window_exit(self):
        self.window.destroy()  
        
    def FindRecord(self):
        pass
    
    def SaveRecordChanges(self):
        pass
        
        
        
        
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