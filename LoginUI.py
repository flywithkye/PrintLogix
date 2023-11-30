import tkinter as tk
import customtkinter as ctk  
from tkinter import messagebox as mgbx
from PIL import ImageTk
from PIL import Image as pImg

import GeneralViewUI as genUI

class LoginUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol("WM_DELETE_WINDOW", lambda: self.quit())
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        error_red = "#FF0000"
        white = "#ffffff"          
        gray = "#EEEEEE"
        dark_gray = "#7E7E7E"
        black = "#000000"        
        
        # Images
        icon_img = "images\\logo.ico"
        login_img = pImg.open("images\\login-side.jpg")
        email_img = pImg.open("images\\email-icon.png")
        email_img = email_img.resize((20, 20))
        password_img = pImg.open("images\\password-icon.png")
        password_img = password_img.resize((22,22))
        
        # Turn images to Ctk type images and establish size
        loginside_img = ImageTk.PhotoImage(image=login_img)        
        email_icon = ImageTk.PhotoImage(image= email_img)        
        password_icon = ImageTk.PhotoImage(image= password_img)
        
        
        # Set app size
        self.geometry("615x480")
        # Make app not resizable
        self.resizable(0,0) 
        # Set app title
        self.title("Welcome To PrintLogix") 
        # Set app icon
        self.iconbitmap(icon_img)
        
        # Placing login side pic
        self.loginpicLbl = tk.Label(master=self, image=loginside_img, bd=0)  
        self.loginpicLbl.image = loginside_img      
        self.loginpicLbl.pack(side="left")        
            
        # Create Frame
        self.mainFrame = tk.Frame(master=self, width=320, height=480, bg=white)
        self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(side="right")

        # Displayed elements
        self.welcomeLbl = tk.Label(master=self.mainFrame, text="Welcome.", bg=white, fg=dark_green, anchor="w", justify="left", font=("Arial Bold", 20)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        self.loginLbl = ctk.CTkLabel(master=self.mainFrame, text="Sign up or Login to your account\nbelow.", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 15)).pack(anchor="w", padx=(29, 0))

        self.userLbl = tk.Label(master=self.mainFrame, text="Username:", bg=white, fg=dark_green, anchor="w", justify="left", font=("Arial Bold", 12), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(5, 0))
        self.userInput = ctk.CTkEntry(master=self.mainFrame, width=250, fg_color="#EEEEEE", border_color=darker_green, border_width=1, text_color="#000000")
        self.userInput.pack(anchor="w", padx=(30, 17))

        self.passLbl = tk.Label(master=self.mainFrame, text="Password:",  bg=white, fg=dark_green, anchor="w", justify="left", font=("Arial Bold", 12), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(5, 0))
        self.passInput = ctk.CTkEntry(master=self.mainFrame, width=250, fg_color="#EEEEEE", border_color=darker_green, border_width=1, text_color="#000000", show="*")
        self.passInput.pack(anchor="w", padx=(30, 17))
        
        self.errorLbl = tk.Label(master=self.mainFrame, text="",  bg=white, fg=error_red, anchor="w", justify="left", font=("Arial", 12), compound="left")
        self.errorLbl.pack(anchor="w", pady=(10, 0), padx=(30, 15))
        print(self.errorLbl)
        
        # Login Button
        self.loginBtn = ctk.CTkButton(master=self.mainFrame, text="Login", width=250, fg_color=dark_green, hover_color=darker_green, font=("Arial Bold", 15), text_color="#ffffff", command=self.OpenGeneralView)
        self.loginBtn.pack(anchor="w", pady=(5, 0), padx=(30, 0))
        
        self.signUpBtn = ctk.CTkButton(master=self.mainFrame, text="Sign Up", width=250, fg_color=dark_green, hover_color=darker_green, font=("Arial Bold", 15), text_color="#ffffff", command=self.OpenGeneralView)
        self.signUpBtn.pack(anchor="w", pady=(20, 0), padx=(30, 0))
        
        self.genUI = None

    def show_msg(self):
        #should call authenticate user which with invoke authorize use depending on the account
        self.errorLbl.config(text = 'Please Enter a Valid Username & \nPassword')
        mgbx.showinfo("Message","Hey There! I hope you are doin','g well.")
        
    def OpenGeneralView(self):       
        if self.genUI is None or not self.genUI.winfo_exists():           
            self.withdraw()
            self.genUI = genUI.GeneralViewUI(self)             

        else:          
            self.withdraw()
            self.genUI.wm_deiconify()
            self.genUI.state("zoomed")
            self.genUI.focus()  # if window exists focus it

    
    def quit(self):
        if self.genUI is not None:              
            self.genUI.destroy()
        self.destroy()
             

            
   
            
        """
            try:
                self.withdraw()
                self.genUI.focus()  # if window exists focus it
            except Exception:
                pass  
        """
        
        """if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = genUI.GeneralViewUI()  # create window if its None or destroyed
            #
        else:
            self.toplevel_window.focus()  # if window exists focus it"""


if __name__ == "__main__":
    app = LoginUI()    
    app.mainloop()


    