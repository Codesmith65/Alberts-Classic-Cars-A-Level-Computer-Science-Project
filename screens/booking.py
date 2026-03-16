from datetime import datetime, date
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox

from .generic import GenericScreen
from application import Application

from dataTypes.booking import Booking as BookingDataType
from uuid import UUID, uuid4

import os.path
import pickle

import screens
import popups


class Booking(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		#Creating witgets and seting window title
		self.root.title("Albert's Classic Car - Booking")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLable = tk.Label(self.topBarFrame)
		self.logOutButton = ttk.Button(self.topBarFrame)
		
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


		#Configuring the widgets
		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 100
		self.companyLogoHomeButton["height"] = 100

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
		
		self.logOutButton["command"] = self.logout

		self.bookButton["text"] = "Create Booking"
		
		self.pickUpDateLabelFrame["text"] = "Pickup Date"
		self.dropOffDateLabelFrame["text"] = "Drop off Date"
		
		self.companyLogoHomeButton["command"] = self.goHome
		self.bookButton["command"] = self.createBooking
		
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


		#Placing the widgest on the GUI
		self.topBarFrame.pack(fill="x")
		self.mainContectFrame.pack()

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLable.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
		
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
		
	
	#Takes the uses back to the home screen
	def goHome(self) -> None:
		self.application.switchForm(screens.Home)
	
	#Logsout the user and takes them to the login screen
	def logout(self) -> None:
		self.application.setLoggedInUser(None)
		self.application.setLoggedInStaff(None)
		self.application.switchForm(screens.Login)
	
	#Complets validation and then creates a booking if they check out
	def createBooking(self) -> None:
		#Validates if the client id is populated
		clientID = self.clientEntryStringVar.get()
		if clientID == "":
			messagebox.showwarning("Client ID", "Client ID not populated, please enter a client ID.")
			return
		
		#Validates weather vehicle id is populated
		vehicleID = self.vehicleEntryStringVar.get()
		if vehicleID == "":
			messagebox.showwarning("Vehicle ID", "Vehicle ID not populated, please enter a vehicle ID")
			return
		
		#Validates if the pick up date is proveded and a valid date
		pickUpDay = self.pickUpDay.get()
		pickUpMonth = self.pickUpMonth.get()
		pickUpYear = self.pickUpYear.get()

		try:
			pickUpDate = datetime.fromisoformat(f"{pickUpYear}-{pickUpMonth}-{pickUpDay}")
		except ValueError as e:
			messagebox.showwarning("Pick up date", str(e))
			return
		
		#Validates if the drop off date is proveded and a valid date
		dropOffDay = self.dropOffDay.get()
		dropOffMonth = self.dropOffMonth.get()
		dropOffYear = self.dropOffYear.get()

		try:
			dropOffDate = datetime.fromisoformat(f"{dropOffYear}-{dropOffMonth}-{dropOffDay}")
		except ValueError as e:
			messagebox.showwarning("Drop off date", str(e))
			return
		
		#Checks that the pick update is before teh drop off date
		if pickUpDate > dropOffDate:
			messagebox.showwarning("Pick up and drop off", "Pick up date can't be after drop off date")
			return
	
		#Creates the booking
		booking = BookingDataType(self.application.loggedInStaff, UUID(clientID), UUID(vehicleID), int(pickUpDate.timestamp()), uuid4(), int(dropOffDate.timestamp()), uuid4()) #Currently location id randomised
		
		#Checks if the booking file exists and if so loads the current bookings
		if os.path.isfile("data/bookings.pkl"):
			with open("data/bookings.pkl", "rb") as bookingFile:
				bookings = pickle.load(bookingFile)
		else:
			bookings = []

		bookings.append(booking)

		#Saves the bookings to the file
		with open("data/bookings.pkl", "wb") as bookingFile:
			pickle.dump(bookings, bookingFile)
		
		#Switches form and adds the booking id to the cross screen data
		self.application.switchForm(screens.Invoice, {"BookingID": booking.bookingID})
	
	#Shows a search screen for a cliet
	def __clientSearch(self) -> None:
		searchScreen = popups.SearchPopup(2)
		searchScreen.topLevel.protocol("WM_DELETE_WINDOW", lambda popup=searchScreen, stringVar=self.clientEntryStringVar: self.__clsoeSerachPopup(popup, stringVar))
	
	#Shows a search window for a vehicle
	def __vehicleSearch(self) -> None:
		searchScreen = popups.SearchPopup(4)
		searchScreen.topLevel.protocol("WM_DELETE_WINDOW", lambda popup=searchScreen, stringVar=self.vehicleEntryStringVar: self.__clsoeSerachPopup(popup, stringVar))
	
	#Closes the popup search screen an sets the selected value to teh field
	def __clsoeSerachPopup(self, popup: popups.SearchPopup, stringVar: tk.StringVar):
		serachResultData = popup.selctedData
		if serachResultData == {}:
			messagebox.showerror("No result selected", "No search result was selcted")
			popup.topLevel.destroy()
			return

		stringVar.set(str(serachResultData["id"]))
		popup.topLevel.destroy()