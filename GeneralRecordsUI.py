import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg



class GeneralRecordsUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
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

        self.genTitleLbl = tk.Label(master=self.title_frame, width=50, text="General Print Records - Administrator - admin1234", bg=white, font=("Arial Black", 19), fg=dark_green)
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
        
        self.addRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Add Record",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.addRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
        
        self.editRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Edit Record",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.editRecsBtn.pack(anchor="se", side="left", padx=(21, 0))
                
        self.exportRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Export Records",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
        self.exportRecsBtn.pack(anchor="se", side="left", padx=(21, 0))
                 
        
        table_data = [
            ["Record ID", "Employee Name", "Printer Model", "Number of Pages", "Page Type", "Date", "Time", "Description", "Type"],
            ['3833', 'Jane Doe', 'Xerox C17', '12', 'Legal', '10/12/23', '1:45 PM', 'School Project', 'Internal'],
            ['3833', 'John Doe', 'Xerox C17', '2', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['5629', 'Jane Allen', 'Xerox C17', '12', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '12', 'Letter', '10/12/23', '11:00 AM', 'School Project', 'Internal'],
            ['3833', 'Jamie Dodger', 'Xerox C17', '12', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['3834', 'Jane Doe', 'Xerox C17', '12', 'Tabloid', '16/7/23', '2:35 PM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '12', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['1343', 'Jane Doe', 'Xerox C17', '45', 'Letter', '10/12/23', '7:35 AM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '7', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['5633', 'Yelan Smith', 'Xerox C17', '12', 'Tabloid', '10/12/23', '10:35 PM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '11', 'Letter', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['8814', 'Jane Doe', 'Xerox C17', '132', 'Letter', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['3833', 'James Potter', 'Xerox C17', '12', 'Legal', '10/15/23', '2:35 PM', 'School Project', 'Internal'],
            ['3663', 'Jane Doe', 'Xerox C17', '12', 'Legal', '10/12/23', '8:35 AM', 'School Project', 'Internal'],
            ['3835', 'Jane Doe', 'Xerox C17', '12', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '34', 'Tabloid', '10/12/23', '5:35 PM', 'School Project', 'Internal'],
            ['7833', 'Jane Doe', 'Xerox C17', '12', 'Letter', '5/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '12', 'Letter', '10/12/23', '11:00 AM', 'School Project', 'Internal'],
            ['3833', 'Jamie Dodger', 'Xerox C17', '12', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['3834', 'Jane Doe', 'Xerox C17', '12', 'Tabloid', '16/7/23', '2:35 PM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '12', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['1343', 'Jane Doe', 'Xerox C17', '45', 'Letter', '10/12/23', '7:35 AM', 'School Project', 'Internal'],
            ['3833', 'Jane Doe', 'Xerox C17', '7', 'Legal', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['5633', 'Yelan Smith', 'Xerox C17', '12', 'Tabloid', '10/12/23', '10:35 PM', 'School Project', 'Inernal'],
            ['3833', 'Jane Doe', 'Xerox C17', '11', 'Letter', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
            ['8814', 'Jane Doe', 'Xerox C17', '132', 'Letter', '10/12/23', '2:35 PM', 'School Project', 'Internal'],
           
        ] 

        self.table_frame = CTkXYFrame(master=self.main_view, width=1100, height=650, fg_color="#fff")
        self.table_frame.pack(expand=True, fill="both", padx=(25, 18), pady=20)
        self.table_frame.pack(anchor="w", side="left")
        self.table = ctkt(master=self.table_frame, values=table_data, corner_radius=7, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
        self.table.edit_row(0, text_color=white, hover_color="#2A8C55")
        self.table.pack()
        self.table.pack(anchor="w", side="left")