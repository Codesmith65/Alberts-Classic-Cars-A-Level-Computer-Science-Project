import tkinter as tk
from tkinter import messagebox, ttk
from .generic import GenericScreen
from application import Application
import screens
import pickle

from dataTypes.user import User

import colourPallet as pallet


class Home(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)
		
		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("highlight.TButton", background=pallet.bg, focuscolor=pallet.highlight)

		# Sets the window title
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

		# Creates the frames for the ui elements
		self.topBarFrame = tk.Frame(self.root, bg=pallet.bg2)
		self.mainContectFrame = tk.Frame(self.root, bg=pallet.bg)
		self.navigationButtonsFrame = tk.Frame(self.mainContectFrame, bg=pallet.bg)

		# Creates the widgets for the diffrent elements
		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeLabel = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.titleLable = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.logOutButton = ttk.Button(self.topBarFrame, style="nav.TButton")

		self.searchButton = ttk.Button(self.navigationButtonsFrame, style="highlight.TButton")
		self.bookingButton = ttk.Button(self.navigationButtonsFrame, style="highlight.TButton")
		self.taskButton = ttk.Button(self.navigationButtonsFrame, style="highlight.TButton")
		# Checks if the user is an admin, if so shows the account screen button
		if currentUser.admin:
			self.accountsButton = ttk.Button(self.navigationButtonsFrame, text="Accounts", command=self.openAccounts, style="highlight.TButton")


		# Configure the widgets for displaying
		self.searchButton["text"] = "Search"
		
		self.navigationButtonsFrame.grid_propagate(False)
		self.navigationButtonsFrame["width"] = 600
		self.navigationButtonsFrame["height"] = 400
		
		self.bookingButton["text"] = "Create Booking"
		self.taskButton["text"] = "Tasks"

		self.companyLogoHomeLabel["image"] = self.companyLogo
		self.companyLogoHomeLabel["width"] = 100
		self.companyLogoHomeLabel["height"] = 100

		self.titleLable["text"] ="Home"
		self.titleLable["font"] = ("Helvetica", 40, "bold")
		self.logOutButton["text"] = "Logout"
		
		self.logOutButton["command"] = self.logout
		self.searchButton["command"] = self.openSearch
		self.bookingButton["command"] = self.openBooking
		self.taskButton["command"] = self.openTasks


		# Displays the widgets on the UI
		self.topBarFrame.pack(fill="x")
		self.mainContectFrame.pack(expand=1, fill="both")
		self.navigationButtonsFrame.grid()

		self.mainContectFrame.grid_rowconfigure(0, weight=1)
		self.mainContectFrame.grid_columnconfigure(0, weight=1)

		self.searchButton.grid(row=0, column=0, sticky="nesw")
		self.bookingButton.grid(row=0, column=1, sticky="nesw")
		self.taskButton.grid(row=0, column=2, sticky="nesw")
		if currentUser.admin:
			self.accountsButton.grid(row=1, column=1, sticky="nesw")
		
		self.navigationButtonsFrame.grid_rowconfigure(0, weight=1)
		self.navigationButtonsFrame.grid_rowconfigure(1, weight=1)
		self.navigationButtonsFrame.grid_columnconfigure(0, weight=1)
		self.navigationButtonsFrame.grid_columnconfigure(1, weight=1)
		self.navigationButtonsFrame.grid_columnconfigure(2, weight=1)

		self.companyLogoHomeLabel.grid(row=0, column=0, sticky="w")
		self.titleLable.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)
		
		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
	
	# Used to log the user out and take them to the login screen
	def logout(self) -> None:
		self.application.setLoggedInUser(None)
		self.application.setLoggedInStaff(None)
		self.application.switchForm(screens.Login)
	
	# Used to take the user to the search screen
	def openSearch(self) -> None:
		self.application.switchForm(screens.Search)
	
	# Used to take the user to the booking screen
	def openBooking(self) -> None:
		self.application.switchForm(screens.Booking)
	
	# Used to take the user to the task screen
	def openTasks(self) -> None:
		self.application.switchForm(screens.Task)
	
	# Used to take the user to the accounts screen
	def openAccounts(self) -> None:
		self.application.switchForm(screens.Account)