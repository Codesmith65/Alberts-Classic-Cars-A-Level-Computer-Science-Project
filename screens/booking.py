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


import colourPallet as pallet


class Booking(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)
		
		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("generic.TEntry", background=pallet.bg, highlightcolor=pallet.highlight)
		style.configure("generic.TCombobox", background=pallet.bg, highlightcolor=pallet.highlight)

		#Creating witgets and seting window title
		self.root.title("Albert's Classic Car - Booking")

		# Creates the frames and widgets for the UI
		self.topBarFrame = tk.Frame(self.root, bg=pallet.bg2)
		self.mainContectFrame = tk.Frame(self.root, bg=pallet.bg)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.searchIcon = tk.PhotoImage(file="assets/serach.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame, bg=pallet.bg2)
		self.titleLable = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.logOutButton = ttk.Button(self.topBarFrame, style="nav.TButton")
		
		self.bookingInfoContainer = tk.Frame(self.mainContectFrame, bg=pallet.bg)
		self.clientIDContainer = tk.Frame(self.bookingInfoContainer, bg=pallet.bg)
		self.vehicleIDContainer = tk.Frame(self.bookingInfoContainer, bg=pallet.bg)
		self.pickUpDateLabelFrame = tk.LabelFrame(self.bookingInfoContainer, bg=pallet.bg)
		self.dropOffDateLabelFrame = tk.LabelFrame(self.bookingInfoContainer, bg=pallet.bg)
		
		self.clientLabel = tk.Label(self.clientIDContainer, bg=pallet.bg)
		self.clientEntry = ttk.Entry(self.clientIDContainer, style="generic.TEntry")
		self.clientSearch = ttk.Button(self.clientIDContainer, style="generic.TButton")
		
		self.vehicleLabel = tk.Label(self.vehicleIDContainer, bg=pallet.bg)
		self.vehicleEntry = ttk.Entry(self.vehicleIDContainer, style="generic.TEntry")
		self.vehicleSearch = ttk.Button(self.vehicleIDContainer, style="generic.TButton")
		
		self.clientEntryStringVar: tk.StringVar = tk.StringVar()
		self.vehicleEntryStringVar: tk.StringVar = tk.StringVar()
		
		self.pickUpDay: ttk.Combobox = ttk.Combobox(self.pickUpDateLabelFrame, style="generic.TCombobox", width=5)
		self.pickUpMonth: ttk.Combobox = ttk.Combobox(self.pickUpDateLabelFrame, style="generic.TCombobox", width=5)
		self.pickUpYear: ttk.Combobox = ttk.Combobox(self.pickUpDateLabelFrame, style="generic.TCombobox", width=5)
		
		self.dropOffDay: ttk.Combobox = ttk.Combobox(self.dropOffDateLabelFrame, style="generic.TCombobox", width=5)
		self.dropOffMonth: ttk.Combobox = ttk.Combobox(self.dropOffDateLabelFrame, style="generic.TCombobox", width=5)
		self.dropOffYear: ttk.Combobox = ttk.Combobox(self.dropOffDateLabelFrame, style="generic.TCombobox", width=5)
		
		self.bookButton = ttk.Button(self.bookingInfoContainer, style="generic.TButton")


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
		self.clientSearch["image"] = self.searchIcon
		self.clientSearch["command"] = self.__clientSearch
		self.vehicleLabel["text"] = "Vehicle"
		self.vehicleSearch["image"] = self.searchIcon
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
		self.mainContectFrame.pack(fill="both", expand=1)
		self.bookingInfoContainer.grid(row=0, column=0)
		
		self.clientIDContainer.grid(row=0, column=0, padx=5, pady=10)
		self.vehicleIDContainer.grid(row=0, column=1, padx=5, pady=10)

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLable.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
		
		self.clientLabel.grid(row=0, column=0, padx=1)
		self.clientEntry.grid(row=0, column=1, padx=1)
		self.clientSearch.grid(row=0, column=2, padx=1)
		
		self.vehicleLabel.grid(row=0, column=0, padx=1)
		self.vehicleEntry.grid(row=0, column=1, padx=1)
		self.vehicleSearch.grid(row=0, column=2, padx=1)

		self.pickUpDay.grid(row=0, column=0, padx=1, pady=1)
		self.pickUpMonth.grid(row=0, column=1, padx=1, pady=1)
		self.pickUpYear.grid(row=0, column=2, padx=1, pady=1)
		
		self.dropOffDay.grid(row=0, column=0, padx=1, pady=1)
		self.dropOffMonth.grid(row=0, column=1, padx=1, pady=1)
		self.dropOffYear.grid(row=0, column=2, padx=1, pady=1)
		
		self.pickUpDateLabelFrame.grid(row=1, column=0)
		self.dropOffDateLabelFrame.grid(row=1, column=1)

		self.bookButton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
		
		self.mainContectFrame.grid_rowconfigure(0, weight=1)
		self.mainContectFrame.columnconfigure(0, weight=1)

		self.bookingInfoContainer.grid_rowconfigure(0, weight=1)
		self.bookingInfoContainer.grid_rowconfigure(1, weight=1)
		self.bookingInfoContainer.grid_rowconfigure(2, weight=1)
		self.bookingInfoContainer.grid_columnconfigure(0, weight=1)
		self.bookingInfoContainer.grid_columnconfigure(1, weight=1)
		
	
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