import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .generic import GenericScreen
import screens
import pickle
from application import Application
from dataTypes.user import User
from dataTypes.staff import Staff


class Login(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Login")

		self.leftFrame: tk.Frame = tk.Frame(self.root)
		self.rightFrame: tk.Frame = tk.Frame(self.root)
		self.loginFrame: tk.Frame = tk.Frame(self.rightFrame)

		self.loginTitleLabel: tk.Label = tk.Label(self.loginFrame)
		self.usernameEntry: tk.Entry = tk.Entry(self.loginFrame)
		self.passwordEntry: tk.Entry = tk.Entry(self.loginFrame)
		self.loginButton: tk.Button = tk.Button(self.loginFrame)
		self.forgotPasswordLabel: tk.Label = tk.Label(self.loginFrame)


		self.loginTitleLabel["text"] = "Login"
		self.loginTitleLabel["font"] = ("Helvetica", 40)
		self.loginButton["text"] = "Login"
		self.forgotPasswordLabel["text"] = "Forgot password? Contact admin."
		
		self.passwordEntry["show"] = "*"
		
		self.loginButton["command"] = self.login


		self.rightFrame.pack()
		self.loginFrame.pack()

		self.loginTitleLabel.pack()
		self.usernameEntry.pack()
		self.passwordEntry.pack()
		self.loginButton.pack()
		self.forgotPasswordLabel.pack()
	
	def login(self) -> None:
		username: str = self.usernameEntry.get()
		password: str = self.passwordEntry.get()
		
		users: list[User] = []
		staffs: list[Staff] = []
		with open("data/users.pkl", "rb") as userFile:
			users = pickle.load(userFile)
		
		with open("data/staff.pkl", "rb") as staffFile:
			staffs = pickle.load(staffFile)
			
		for user in users:
			if not user.checkCredentials(username, password):
				continue

			for staff in staffs:
				if staff.userID == user.userID:
					self.application.setLoggedInStaff(staff.staffID)
			
			self.application.setLoggedInUser(user.userID)
			self.application.switchForm(screens.Home)
			return
		
		messagebox.showwarning("Incorect username or password", "The username or password is incorrect, please ensure that the details are correct")
