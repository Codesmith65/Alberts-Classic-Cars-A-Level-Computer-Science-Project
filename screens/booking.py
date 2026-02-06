from datetime import datetime
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
		
		self.clientEntryStringVar: tk.StringVar = tk.StringVar()
		self.vehicleEntryStringVar: tk.StringVar = tk.StringVar()
		
		self.pickUpDateLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.dropOffDateLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		self.pickUpDay: ttk.Combobox = ttk.Combobox(self.pickUpDateLabelFrame)
		self.pickUpMonth: ttk.Combobox = ttk.Combobox(self.pickUpDateLabelFrame)
		self.pickUpYear: ttk.Combobox = ttk.Combobox(self.pickUpDateLabelFrame)
		
		self.dropOffDay: ttk.Combobox = ttk.Combobox(self.dropOffDateLabelFrame)
		self.dropOffMonth: ttk.Combobox = ttk.Combobox(self.dropOffDateLabelFrame)
		self.dropOffYear: ttk.Combobox = ttk.Combobox(self.dropOffDateLabelFrame)
		
		self.bookButton = tk.Button(self.mainContectFrame)


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
		self.vehicleEntry["textvariable"] = self.vehicleEntryStringVar
		
		self.clientLabel["text"] = "Client"
		self.clientSearch["text"] = "s"
		self.clientSearch["command"] = self.__clientSearch
		self.vehicleLabel["text"] = "Vehicle"
		self.vehicleSearch["text"] = "s"
		self.vehicleSearch["command"] = self.__vehicleSearch
		
		self.pickUpDateLabelFrame["text"] = "Pickup Date"
		self.dropOffDateLabelFrame["text"] = "Drop off Date"
		
		self.companyLogoHomeButton["command"] = self.goHome
		
		self.pickUpDay["state"] = "readonly"
		self.pickUpMonth["state"] = "readonly"
		self.pickUpYear["state"] = "readonly"
		
		self.dropOffDay["state"] = "readonly"
		self.dropOffMonth["state"] = "readonly"
		self.dropOffYear["state"] = "readonly"
		
		days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
		months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
		currentYear = current_year = datetime.now().year
		years = []
		for x in range(5):
			years.append(str(currentYear + x))
	
		self.pickUpDay["values"] = days
		self.pickUpMonth["values"] = months
		self.pickUpYear["values"] = years
		
		self.dropOffDay["values"] = days
		self.dropOffMonth["values"] = months
		self.dropOffYear["values"] = years


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

		self.pickUpDay.pack()
		self.pickUpMonth.pack()
		self.pickUpYear.pack()
		
		self.dropOffDay.pack()
		self.dropOffMonth.pack()
		self.dropOffYear.pack()
		
		self.pickUpDateLabelFrame.pack()
		self.dropOffDateLabelFrame.pack()

		self.bookButton.pack()
	
		self.mainContectFrame.pack()
		
	
	def goHome(self) -> None:
		self.application.switchForm(screens.Home)
	
	def __clientSearch(self) -> None:
		searchScreen = popups.SearchPopup(1)
		searchScreen.topLevel.protocol("WM_DELETE_WINDOW", lambda popup=searchScreen, stringVar=self.clientEntryStringVar: self.__clsoeSerachPopup(popup, stringVar))
	
	def __vehicleSearch(self) -> None:
		searchScreen = popups.SearchPopup(5)
		searchScreen.topLevel.protocol("WM_DELETE_WINDOW", lambda popup=searchScreen, stringVar=self.vehicleEntryStringVar: self.__clsoeSerachPopup(popup, stringVar))
	
	def __clsoeSerachPopup(self, popup: popups.SearchPopup, stringVar: tk.StringVar):
		serachResultData = popup.selctedData
		if serachResultData == {}:
			messagebox.showerror("No result selected", "No search result was selcted")
			popup.topLevel.destroy()
			return

		stringVar.set(str(serachResultData["id"]))
		popup.topLevel.destroy()