from math import exp
import tkinter as tk
from tkinter import ttk, messagebox
from turtle import color
from .generic import GenericScreen
from application import Application
from uuid import UUID
from datetime import datetime
from dataTypes.booking import Booking
from dataTypes.vehicle import Vehicle
import pickle
import screens

import colourPallet as pallet


class Invoice(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("generic.TEntry", background=pallet.bg, highlightcolor=pallet.highlight)
		style.configure("generic.TCombobox", background=pallet.bg, highlightcolor=pallet.highlight)

		#Creating wigets and setting window title
		self.root.title("Albert's Classic Car - Invoice")
		self.root.configure(bg=pallet.bg)

		# Create frames for UI
		self.topBarFrame = tk.Frame(self.root, bg=pallet.bg2)
		self.mainContectFrame = tk.Frame(self.root, bg=pallet.bg)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame, bg=pallet.bg2)
		self.titleLabel = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.logOutButton = ttk.Button(self.topBarFrame, style="nav.TButton")
		
		self.generalLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="General", bg=pallet.bg)
		self.vehicleLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="Vehicle", bg=pallet.bg)
		self.pickupAndDropoffLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="Pick up & Drop off", bg=pallet.bg)
		self.costLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="Cost", bg=pallet.bg)
		
		self.BookingIDLabel = tk.Label(self.generalLabelFrame, justify="left", bg=pallet.bg)
		self.statusLabel = tk.Label(self.generalLabelFrame, justify="left", bg=pallet.bg)
		
		self.pickUpLabel = tk.Label(self.pickupAndDropoffLabelFrame, justify="left", bg=pallet.bg)
		self.dropOffLabel = tk.Label(self.pickupAndDropoffLabelFrame, justify="left", bg=pallet.bg)

		self.vehicleIdLabel = tk.Label(self.vehicleLabelFrame, justify="left", bg=pallet.bg)
		self.vehicleNameLabel = tk.Label(self.vehicleLabelFrame, justify="left", bg=pallet.bg)
		self.vehicleColourLabel = tk.Label(self.vehicleLabelFrame, justify="left", bg=pallet.bg)
		self.vehicleRegistrationLabel = tk.Label(self.vehicleLabelFrame, justify="left", bg=pallet.bg)
		
		self.costPerDayLabel = tk.Label(self.costLabelFrame, justify="left", bg=pallet.bg)
		self.totalCostLabel = tk.Label(self.costLabelFrame, justify="left", bg=pallet.bg)
		self.depositeLabel = tk.Label(self.costLabelFrame, justify="left", bg=pallet.bg)
		self.depositeDueLabel = tk.Label(self.costLabelFrame, justify="left", bg=pallet.bg)
		self.balanceLabel = tk.Label(self.costLabelFrame, justify="left", bg=pallet.bg)
		self.balanceDueLabel = tk.Label(self.costLabelFrame, justify="left", bg=pallet.bg)


		#Checking weather a booking ID has been provided from previous screen
		if not "BookingID" in self.application.crossScreenDataStore:
			self.BookingIDLabel["text"] = "BookingID: No booking inputed"
			messagebox.showerror("Booking ID", "No booking ID has been passed to this form, try going back and reloading form, if persists contact administartor")
			return
		
		self.bookingID: UUID = self.application.crossScreenDataStore["BookingID"]
		self.booking: Booking|None = None
		self.vehicle: Vehicle|None = None

		#Loading bookings and searcing for specified one, handles errors where data is stored in incorcet form or the booking isnt found
		with open("data/bookings.pkl", "br") as bookingsFile:
			bookings: list[Booking] = pickle.load(bookingsFile)

			if type(bookings) is not list:
				messagebox.showerror("Booking data storage", "There is an issue with the storage of booking data, contact administartor")

			for booking in bookings:
				if booking.bookingID == self.bookingID:
					self.booking = booking
					break
			
			if self.booking is None:
				messagebox.showerror("Booking not found", "The requested booking was not found, please contact the administrator")
				return
		
		with open("data/vehicles.pkl", "br") as vehiclesFile:
			vehicles: list[Vehicle] = pickle.load(vehiclesFile)
			
			if type(vehicles) is not list:
				messagebox.showerror("Vehicles data storage", "There is an issue with the storage of vehicle data, contact administrator")

			for vehicle in vehicles:
				if vehicle.vehicleID == self.booking.vehicleID:
					self.vehicle = vehicle
					break
			
			if self.vehicle is None:
				messagebox.showerror("Vehicle not found", "The requested vehicle was not found, please contact the administrator")
				return
			
		#Calculates duration in days and how much itll cost
		bookingDuration = (self.booking.dropoffDate - self.booking.pickupDate) / 86400
		bookingCost = bookingDuration * self.vehicle.costPerDay #Cost of booking a car per day
		bookingDeposit = bookingCost * 0.1 #Deposite is 10% of booking cost
		bookingBalence = bookingCost - bookingDeposit


		#Configuring widgets to have correct infomation and functionality
		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 100
		self.companyLogoHomeButton["height"] = 100
		self.companyLogoHomeButton["command"] = self.__goHome
		self.logOutButton["command"] = self.logout
		
		self.companyLogoHomeButton["text"] = "logo"
		self.titleLabel["text"] ="Invoice"
		self.titleLabel["font"] = ("Helvetica", 40, "bold")
		self.logOutButton["text"] = "Logout"
		
		self.generalLabelFrame["font"] = ("Helvetica", 12, "bold")
		self.vehicleLabelFrame["font"] = ("Helvetica", 12, "bold")
		self.pickupAndDropoffLabelFrame["font"] = ("Helvetica", 12, "bold")
		self.costLabelFrame["font"] = ("Helvetica", 12, "bold")

		self.BookingIDLabel["text"] = f"BookingID: {self.bookingID}"
		self.statusLabel["text"] = f"Status: {self.booking.status}"
		
		self.pickUpLabel["text"] = f"Pickup: {datetime.fromtimestamp(self.booking.pickupDate):%d/%m/%Y}"
		self.dropOffLabel["text"] = f"Drop off: {datetime.fromtimestamp(self.booking.dropoffDate):%d/%m/%Y}"
		
		self.vehicleIdLabel["text"] = f"Vehicle ID: {self.vehicle.vehicleID}"
		self.vehicleNameLabel["text"] = f"Vehicle: {self.vehicle.make} {self.vehicle.model}"
		self.vehicleColourLabel["text"] = f"Colour: {self.vehicle.colour}"
		self.vehicleRegistrationLabel["text"] = f"Registration: {self.vehicle.registration}"
		
		self.costPerDayLabel["text"] = f"Cost per day: £{self.vehicle.costPerDay:.2f}"
		self.totalCostLabel["text"] = f"Total cost: £{bookingCost:.2f}"
		self.depositeLabel["text"] = f"Deposite: £{bookingDeposit:.2f}"
		self.depositeDueLabel["text"] = "Due:"
		self.balanceLabel["text"] = f"Balance: £{bookingBalence:.2f}"
		self.balanceDueLabel["text"] = "Due:"


		#Position widgets on gui
		self.topBarFrame.pack(fill="x")
		self.mainContectFrame.pack(expand=1)

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLabel.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
		
		self.generalLabelFrame.grid(row=0, column=0, sticky="w", padx=50, pady=10)
		self.vehicleLabelFrame.grid(row=1, column=0, sticky="w", padx=50, pady=10)
		self.pickupAndDropoffLabelFrame.grid(row=0, column=1, sticky="w", padx=50, pady=10)
		self.costLabelFrame.grid(row=1, column=1, sticky="w", padx=50, pady=10)
	
		self.BookingIDLabel.pack(anchor="w")
		self.statusLabel.pack(anchor="w")
		
		self.pickUpLabel.pack(anchor="w")
		self.dropOffLabel.pack(anchor="w")
		
		self.vehicleIdLabel.pack(anchor="w")
		self.vehicleNameLabel.pack(anchor="w")
		self.vehicleColourLabel.pack(anchor="w")
		self.vehicleRegistrationLabel.pack(anchor="w")
		
		self.costPerDayLabel.pack(anchor="w")
		self.totalCostLabel.pack(anchor="w")
		self.depositeLabel.pack(anchor="w")
		self.depositeDueLabel.pack(anchor="w")
		self.balanceLabel.pack(anchor="w")
		self.balanceDueLabel.pack(anchor="w")
	
	#Logsout the user and takes them to the login screen
	def logout(self) -> None:
		self.application.setLoggedInUser(None)
		self.application.setLoggedInStaff(None)
		self.application.switchForm(screens.Login)

	#Functionality for home button to switch form
	def __goHome(self):
		self.application.switchForm(screens.Home)
