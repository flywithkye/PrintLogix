import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg
from PIL import ImageTk


class SalesRecordsUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.box = None
        
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

        self.genTitleLbl = ctk.CTkLabel(master=self.title_frame, width=50, text="Sales Print Records - Administrator - admin1234", fg_color=white, font=("Arial Black", 24), text_color=dark_green)
        self.genTitleLbl.pack(anchor="n")    
              
        self.search_container = tk.Frame(master=self.main_view, height=50, bg=gray)
        self.search_container.pack(fill="x", pady=(19, 0), padx=32)    
        
        ctk.set_appearance_mode("light")  # keeps ctk widgets white
        self.SortBox = ctk.CTkComboBox(master=self.search_container, width=140, state="readonly", values=["Sort By"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244",dropdown_hover_color="#207244" , dropdown_fg_color="#2A8C55", dropdown_text_color="#fff")
        self.SortBox.pack(side="right", padx=(16, 15), pady=15)
        self.SortBox.set("Sort By")
        
        self.SearchEntry = ctk.CTkEntry(master=self.search_container, width=305, placeholder_text="Search Records", border_color="#2A8C55", border_width=2)
        self.SearchEntry.pack(side="right", padx=(13, 0), pady=15)
            
        self.buttons_frame = tk.Frame(master=self.search_container, bg=gray)
        self.buttons_frame.grid_propagate(0)
        self.buttons_frame.pack(side="left")
        
        self.uploadRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Upload Records",  command=lambda: self.OpenButtonWindow(UploadRecords()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=165)
        self.uploadRecsBtn.pack(anchor="se", side="left", padx=(35, 0))
        
        self.exportRecsBtn = ctk.CTkButton(master=self.buttons_frame, text="Export Records",  command=lambda: self.OpenButtonWindow(ExportSRecords()), font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244", width=160)
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
            self.box.window.focus_set()   # take over input focus,
            #self.box.window.grab_set()    # disable other windows while I'm open,
            self.box.window.wait_window() # and wait here until win destroyed
            
  
  
class UploadRecords:
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
        self.window.wm_title("Upload Records")        
        
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
        self.label = tk.Label(self.linkframe, text='Choose a .csv File: ')
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
        self.uploadrecsbtn = ctk.CTkButton(self.buttonframe, width=150, text="Upload File", command=self.StartUpload, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.uploadrecsbtn.pack(side='left', padx=15)
        self.cancelbtn = ctk.CTkButton(self.buttonframe, width=110, text="Cancel", command=self.window_exit, font=("Arial Bold", 15), height=27, text_color="#fff", fg_color="#2A8C55", hover_color="#207244")
        self.cancelbtn.pack(side='left', padx=15)
              

    def window_exit(self):
        self.window.destroy()    
        
    def OpenFileExplorer(self):
        pass
    
    def StartUpload(self):
        pass
  
            
            
class ExportSRecords:
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
        self.window.wm_title("Export Sales Records")        
        
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