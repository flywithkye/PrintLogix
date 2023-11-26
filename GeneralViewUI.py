import tkinter as tk
import customtkinter as ctk  
from CTkXYFrame import *
from CTkTable import CTkTable as ctkt
from tkinter.ttk import Combobox as ttkCb
from PIL import Image as pImg
from PIL import ImageTk
from tksheet import Sheet as shtk

from GeneralRecordsUI import GeneralRecordsUI
from SalesRecordsUI import SalesRecordsUI

class GeneralViewUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        # Pre-defining Colors
        self.dark_green = "#29A165"
        self.darker_green = "#1E8350" 
        self.white = "#ffffff"        
        self.gray = "#F0F0F0"
        self.black = "#000000"
        
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
        self.title("PrintLogix")
        # Set app size
        self.geometry("1080x720")
        self.minsize(1080, 720)
        self.state("zoomed")
        # Set app icon
        self.iconbitmap(icon_img)

        self.sidebar_frame = tk.Frame(master=self, bg=self.dark_green,  width=176, height=650)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        
        logo_img = ImageTk.PhotoImage(image=logo_img_data)           
        self.logoImgLbl = tk.Label(master=self.sidebar_frame, image=logo_img, bd=0, bg=self.dark_green)
        self.logoImgLbl.image = logo_img
        self.logoImgLbl.pack(pady=(55, 0), anchor="center")
        
        logo_txt = ImageTk.PhotoImage(image=logo_txt_data)
        self.logoTxtLbl = tk.Label(master=self.sidebar_frame, bd=0, image=logo_txt, bg=self.dark_green)
        self.logoTxtLbl.image = logo_txt
        self.logoTxtLbl.pack(pady=(20, 0), anchor="center")        
        
        recs_img = ctk.CTkImage(dark_image=records_img_data, light_image=records_img_data, size=(23, 23))
        self.recordsBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoGenRecords, width=150, image=recs_img, text="General", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.darker_green, anchor="w")
        self.recordsBtn.pack(anchor="center", ipady=5, pady=(50, 0))

        sales_img = ctk.CTkImage(dark_image=sales_img_data, light_image=sales_img_data, size=(23, 23))
        self.salesBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoSalesRecords, width=150, image=sales_img, text="Sales", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.darker_green, anchor="w")
        self.salesBtn.pack(anchor="center", ipady=5, pady=(16, 0))
        
        settings_img = ctk.CTkImage(dark_image=settings_img_data, light_image=settings_img_data, size=(23, 23))
        self.settingsBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoSettings, width=150, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.darker_green, anchor="w")
        self.settingsBtn.pack(anchor="center", ipady=5, pady=(16, 0))
        
        acnt_img = ctk.CTkImage(dark_image=acnt_img_data, light_image=acnt_img_data, size=(23, 23))
        self.accountBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoLogin, image=acnt_img, text="Account", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.white, anchor="w")
        self.accountBtn.pack(anchor="center", ipady=5, pady=(330, 0))
        
                
        main_container = tk.Frame(master=self, bg=self.white)
        main_container.pack(side="left", fill="both", anchor="center", expand=True)        
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        # tell frame not to let its children control its size
        main_container.pack_propagate(0)
        
        self.frames = {}
        for F in (GeneralRecordsUI, SalesRecordsUI):
            page_name = F.__name__
            frame = F(parent=main_container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self. NavigatetoGenRecords()
        

        #self.title_frame = gRecsUI.GeneralRecordsUI(self.main_view)
        
            
    def NavigatetoGenRecords(self):
        self.recordsBtn.configure(fg_color=self.darker_green)        
        self.salesBtn.configure(fg_color=self.dark_green)
        self.settingsBtn.configure(fg_color=self.dark_green)
        
        frame = self.frames["GeneralRecordsUI"]        
        frame.tkraise()
           
        
    def NavigatetoSalesRecords(self):
        self.salesBtn.configure(fg_color=self.darker_green)
        self.recordsBtn.configure(fg_color=self.dark_green)
        self.settingsBtn.configure(fg_color=self.dark_green)
                        
        frame = self.frames["SalesRecordsUI"]
        frame.tkraise()
                
        
    def NavigatetoSettings(self):
        self.settingsBtn.configure(fg_color=self.darker_green)
        self.recordsBtn.configure(fg_color=self.dark_green)
        self.salesBtn.configure(fg_color=self.dark_green)
    
    
    def NavigatetoLogin(self):
        pass
        
        
        
        
        
"""
class GeneralRecordsUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        self.controller = controller
        
        frame1 = tk.Frame(self, bg="#1E8350")
        frame1.pack(side="left", fill="both", expand=True)
        label = tk.Label(frame1, text="This is the start page")
        label.pack(side="left", fill="x", pady=10)

        button1 = tk.Button(frame1, text="Go to Page One",
                            command=lambda: controller.show_frame("SalesRecordsUI"))
        button1.pack(side="left")
        
        
"""
        
        
        
"""
class SalesRecordsUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("GeneralRecordsUI"))
        button.pack()
"""

        
if __name__ == "__main__":
    app = GeneralViewUI()
    app.mainloop()