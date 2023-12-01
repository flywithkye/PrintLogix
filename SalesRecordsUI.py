# Importing modules/libraries to build gui elements
import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg
from PIL import ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox as mgbx
# Import helper libraries
import pandas as pd 
import csv
import string

# Sales records screen that is displayed when selected using sidebar in GeneralViewUI
class SalesRecordsUI(tk.Frame):
    # Class constructor for screen, creates gui components and intializes it
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.box = None
        self.table_data = []
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        error_red = "#FF0000"
        white = "#ffffff"        
        gray = "#F0F0F0"
        black = "#000000"
        
        # Container/frame in which all widgets are displayed  
        self.main_view = tk.Frame(self, bg=white)
        self.main_view.pack(side="left", fill="both", expand=True)
        # Container/frame in which the title is displayed  
        self.title_frame = tk.Frame(master=self.main_view, bg=white)
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(24, 0))

        # Creating label to store and display title of the screen
        self.genTitleLbl = ctk.CTkLabel(master=self.title_frame, width=50, text="Sales Print Records - Administrator - admin1234", fg_color=white, font=("Arial Black", 24), text_color=dark_green)
        self.genTitleLbl.pack(anchor="n")    
        
        # Container/frame in which the search widgets are displayed              
        self.search_container = tk.Frame(master=self.main_view, height=50, bg=gray)
        self.search_container.pack(fill="x", pady=(19, 0), padx=32)    
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white        
        # Dropdwon for sort options
        self.SortBox = ctk.CTkComboBox(master=self.search_container, width=140, state="readonly", values=["Sort By"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.SortBox.pack(side="right", padx=(16, 15), pady=15)
        self.SortBox.set("Sort By")
        
        # Input field for searching records
        self.SearchEntry = ctk.CTkEntry(master=self.search_container, width=305, placeholder_text="Search Records", border_color="#2A8C55", border_width=2)
        self.SearchEntry.pack(side="right", padx=(13, 0), pady=15)
        
        # Container/frame in which the button widgets are displayed
        self.buttons_frame = tk.Frame(master=self.search_container, bg=gray)
        self.buttons_frame.grid_propagate(0)
        self.buttons_frame.pack(side="left")
        
        # Creating Button that will run a method which launches the window that uploads sales records
        self.uploadRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Upload Records",  command=lambda: self.OpenButtonWindow(UploadRecords()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=165)
        self.uploadRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
        
        # Creating Button that will run a method which launches the window that exports records as excel file       
        self.exportRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Export Records", state="disabled", command=lambda: self.OpenButtonWindow(ExportSRecords(self.table_data)), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
        self.exportRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
               
          # Variables to store values that populate table   
        self.table_data = [
            ["", "", "", "", "", "", "", "", "", "", ""]
        ] 
        
        # Creating container for table, creating and populating table        
        self.table_frame = CTkXYFrame(master=self.main_view, width=1100, height=650, fg_color="#fff")
        self.table_frame.pack(expand=True, fill="both", padx=(25, 18), pady=20)
        self.table_frame.pack(anchor="w", side="left")
        self.table = ctkt(master=self.table_frame, values=self.table_data, row=30, corner_radius=7, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
        self.table.edit_row(0, text_color=white, hover_color="#2A8C55")
        self.table.pack()
        self.table.pack(anchor="w", side="left")
        
        
   # Method to repopulate table to reflect any changes to its data
    def UpdateTable(self):      
        self.table.update_values(values=self.table_data)
        
    
    # Method to launch the window of the desired classtype 
    def OpenButtonWindow(self, classtype):
        if self.box != None:                
            if self.box.window.winfo_exists() != True:                      
                # create window
                self.box = classtype
                    
                # set it modal (to wait for value)
                self.box.window.focus_force()
                #self.box.window.focus_set()   # take over input focus,
                self.box.window.grab_set()    # disable other windows while I'm open,
                self.box.window.wait_window() # and wait here until win destroyed
        else:
            # create window
            self.box = classtype
                
            # set it modal (to wait for value)
            self.box.window.focus_force()
            #self.box.window.focus_set()   # take over input focus,
            #self.box.window.grab_set()    # disable other windows while I'm open,
            self.box.window.wait_window() # and wait here until win destroyed
        
        # Updates table to reflect uploaded records
        if isinstance(self.box, UploadRecords):
            if self.box.tabledata != []:
                self.table.update_values(values=[])  
                self.table_data = self.box.tabledata.copy()
                mgbx.showinfo("Success", "Records uploaded successfully.")
                self.exportRecsBtn.configure(state="normal") 
                self.UpdateTable()
            
        
            
        
# Window that takes a desired csv and extracts the data from it to repopulate the table
class UploadRecords:    
    def __init__(self): 
        # To store extracted data
        self.tabledata = []     
         
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
        
        # Creating window and initializing it
        self.window = tk.Toplevel()
        self.window.iconbitmap(icon_img)      
        self.window.wm_title("Upload Records")        
        
        # Set app size and centering it
        window_height = 150
        window_width = 385
        screen_width = self.window.winfo_screenwidth()
        #screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = 110
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            
        self.window.resizable(False,False) 
        
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white     
          
        # Creating container for file path entry field, autofilled to reflect file selected
        self.linkframe = tk.Frame(self.window)
        self.linkframe.pack(anchor='nw', side='top', padx=15, pady=(17,0))
        self.label = tk.Label(self.linkframe, text='Choose a .csv File: ')
        self.label.pack(anchor='nw', side="top", pady=(0,3))   
        self.innerframe = tk.Frame(self.linkframe)
        self.innerframe.pack(anchor='nw', side="bottom")
        self.linkentry = ctk.CTkEntry(master=self.innerframe, width=299, border_color="#2A8C55", border_width=2)
        self.linkentry.pack(side="left", padx=(3,10))
        folder_img = ImageTk.PhotoImage(image=folder_img_data)
        self.folderBtn = ctk.CTkButton(master=self.innerframe, command=self.OpenFileExplorer, width=40, image=folder_img, text="", text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.folderBtn.pack(side="right")
        
        
        # Container/frame in which the button widgets are displayed
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=(0,23))
        # Create button which actively uploads records from chosen file into system
        self.uploadrecsbtn = ctk.CTkButton(self.buttonframe, state="disabled", width=150, text="Upload File", command=self.StartUpload, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.uploadrecsbtn.pack(side='left', padx=15)
        # Create button which closes window
        self.cancelbtn = ctk.CTkButton(self.buttonframe, width=110, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=15)
              
    
    # Method to close method
    def window_exit(self):
        self.window.destroy()    
        
    
    # Method to open file explorer to retrive the path to the desired file
    def OpenFileExplorer(self):
        try: 
            self.file_name = fd.askopenfilename(initialdir = '/Desktop', 
                                                            title = 'Select a File', 
                                                            filetypes = (('csv files','*.csv'), 
                                                                        ("csv files","*.csv*")))
        
            self.uploadrecsbtn.configure(state="normal")
            self.linkentry.delete(0 ,'end')
            self.linkentry.insert(0, self.file_name)            
        except FileNotFoundError as e: 
            print(e) 
            mgbx.showerror('Error in opening file',e)             
        
    
    # Method to extract records from a valid file
    def StartUpload(self):
        # STores output of extraction from file
        csv_data = []
        
        try: 
            # Read from file using link in the input field
            with open(self.linkentry.get()) as file_obj:
                reader = csv.reader(file_obj)
                for row in reader:
                    csv_data.append(row)
                    
            print(csv_data)
            
            if len(csv_data) == 0: 
                mgbx.showerror('Error', 'Error: File path is invalid.') 
            else:
                self.tabledata = csv_data.copy()
                self.window_exit()  
                 
        except FileNotFoundError as e: 
            print(e) 
            mgbx.showerror('Error', 'Error: File not found.')    
        
             
        
         
# Window that takes all records from the database and converts them to an excel file in a
# given directory                
class ExportSRecords:
    def __init__(self, tabledata): 
        # Storing reference to the variable the table pulls values from
        self.csvdata = tabledata
        
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
        
        # Creating window and initializing it
        self.window = tk.Toplevel()
        self.window.iconbitmap(icon_img)      
        self.window.wm_title("Export Sales Records")        
        
        # Set app size and centering it
        window_height = 230
        window_width = 385
        screen_width = self.window.winfo_screenwidth()
        #screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = 110
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            
        self.window.resizable(False,False) 
        
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white 
        
        # Creating container for name entry field
        self.nameframe = tk.Frame(self.window)
        self.nameframe.pack(anchor='nw', side='top', padx=15, pady=(17,0))
        self.label = tk.Label(self.nameframe, text='Select File Name: ')
        self.label.pack(anchor='nw', side="top", pady=(0,3))   
        self.innerframe = tk.Frame(self.nameframe)
        self.innerframe.pack(anchor='nw', side="bottom")
        self.nameentry = ctk.CTkEntry(master=self.innerframe, width=299, border_color="#2A8C55", border_width=2)
        self.nameentry.pack(side="left", padx=(3,10))      
        
        # Creating container for name entry field, autofilled to reflect directory selected
        self.linkframe = tk.Frame(self.window)
        self.linkframe.pack(anchor='nw', side='top', padx=15, pady=(17,0))
        self.label = tk.Label(self.linkframe, text='Select Output Directory: ')
        self.label.pack(anchor='nw', side="top", pady=(0,3))   
        self.innerframe = tk.Frame(self.linkframe)
        self.innerframe.pack(anchor='nw', side="bottom")
        self.linkentry = ctk.CTkEntry(master=self.innerframe, width=299, border_color="#2A8C55", border_width=2)
        self.linkentry.pack(side="left", padx=(3,10))
        folder_img = ImageTk.PhotoImage(image=folder_img_data)
        self.folderBtn = ctk.CTkButton(master=self.innerframe, command=self.OpenFileExplorer, width=40, image=folder_img, text="", text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.folderBtn.pack(side="right")
        
        
        # Container/frame in which the button widgets are displayed
        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.pack(anchor='center', side='bottom', pady=(0,23))
        # Create button which actively exports records to chosen directory
        self.exportbtn = ctk.CTkButton(self.buttonframe, width=170, state="disabled", text="Export To Excel", command=self.StartExport, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.exportbtn.pack(side='left', padx=15)
        # Create button which closes window
        self.cancelbtn = ctk.CTkButton(self.buttonframe, width=110, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=15)
              

    
    # Method to close method
    def window_exit(self):
        self.window.destroy()  
        
    
    # Method to open file explorer to retrive the path to the desired directory 
    def OpenFileExplorer(self):
        try: 
            self.selected_directory = fd.askdirectory()
            """print("dir:") 
            print(self.selected_directory)"""
            self.linkentry.delete(0, tk.END)
            self.linkentry.insert(0, self.selected_directory)
            self.exportbtn.configure(state="normal")
        except Exception as e: 
            print(e) 
            mgbx.showerror('Error','Error: ' + e)  
        
    
    # Method to export records to a valid directory
    def StartExport(self):
        # Checks to make sure the given file name and file directory is valid before exporting 
        allowed = set(string.ascii_letters + string.digits + '_' + '-')
        if self.nameentry.get() == "":
            mgbx.showerror('Error','Error: Please enter a file name.')  
        elif any(char not in allowed for char in self.nameentry.get()):
            mgbx.showerror('Error','Error: File name must not have special characters.') 
        elif self.linkentry.get() == "":
            mgbx.showerror('Error','Error: Please select a directory.')
        else:
            df = pd.DataFrame(self.csvdata)
                        
            try:
                # Write DataFrame to an Excel file
                df.to_excel(self.linkentry.get() + "\\" + self.nameentry.get() + ".xlsx",  index=False)
                mgbx.showinfo('Success', 'Excel File created in: ' + self.linkentry.get())
                self.window_exit()                  
            except Exception:
                mgbx.showerror('Error','Error: Export unsuccessful. Ensure \ndirectory path is valid.')  
            
        