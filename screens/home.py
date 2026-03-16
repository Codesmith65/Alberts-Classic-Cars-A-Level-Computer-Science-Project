import tkinter as tk
from tkinter import messagebox, ttk
from .generic import GenericScreen
from application import Application
import screens
import pickle

from dataTypes.user import User


class Home(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Home")

		# Opens user file and gets all users
		with open("data/users.pkl", "br") as userFile:
			users: list[User] = pickle.load(userFile)
		
		# Searches through users to find logged in user
		currentUser: User|None = None
		for user in users:
			if user.userID == self.application.logedInUser:
				currentUser = user
				break
		
		# Checks if the user logged in exists, should never run
		if currentUser is None:
			messagebox.showerror("Logged in user", "The user logged in is not found in the user file, logging out")
			application.switchForm(screens.Login)
			return

		self.topBarFrame = tk.Frame(self.root, background="red")
		self.mainContectFrame = tk.Frame(self.root)
		self.navigationButtonsFrame = tk.Frame(self.mainContectFrame)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Label(self.topBarFrame)
		self.titleLable = tk.Label(self.topBarFrame)
		self.logOutButton = ttk.Button(self.topBarFrame)

		self.searchButton = tk.Button(self.navigationButtonsFrame)
		self.bookingButton = ttk.Button(self.navigationButtonsFrame)
		self.taskButton = ttk.Button(self.navigationButtonsFrame)
		if currentUser.admin:
			self.accountsButton = ttk.Button(self.navigationButtonsFrame, text="Accounts", command=self.openAccounts)


		self.searchButton["text"] = "Search"
		self.searchButton["width"] = 10
		self.searchButton["height"] = 10
		
		self.bookingButton["text"] = "Create Booking"
		self.taskButton["text"] = "Tasks"

		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["width"] = 100
		self.companyLogoHomeButton["height"] = 100

		self.titleLable["text"] ="Home"
		self.titleLable["font"] = ("Helvetica", 40, "bold")
		self.logOutButton["text"] = "Logout"
		
		self.logOutButton["command"] = self.logout
		self.searchButton["command"] = self.openSearch
		self.bookingButton["command"] = self.openBooking
		self.taskButton["command"] = self.openTasks


		self.topBarFrame.pack(fill="x")
		self.mainContectFrame.pack(expand=1)
		self.navigationButtonsFrame.pack()

		self.searchButton.grid(row=0, column=0)
		self.bookingButton.grid(row=0, column=1)
		self.taskButton.grid(row=0, column=2)
		if currentUser.admin:
			self.accountsButton.grid(row=1, column=1)

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLable.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)
		
		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
	
	def logout(self) -> None:
		self.application.setLoggedInUser(None)
		self.application.setLoggedInStaff(None)
		self.application.switchForm(screens.Login)
	
	def openSearch(self) -> None:
		self.application.switchForm(screens.Search)
		
	def openBooking(self) -> None:
		self.application.switchForm(screens.Booking)
		
	def openTasks(self) -> None:
		self.application.switchForm(screens.Task)
		
	def openAccounts(self) -> None:
		self.application.switchForm(screens.Account)