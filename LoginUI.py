# Importing modules/libraries to build gui elements
import tkinter as tk
import customtkinter as ctk  
from tkinter import messagebox as mgbx
from PIL import ImageTk
from PIL import Image as pImg

# Import class which has the main program window 
import GeneralViewUI as genUI

# First screen that launches on startup, allows for login and sign up and authentication
class LoginUI(tk.Tk):
    # Class constructor for login screen, creates gui components and intializes window
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Attribute to store reference to main program window 
        self.genUI = None     
        
        # An account for login testing
        self.username = "admin1234"
        self.password = "testtest123"   
        
        # Allows program to terminate properly on exit
        self.protocol("WM_DELETE_WINDOW", lambda: self.quit())    
        
        
        # Pre-defining Colors
        dark_green = "#29A165"
        darker_green = "#1E8350" 
        error_red = "#FF0000"
        white = "#ffffff"          
        gray = "#EEEEEE"
        dark_gray = "#7E7E7E"
        black = "#000000"        
        
        # Storing image references and setting their sizes
        icon_img = "images\\logo.ico"
        login_img = pImg.open("images\\login-side.jpg")
        email_img = pImg.open("images\\email-icon.png")
        email_img = email_img.resize((20, 20))
        password_img = pImg.open("images\\password-icon.png")
        password_img = password_img.resize((22,22))
        
        # Turn images to Tk type images
        loginside_img = ImageTk.PhotoImage(image=login_img)        
        email_icon = ImageTk.PhotoImage(image= email_img)        
        password_icon = ImageTk.PhotoImage(image= password_img)
        
        
        # Set login window size
        self.geometry("615x480")
        # Make login window not resizable
        self.resizable(False,False) 
        # Set login window title
        self.title("Welcome To PrintLogix") 
        # Set login window icon to PrintLogix icon
        self.iconbitmap(icon_img)
        
        
        """Creating and placing actual widgets in login window"""        
        # Placing login side picture to the left
        self.loginpicLbl = tk.Label(master=self, image=loginside_img, bd=0)  
        self.loginpicLbl.image = loginside_img      
        self.loginpicLbl.pack(side="left")        
            
        # Create frame to right where text, text entries and buttons are displayed
        self.mainFrame = tk.Frame(master=self, width=320, height=480, bg=white)
        self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(side="right")

        # Creating labels and input boxes for login attempts
        self.welcomeLbl = tk.Label(master=self.mainFrame, text="Welcome.", bg=white, fg=dark_green, anchor="w", justify="left", font=("Arial Bold", 20)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        self.loginLbl = ctk.CTkLabel(master=self.mainFrame, text="Sign up or Login to your account\nbelow.", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 15)).pack(anchor="w", padx=(29, 0))

        self.userLbl = tk.Label(master=self.mainFrame, text="Username:", bg=white, fg=dark_green, anchor="w", justify="left", font=("Arial Bold", 12), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(5, 0))
        self.userInput = ctk.CTkEntry(master=self.mainFrame, width=250, fg_color="#EEEEEE", border_color=darker_green, border_width=1, text_color="#000000")
        self.userInput.pack(anchor="w", padx=(30, 17))

        self.passLbl = tk.Label(master=self.mainFrame, text="Password:",  bg=white, fg=dark_green, anchor="w", justify="left", font=("Arial Bold", 12), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(5, 0))
        self.passInput = ctk.CTkEntry(master=self.mainFrame, width=250, fg_color="#EEEEEE", border_color=darker_green, border_width=1, text_color="#000000", show="*")
        self.passInput.pack(anchor="w", padx=(30, 17))
        
        # Used to display error messages below username and password input
        self.errorLbl = tk.Label(master=self.mainFrame, text="",  bg=white, fg=error_red, anchor="w", justify="left", font=("Arial", 12), compound="left")
        self.errorLbl.pack(anchor="w", pady=(10, 0), padx=(30, 15))
        print(self.errorLbl)
        
        # Houses button widgets
        self.buttonframe = tk.Frame(master=self.mainFrame, bg=white)
        self.buttonframe.pack(anchor="w", pady=(5, 0), padx=(30, 0))
        
        # Creating login Button that when clicked will run a method which launches the main screen if user info is valid
        self.loginBtn = ctk.CTkButton(master=self.buttonframe, text="Login", command=self.OpenGeneralView, width=115, fg_color=dark_green, hover_color=darker_green, font=("Arial Bold", 15), text_color="#ffffff")
        self.loginBtn.pack(side="left", pady=5, padx=(0,10))
        
        # Creating sign up Button that when clicked should run a method which launches a sign up screen to collect details for sign up
        self.signUpBtn = ctk.CTkButton(master=self.buttonframe, text="Sign Up", command=self.OpenGeneralView, width=115, fg_color=dark_green, hover_color=darker_green, font=("Arial Bold", 15), text_color="#ffffff")
        self.signUpBtn.pack(side="left", pady=5, padx=(10,0))
        
       
    # Method that should check for validity and authorize the user then launch the main program window
    def OpenGeneralView(self):   
        # Here should authenticate user which should authorize user depending on the account role/type
        
        if self.userInput.get() == "" or self.passInput.get() == "":
            self.errorLbl.config(text = 'Please Enter a Valid Username & \nPassword')
        elif self.userInput.get() != self.username or self.passInput.get() != self.password:
            self.errorLbl.config(text = 'Account does not exist. Please \ntry again.')
        else: 
            # Does a check to see the window was already created, navigating to it if it is
            # and creating it if it was not
            if self.genUI is None or not self.genUI.winfo_exists():           
                self.withdraw()
                self.genUI = genUI.GeneralViewUI(self)             

            else:          
                self.withdraw()
                self.genUI.wm_deiconify()
                self.genUI.state("zoomed")
                self.genUI.focus()  # if window exists focus it



    # Method handles quitting properly instead of quitting without handling all screens
    def quit(self):
        if self.genUI is not None:              
            self.genUI.destroy()
        self.destroy()
             

# Main driver for program
if __name__ == "__main__":
    app = LoginUI()    
    app.mainloop()


    