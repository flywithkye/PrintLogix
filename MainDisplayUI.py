import tkinter as tk
import customtkinter as ctk  
from tkinter.ttk import Combobox as ttkCb
from PIL import Image as pImg
from PIL import ImageTk
from tksheet import Sheet as shtk

class MainDisplayUI(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        white = "#ffffff"        
        gray = "#F0F0F0"
        black = "#000000"
        
        # Storing images
        icon_img = "images\\logo.ico"
        logo_img_data = pImg.open("images\\ICON.png")
        logo_img_data = logo_img_data.resize((80, 70))
        logo_txt_data = pImg.open("images\\logo_text.png")
        logo_txt_data = logo_txt_data.resize((137, 25))
        records_img_data = pImg.open("images\\records_icon.png")
        sales_img_data = pImg.open("images\\sales_icon.png")
        settings_img_data = pImg.open("images\\settings_icon.png")
        acnt_img_data = pImg.open("images\\acnt_icon.png")
        totalrs_img_data = pImg.open("images\\totalrecs_icon.png")
        
        # Set app title
        self.title("PrintLogix - Administrator - admin1234")
        # Set app size
        self.geometry("1080x720")
        self.minsize(1080, 720)
        self.state("zoomed")
        # Set app icon
        self.iconbitmap(icon_img)

        self.sidebar_frame = tk.Frame(master=self, bg=dark_green,  width=176, height=650)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        
        logo_img = ImageTk.PhotoImage(image=logo_img_data)           
        self.logoImgLbl = tk.Label(master=self.sidebar_frame, image=logo_img, bd=0, bg=dark_green)
        self.logoImgLbl.image = logo_img
        self.logoImgLbl.pack(pady=(70, 0), anchor="center")
        
        logo_txt = ImageTk.PhotoImage(image=logo_txt_data)
        self.logoTxtLbl = tk.Label(master=self.sidebar_frame, bd=0, image=logo_txt, bg=dark_green)
        self.logoTxtLbl.image = logo_txt
        self.logoTxtLbl.pack(pady=(20, 0), anchor="center")        
        
        recs_img = ctk.CTkImage(dark_image=records_img_data, light_image=records_img_data, size=(23, 23))
        self.recordsLbl = ctk.CTkButton(master=self.sidebar_frame, command=self.ChangetoGenRecords, image=recs_img, text="General", fg_color="transparent", font=("Arial Bold", 17), hover_color=white, anchor="w")
        self.recordsLbl.pack(anchor="center", ipady=5, pady=(50, 0))

        sales_img = ctk.CTkImage(dark_image=sales_img_data, light_image=sales_img_data, size=(23, 23))
        self.salesLbl = ctk.CTkButton(master=self.sidebar_frame, command=self.ChangetoSalesRecords, image=sales_img, text="Sales", fg_color="transparent", font=("Arial Bold", 17), hover_color=white, anchor="w")
        self.salesLbl.pack(anchor="center", ipady=5, pady=(16, 0))
        
        settings_img = ctk.CTkImage(dark_image=settings_img_data, light_image=settings_img_data, size=(23, 23))
        self.settingsLbl = ctk.CTkButton(master=self.sidebar_frame, command=self.ChangetoSettings, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 17), hover_color=white, anchor="w")
        self.settingsLbl.pack(anchor="center", ipady=5, pady=(16, 0))
        
        acnt_img = ctk.CTkImage(dark_image=acnt_img_data, light_image=acnt_img_data, size=(23, 23))
        self.accountLbl = ctk.CTkButton(master=self.sidebar_frame, image=acnt_img, text="Account", fg_color="transparent", font=("Arial Bold", 17), hover_color=white, anchor="w")
        self.accountLbl.pack(anchor="center", ipady=5, pady=(330, 0))
        
        
        self.main_view = tk.Frame(master=self, bg=white,  width=1290, height=815)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = tk.Frame(master=self.main_view, bg=white)
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(35, 0))

        self.genTitleLbl = tk.Label(master=self.title_frame, text="General Print Records", bg=white, font=("Arial Black", 19), fg=dark_green)
        self.genTitleLbl.pack(anchor="nw", side="left")
        
        self.exportRecsBtn = ctk.CTkButton(master=self.title_frame, text="Export Records",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
        self.exportRecsBtn.pack(anchor="se", side="right", padx=(15, 0), pady=15)
        
        self.editRecsBtn = ctk.CTkButton(master=self.title_frame, text="Edit Record",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.editRecsBtn.pack(anchor="se", side="right", padx=(15, 0), pady=15)
        
        self.addRecsBtn = ctk.CTkButton(master=self.title_frame, text="Add Record",  font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.addRecsBtn.pack(anchor="se", side="right", padx=(15, 0), pady=15)
                
        self.search_container = tk.Frame(master=self.main_view, height=50, bg=gray)
        self.search_container.pack(fill="x", pady=(16, 0), padx=27)    
        
        ctk.set_appearance_mode("light")  
        self.filterBox = ctk.CTkComboBox(master=self.search_container, width=125, values=["Filter", "Processing", "Confirmed", "Packing", "Shipping", "Delivered", "Cancelled"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.filterBox.pack(side="right", padx=(16, 15), pady=15)
        self.SortBox = ctk.CTkComboBox(master=self.search_container, width=125, values=["Sort By", "Date", "Least Recent Order"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.SortBox.pack(side="right", padx=(16, 0), pady=15)
        
        self.SearchEntry = ctk.CTkEntry(master=self.search_container, width=305, placeholder_text="Search Records", border_color="#2A8C55", border_width=2)
        self.SearchEntry.pack(side="right", padx=(13, 0), pady=15)
        
        self.metrics_frame = tk.Frame(master=self.search_container, bg=dark_green, width=190, height=35)
        self.metrics_frame.grid_propagate(0)
        self.metrics_frame.pack(side="left", padx=(25, 0), pady=10)

        self.metrictxt = tk.Label(master=self.metrics_frame, text="Total: 123", bg=dark_green, fg=white, font=("Arial Black", 13))
        self.metrictxt.pack(anchor="center", padx=(18, 18))
        
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

        self.table_frame = tk.Frame(master=self.main_view, width=1190, height=545,  bg=dark_green, bd=2)
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=35)
        self.table_frame.pack(anchor="w", side="left")
        
        self.sheet = shtk(self.table_frame, headers = table_data[0], data = table_data[1:], edit_cell_validation=False, width=1184, height=533)
        self.sheet.change_theme(theme = "light green", redraw = True)
        self.sheet.font(newfont=("Arial", 10, "normal"), reset_row_positions= True)
        self.sheet.header_font(newfont=("Arial", 11, "normal"))
        self.sheet.header_align("w")
        self.sheet.enable_bindings("drag_select","column_select","single_select","toggle_select","row_select","column_width_resize","row_width_resize")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
    def ChangetoGenRecords(self):
        pass
               
        
    def ChangetoSalesRecords(self):
        pass
                
        
    def ChangetoSettings(self):
        pass
    
    
    def OpenLogin(self):
        pass
        