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


class Invoice(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		#Creating wigets and setting window title
		self.root.title("Albert's Classic Car - Invoice")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = ttk.Button(self.topBarFrame)
		
		self.generalLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="General")
		self.vehicleLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="Vehicle")
		self.pickupAndDropoffLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="Pick up & Drop off")
		self.costLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, text="Cost")
		
		self.BookingIDLabel = tk.Label(self.generalLabelFrame, justify="left")
		self.statusLabel = tk.Label(self.generalLabelFrame, justify="left")
		
		self.pickUpLabel = tk.Label(self.pickupAndDropoffLabelFrame, justify="left")
		self.dropOffLabel = tk.Label(self.pickupAndDropoffLabelFrame, justify="left")

		self.vehicleIdLabel = tk.Label(self.vehicleLabelFrame, justify="left")
		self.vehicleNameLabel = tk.Label(self.vehicleLabelFrame, justify="left")
		self.vehicleColourLabel = tk.Label(self.vehicleLabelFrame, justify="left")
		self.vehicleRegistrationLabel = tk.Label(self.vehicleLabelFrame, justify="left")
		
		self.costPerDayLabel = tk.Label(self.costLabelFrame, justify="left")
		self.totalCostLabel = tk.Label(self.costLabelFrame, justify="left")
		self.depositeLabel = tk.Label(self.costLabelFrame, justify="left")
		self.depositeDueLabel = tk.Label(self.costLabelFrame, justify="left")
		self.balanceLabel = tk.Label(self.costLabelFrame, justify="left")
		self.balanceDueLabel = tk.Label(self.costLabelFrame, justify="left")


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
