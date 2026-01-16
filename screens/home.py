import tkinter as tk
from tkinter import NO, ttk
from .generic import GenericScreen
from application import Application
import screens

class Home(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Home")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)
		self.navigationButtonsFrame = tk.Frame(self.mainContectFrame)

		self.companyLogo = tk.PhotoImage
		self.companyLogoLabel = tk.Label(self.topBarFrame)
		self.titleLable = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)

		self.searchButton = tk.Button(self.navigationButtonsFrame)
		self.bookingButton = tk.Button(self.navigationButtonsFrame)
		self.taskButton = tk.Button(self.navigationButtonsFrame)
		#TODO check if account should see this
		self.accountsButton = tk.Button(self.navigationButtonsFrame)


		self.searchButton["text"] = "Search"
		self.bookingButton["text"] = "Create Booking"
		self.taskButton["text"] = "Tasks"

		self.companyLogoLabel["text"] = "logo"
		self.titleLable["text"] ="Home"
		self.titleLable["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.logOutButton["command"] = self.logout
		self.searchButton["command"] = self.openSearch
		self.bookingButton["command"] = self.openBooking
		self.taskButton["command"] = self.openTasks
		self.accountsButton["command"] = self.openAccounts


		self.topBarFrame.pack()
		self.mainContectFrame.pack()
		self.navigationButtonsFrame.pack()

		self.searchButton.grid(row=0, column=0)
		self.bookingButton.grid(row=0, column=1)
		self.taskButton.grid(row=0, column=2)
		self.accountsButton.grid(row=1, column=1)

		self.companyLogoLabel.pack()
		self.titleLable.pack()
		self.logOutButton.pack()
	
	def logout(self) -> None:
		self.application.setLoggedInUser(None)
		self.application.switchForm(screens.Login)
	
	def openSearch(self) -> None:
		self.application.switchForm(screens.Search)
		
	def openBooking(self) -> None:
		self.application.switchForm(screens.Booking)
		
	def openTasks(self) -> None:
		self.application.switchForm(screens.Task)
		
	def openAccounts(self) -> None:
		self.application.switchForm(screens.Account)