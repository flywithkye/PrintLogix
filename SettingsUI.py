# Importing modules/libraries to build gui elements
import customtkinter as ctk  
from CTkTable import CTkTable as ctkt
from CTkXYFrame import *
import tkinter as tk
from PIL import Image as pImg
from PIL import ImageTk

# settings screen that is displayed when selected using sidebar in GeneralViewUI
class SettingsUI(tk.Frame):
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
        
        # Container/frame in which all widgets are displayed  
        self.main_view = tk.Frame(self, bg=white)
        self.main_view.pack(anchor="n", side="top", fill="x")
        # Container/frame in which the title is displayed  
        self.title_frame = tk.Frame(master=self.main_view, bg=white)
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(24, 0))

        # Creating label to store and display title of the screen
        self.genTitleLbl = ctk.CTkLabel(master=self.title_frame, width=50, text="Settings", fg_color=white, font=("Arial Black", 24), text_color=dark_green)
        self.genTitleLbl.pack(anchor="n")   
        
        # Container/frame to contain widgets to adjust the settings for the program
        self.view = tk.Frame(self, bg=gray)
        self.view.pack(anchor="s", side="bottom", fill="both", expand=True, padx=20, pady=20)
     
              
   