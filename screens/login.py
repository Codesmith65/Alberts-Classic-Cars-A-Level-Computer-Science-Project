import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .generic import GenericScreen
import screens
import pickle
from application import Application
from dataTypes.user import User
from dataTypes.staff import Staff

import colourPallet as pallet


class Login(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)
		
		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("nav.TEntry", background=pallet.bg2, highlightcolor=pallet.highlight)

		# Sets window title
		self.root.title("Albert's Classic Car - Login")
		
		# Creates frames
		self.leftFrame: tk.Frame = tk.Frame(self.root, bg=pallet.bg)
		self.rightFrame: tk.Frame = tk.Frame(self.root, bg=pallet.bg2)
		self.loginFrame: tk.Frame = tk.Frame(self.rightFrame, bg=pallet.bg2)
		
		# Creates widgets for ui
		self.companyLogo = tk.PhotoImage(file="assets/logo-large.png")
		self.companyLogoHomeLabel = tk.Label(self.leftFrame, bg=pallet.bg)

		self.loginTitleLabel: tk.Label = tk.Label(self.loginFrame, bg=pallet.bg2)
		self.usernameEntry: ttk.Entry = ttk.Entry(self.loginFrame, style="nav.TEntry")
		self.passwordEntry: ttk.Entry = ttk.Entry(self.loginFrame, style="nav.TEntry")
		self.loginButton: ttk.Button = ttk.Button(self.loginFrame, style="nav.TButton")
		self.forgotPasswordLabel: tk.Label = tk.Label(self.loginFrame, bg=pallet.bg2)


		# Configures widgets
		self.loginTitleLabel["text"] = "Login"
		self.loginTitleLabel["font"] = ("Helvetica", 40, "bold")
		self.loginButton["text"] = "Login"
		self.forgotPasswordLabel["text"] = "Forgot password? Contact admin."
		
		self.passwordEntry["show"] = "*"
		
		self.loginButton["command"] = self.login

		self.companyLogoHomeLabel["image"] = self.companyLogo
		self.companyLogoHomeLabel["width"] = 500
		self.companyLogoHomeLabel["height"] = 500


		# Places widgets on UI
		self.leftFrame.pack(fill="both", expand=1, side="left")
		self.rightFrame.pack(fill="y", side="right")
		self.loginFrame.grid(row=0, column=0, sticky="")
		self.rightFrame.grid_rowconfigure(0, weight=1)
		self.rightFrame.grid_columnconfigure(0, weight=1)
		
		self.companyLogoHomeLabel.grid(row=0, column=0)
		self.leftFrame.grid_rowconfigure(0, weight=1)
		self.leftFrame.grid_columnconfigure(0, weight=1)

		self.loginTitleLabel.pack(padx=5, pady=20)
		self.usernameEntry.pack(padx=5, pady=1)
		self.passwordEntry.pack(padx=5, pady=1)
		self.loginButton.pack(padx=5, pady=1)
		self.forgotPasswordLabel.pack(padx=50, pady=1)
	
	# Used to log the user in
	def login(self) -> None:
		# Gets the entered username and password
		username: str = self.usernameEntry.get()
		password: str = self.passwordEntry.get()
		
		# Opnes the users and staff data files to get data
		users: list[User] = []
		staffs: list[Staff] = []
		with open("data/users.pkl", "rb") as userFile:
			users = pickle.load(userFile)
		
		with open("data/staff.pkl", "rb") as staffFile:
			staffs = pickle.load(staffFile)
		
		# Loops through every user and checks the credentials of the user if they dont match continue otherwise check the staff to find the associated staff member to the user
		for user in users:
			if not user.checkCredentials(username, password):
				continue

			for staff in staffs:
				if staff.userID == user.userID:
					self.application.setLoggedInStaff(staff.staffID)
			
			# Sets the loged in user and takes to the home screen
			self.application.setLoggedInUser(user.userID)
			self.application.switchForm(screens.Home)
			return
		
		# Shows a error if user name or password incorect
		messagebox.showwarning("Incorect username or password", "The username or password is incorrect, please ensure that the details are correct")
