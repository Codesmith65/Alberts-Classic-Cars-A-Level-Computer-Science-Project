import tkinter as tk
from tkinter import ttk
from .generic import Generic


class Booking(Generic):
	def __init__(self) -> None:
		super().__init__()

		self.root.title("Albert's Classic Car - Booking")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage
		self.companyLogoLabel = tk.Label(self.topBarFrame)
		self.titleLable = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.clientLabel = tk.Label(self.mainContectFrame)
		self.clientEntry = tk.Entry(self.mainContectFrame)
		self.clientSearch = tk.Button(self.mainContectFrame)
		
		self.vehicleLabel = tk.Label(self.mainContectFrame)
		self.vehicleEntry = tk.Entry(self.mainContectFrame)
		self.vehicleSearch = tk.Button(self.mainContectFrame)
		
		self.pickUpDateLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.dropOffDateLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		self.testButton1 = tk.Button(self.pickUpDateLabelFrame, text="test")
		self.testButton1.pack()
		self.testButton1 = tk.Button(self.dropOffDateLabelFrame, text="test")
		self.testButton1.pack()


		self.companyLogoLabel["text"] = "logo"
		self.titleLable["text"] ="Booking"
		self.titleLable["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.clientLabel["text"] = "Client"
		self.clientSearch["text"] = "s"
		self.vehicleLabel["text"] = "Vehicle"
		self.vehicleSearch["text"] = "s"
		
		self.pickUpDateLabelFrame["text"] = "Pickup Date"
		self.dropOffDateLabelFrame["text"] = "Drop off Date"


		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoLabel.pack()
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