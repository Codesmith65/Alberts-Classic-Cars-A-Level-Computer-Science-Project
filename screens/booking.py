from sqlite3 import enable_callback_tracebacks
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox

from .generic import GenericScreen
from application import Application

import screens
import popups


class Booking(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Booking")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLable = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.clientLabel = tk.Label(self.mainContectFrame)
		self.clientEntry = tk.Entry(self.mainContectFrame)
		self.clientSearch = tk.Button(self.mainContectFrame)
		
		self.vehicleLabel = tk.Label(self.mainContectFrame)
		self.vehicleEntry = tk.Entry(self.mainContectFrame)
		self.vehicleSearch = tk.Button(self.mainContectFrame)
		
		self.clientEntryStringVar = tk.StringVar()
		
		self.pickUpDateLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.dropOffDateLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		self.bookButton = tk.Button(self.mainContectFrame)
		
		self.testButton1 = tk.Button(self.pickUpDateLabelFrame, text="test")
		self.testButton1.pack()
		self.testButton1 = tk.Button(self.dropOffDateLabelFrame, text="test")
		self.testButton1.pack()


		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 50
		self.companyLogoHomeButton["height"] = 50

		self.companyLogoHomeButton["text"] = "logo"
		self.titleLable["text"] ="Booking"
		self.titleLable["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.clientEntry["textvariable"] = self.clientEntryStringVar
		
		self.clientLabel["text"] = "Client"
		self.clientSearch["text"] = "s"
		self.clientSearch["command"] = self.__clientSearch
		self.vehicleLabel["text"] = "Vehicle"
		self.vehicleSearch["text"] = "s"
		
		self.pickUpDateLabelFrame["text"] = "Pickup Date"
		self.dropOffDateLabelFrame["text"] = "Drop off Date"
		
		self.companyLogoHomeButton["command"] = self.goHome


		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoHomeButton.pack()
		self.titleLable.pack()
		self.logOutButton.pack()
		
		self.clientLabel.pack()
		self.clientEntry.pack()
		self.clientSearch.pack()
		
		self.vehicleLabel.pack()
		self.vehicleEntry.pack()
		self.vehicleSearch.pack()
		
		self.pickUpDateLabelFrame.pack()
		self.dropOffDateLabelFrame.pack()

		self.mainContectFrame.pack()
	
	def goHome(self) -> None:
		self.application.switchForm(screens.Home)
	
	def __clientSearch(self) -> None:
		searchScreen = popups.SearchPopup(1)
		
		searchScreen.topLevel.protocol("WM_DELETE_WINDOW", lambda popup=searchScreen, stringVar=self.clientEntryStringVar: self.__clsoeSerachPopup(popup, stringVar))
	
	def __clsoeSerachPopup(self, popup: popups.SearchPopup, stringVar: tk.StringVar):
		serachResultData = popup.selctedData
		if serachResultData == {}:
			messagebox.showerror("No result selected", "No search result was selcted")
			popup.topLevel.destroy()
			return

		stringVar.set(str(serachResultData["id"]))
		popup.topLevel.destroy()