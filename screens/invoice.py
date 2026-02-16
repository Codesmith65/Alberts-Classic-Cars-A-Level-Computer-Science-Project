from re import S
import tkinter as tk
from tkinter import ttk, messagebox
from .generic import GenericScreen
from application import Application
from uuid import UUID
from datetime import datetime
from dataTypes.booking import Booking
import pickle
import screens


class Invoice(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Invoice")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage
		self.companyLogoLabel = tk.Label(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.homeButton = tk.Button(self.topBarFrame)
		
		self.BookingIDLabel = tk.Label(self.mainContectFrame)
		self.pickUpLabel = tk.Label(self.mainContectFrame)
		self.dropOffLabel = tk.Label(self.mainContectFrame)
		self.costLabel = tk.Label(self.mainContectFrame)
		self.depositeLabel = tk.Label(self.mainContectFrame)
		self.depositeDueLabel = tk.Label(self.mainContectFrame)
		self.balanceLabel = tk.Label(self.mainContectFrame)
		self.balanceDueLabel = tk.Label(self.mainContectFrame)
		self.statusLabel = tk.Label(self.mainContectFrame)


		if not "BookingID" in self.application.crossScreenDataStore:
			self.BookingIDLabel["text"] = "BookingID: No booking inputed"
			messagebox.showerror("Booking ID", "No booking ID has been passed to this form, try going back and reloading form, if persists contact administartor")
		
		self.bookingID: UUID = self.application.crossScreenDataStore["BookingID"]
		self.booking: Booking|None = None

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
				return #Placeholder, this functionality should be abstracted to function so ui can be created regardless if booking is found or not
		
		bookingDuration = (self.booking.dropoffDate - self.booking.pickupDate) / 86400
		bookingCost = bookingDuration * 20 #Cost of booking a car per day
		bookingDeposit = bookingCost * 0.1 #Deposite is 10% of booking cost
		bookingBalence = bookingCost - bookingDeposit


		self.companyLogoLabel["text"] = "logo"
		self.titleLabel["text"] ="Invoice"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.homeButton["text"] = "Home"
		self.homeButton["command"] = self.__goHome

		self.BookingIDLabel["text"] = f"BookingID: {self.bookingID}"
		self.pickUpLabel["text"] = f"Pickup: {datetime.fromtimestamp(self.booking.pickupDate):%d/%m/%Y}"
		self.dropOffLabel["text"] = f"Drop off: {datetime.fromtimestamp(self.booking.dropoffDate):%d/%m/%Y}"
		self.costLabel["text"] = f"Cost: £{bookingCost:.2f}"
		self.depositeLabel["text"] = f"Deposite: £{bookingDeposit:.2f}"
		self.depositeDueLabel["text"] = "Due:"
		self.balanceLabel["text"] = f"Balance: £{bookingBalence:.2f}"
		self.balanceDueLabel["text"] = "Due:"
		self.statusLabel["text"] = f"Status: {self.booking.status}"


		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoLabel.pack()
		self.titleLabel.pack()
		self.homeButton.pack()
		
		self.BookingIDLabel.pack()
		self.pickUpLabel.pack()
		self.dropOffLabel.pack()
		self.costLabel.pack()
		self.depositeLabel.pack()
		self.depositeDueLabel.pack()
		self.balanceLabel.pack()
		self.balanceDueLabel.pack()
		self.statusLabel.pack()
	

	def __goHome(self):
		self.application.switchForm(screens.Home)
