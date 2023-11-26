import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg



class SalesRecordsUI(tk.Frame):
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

        self.genTitleLbl = tk.Label(master=self.title_frame, width=50, text="Sales Print Records - Administrator - admin1234", bg=white, font=("Arial Black", 19), fg=dark_green)
        self.genTitleLbl.pack(anchor="n")    
              
        self.search_container = tk.Frame(master=self.main_view, height=50, bg=gray)
        self.search_container.pack(fill="x", pady=(19, 0), padx=32)    
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white
        self.filterBox = ctk.CTkComboBox(master=self.search_container, width=125, values=["Filter"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.filterBox.pack(side="right", padx=(16, 15), pady=15)
        self.SortBox = ctk.CTkComboBox(master=self.search_container, width=125, values=["Sort By"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.SortBox.pack(side="right", padx=(16, 0), pady=15)
        
        self.SearchEntry = ctk.CTkEntry(master=self.search_container, width=305, placeholder_text="Search Records", border_color="#2A8C55", border_width=2)
        self.SearchEntry.pack(side="right", padx=(13, 0), pady=15)
            
        self.buttons_frame = tk.Frame(master=self.search_container, bg=gray)
        self.buttons_frame.grid_propagate(0)
        self.buttons_frame.pack(side="left")
        
        self.uploadRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Upload Records",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=165)
        self.uploadRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
        
        self.exportRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Export Records",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
        self.exportRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
               
  
        
        table_data = [
            ["Loc_Settings_LocID","Sal_Ticket","Sal_RegID","Inv_Sku","Inv_Desc","Sal_Quan","Sal_Items_Price_Unit","Sal_Items_Price_Ext","Sal_Items_Cost_Unit","Sal_Items_Cost_Ext","Sal_Items_Retail_Unit","Sal_Items_Retail_Ext","Sal_Items_Taxable","Clerk_Name","Dept_DepartID","Vend_VendorID","Sal_Track_Name","Sal_Date","Cust_CustID","Cust_B_LastName","Cust_B_FirstName","Cust_B_Company","Inv_ItemID","Cla_ClassID","Inv_UPC1","Inv_UPC2"],
            ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
            ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
            ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
            ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
            ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
            ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
            ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
            ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
            ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
            ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
            ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
            ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
            ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
            ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
            ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
            ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
            ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
            ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10'],
            ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
            ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
            ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
            ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
            ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
            ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
            ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
            ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
            ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
            ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
            ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
            ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
            ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
            ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
            ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
            ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']       
        ] 

        self.table_frame = CTkXYFrame(master=self.main_view, width=1100, height=650, fg_color="#fff")
        self.table_frame.pack(expand=True, fill="both", padx=(25, 18), pady=20)
        self.table_frame.pack(anchor="w", side="left")
        self.table = ctkt(master=self.table_frame, values=table_data, corner_radius=7, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
        self.table.edit_row(0, text_color=white, hover_color="#2A8C55")
        self.table.pack()
        self.table.pack(anchor="w", side="left")