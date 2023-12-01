# Importing modules/libraries to build gui elements
import tkinter as tk
import customtkinter as ctk  
from CTkXYFrame import *
from tkinter import messagebox as mgbx
from PIL import Image as pImg
from PIL import ImageTk

# Import classes which have the idividual screens to navigate through
from GeneralRecordsUI import GeneralRecordsUI
from SalesRecordsUI import SalesRecordsUI
from SettingsUI import SettingsUI 

# Second window that launches on startup, is a hub that navigates through screens containing 
# the programs main functionalities
class GeneralViewUI(tk.Tk):
    # Class constructor for main screen, creates gui components and intializes window
    def __init__(self, login, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Attribute to store reference to previous login window 
        self.LoginWin = login
        
        # Allows program to terminate properly on exit
        self.protocol("WM_DELETE_WINDOW", lambda: self.quit())
        
        
        # Pre-defining Colors
        self.dark_green = "#29A165"
        self.darker_green = "#1E8350" 
        self.white = "#ffffff"        
        self.gray = "#F0F0F0"
        self.black = "#000000"
        
        # Storing image references and setting their sizes
        icon_img = "images\\logo.ico"
        logo_img_data = pImg.open("images\\ICON.png")
        logo_img_data = logo_img_data.resize((70, 69))
        logo_txt_data = pImg.open("images\\logo_text.png")
        logo_txt_data = logo_txt_data.resize((132, 22))
        records_img_data = pImg.open("images\\records_icon.png")
        records_img_data = records_img_data.resize((23, 23))
        sales_img_data = pImg.open("images\\sales_icon.png")
        sales_img_data = sales_img_data.resize((23, 23))
        settings_img_data = pImg.open("images\\settings_icon.png")
        settings_img_data = settings_img_data.resize((23, 23))
        acnt_img_data = pImg.open("images\\acnt_icon.png")
        acnt_img_data = acnt_img_data.resize((23, 23))
        
        # Set app title
        self.title("PrintLogix")
        # Set app size
        self.geometry("1920x1080")
        self.resizable(False,False) 
        self.state("zoomed")
        # Set app icon
        self.iconbitmap(icon_img)

        """Creating and placing actual widgets in general view window""" 
        # Creating frame on left to contain navigation buttons to switch between screens/windows
        self.sidebar_frame = tk.Frame(master=self, bg=self.dark_green,  width=195, height=650)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        
        # Creating label to store and display image of printlogix logo at top of sidebar
        logo_img = ImageTk.PhotoImage(master=self.sidebar_frame, image=logo_img_data)           
        self.logoImgLbl = tk.Label(master=self.sidebar_frame, image=logo_img, bd=0, bg=self.dark_green)
        self.logoImgLbl.image = logo_img
        self.logoImgLbl.pack(pady=(65, 0), anchor="center")
        # Creating label to store and display image of printlogix logo text at top of sidebar
        logo_txt = ImageTk.PhotoImage(master=self.sidebar_frame, image=logo_txt_data)
        self.logoTxtLbl = tk.Label(master=self.sidebar_frame, bd=0, image=logo_txt, bg=self.dark_green)
        self.logoTxtLbl.image = logo_txt
        self.logoTxtLbl.pack(pady=(20, 0), anchor="center")        
        
        # Button which switches the screen on the right to general records when clicked
        self.recordsBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoGenRecords, width=150, text="General", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.darker_green, anchor="w")
        self.recordsBtn.pack(anchor="center", ipady=5, ipadx=10, pady=(40, 0))
        recs_img = ImageTk.PhotoImage(master=self.recordsBtn, image=records_img_data)
        self.recordsBtn.configure(image=recs_img)
        
        # Button which switches the screen on the right to sales records when clicked
        self.salesBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoSalesRecords, width=150, text="Sales", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.darker_green, anchor="w")
        self.salesBtn.pack(anchor="center", ipady=5, ipadx=10, pady=(16, 0))
        sales_img = ImageTk.PhotoImage(master=self.salesBtn, image=sales_img_data)
        self.salesBtn.configure(image=sales_img)        
        
        # Button which switches the screen on the right to settings when clicked
        self.settingsBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoSettings, width=150, text="Settings", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.darker_green, anchor="w")
        self.settingsBtn.pack(anchor="center", ipady=5, ipadx=10, pady=(16, 0))
        settings_img = ImageTk.PhotoImage(master=self.settingsBtn, image=settings_img_data)
        self.settingsBtn.configure(image=settings_img)  
        
        # Button which returns the user to the login window when clicked
        self.accountBtn = ctk.CTkButton(master=self.sidebar_frame, command=self.NavigatetoLogin, text="Account", fg_color="transparent", font=("Arial Bold", 17), hover_color=self.gray, anchor="w")
        self.accountBtn.pack(anchor="center", ipady=5, pady=(345, 0))
        acnt_img = ImageTk.PhotoImage(master=self.accountBtn, image=acnt_img_data)
        self.accountBtn.configure(image=acnt_img)
        
        
        # Container/frame in which all available screens are displayed, located on the right of the sidebar       
        main_container = tk.Frame(master=self, bg=self.white)
        main_container.pack(side="left", fill="both", anchor="center", expand=True)        
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        # tell frame not to let its children control its size
        main_container.pack_propagate(0)
        
        # Stores the screens to be navigated to
        self.frames = {}
        # Cycles through available screens and creates parent-child relationship with each
        # screen and the main_container above they will be displayed in
        for F in (GeneralRecordsUI, SalesRecordsUI, SettingsUI):
            page_name = F.__name__
            frame = F(parent=main_container, controller=self)
            self.frames[page_name] = frame

            # Put all of the pages in the same location; the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # Setting the screen visible on startup to general records
        self.NavigatetoGenRecords()
        
        
    # Method changes the currently viewed screen/panel to the one containing the general records      
    def NavigatetoGenRecords(self):
        # Highlights the button corresponding to the currently selected screen, general records here
        self.recordsBtn.configure(fg_color=self.darker_green)        
        self.salesBtn.configure(fg_color=self.dark_green)
        self.settingsBtn.configure(fg_color=self.dark_green)
        
        frame = self.frames["GeneralRecordsUI"]        
        frame.tkraise()
           
    
    # Method changes the currently viewed screen/panel to the one containing the sales records 
    def NavigatetoSalesRecords(self):
        # Highlights the button corresponding to the currently selected screen, sales records here
        self.salesBtn.configure(fg_color=self.darker_green)
        self.recordsBtn.configure(fg_color=self.dark_green)
        self.settingsBtn.configure(fg_color=self.dark_green)
                        
        frame = self.frames["SalesRecordsUI"]
        frame.tkraise()
                
    
    # Method changes the currently viewed screen/panel to the one containing the program's settings
    def NavigatetoSettings(self):
        # Highlights the button corresponding to the currently selected screen, settings here
        self.settingsBtn.configure(fg_color=self.darker_green)
        self.recordsBtn.configure(fg_color=self.dark_green)
        self.salesBtn.configure(fg_color=self.dark_green)
        
        frame = self.frames["SettingsUI"]
        frame.tkraise()
    
    
    # Method allows user to return to the login screen
    def NavigatetoLogin(self):
        # Confirms with user that they intend to open the login window before doing so
        result = mgbx.askquestion("Return to Login", "Are you sure you want to return to \nthe login screen?")
        if result == 'yes':
            self.withdraw()
            self.LoginWin.wm_deiconify()
        
        
    # Method handles quitting properly instead of quitting without handling all screens
    def quit(self):
        self.LoginWin.destroy()
        self.destroy()
        