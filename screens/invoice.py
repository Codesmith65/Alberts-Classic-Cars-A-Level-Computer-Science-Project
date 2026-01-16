from re import S
import tkinter as tk
from tkinter import ttk
from .generic import GenericScreen
from application import Application


class Invoice(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Invoice")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage
		self.companyLogoLabel = tk.Label(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.BookingIDLabel = tk.Label(self.mainContectFrame)
		self.pickUpLabel = tk.Label(self.mainContectFrame)
		self.dropOffLabel = tk.Label(self.mainContectFrame)
		self.costLabel = tk.Label(self.mainContectFrame)
		self.depositeLabel = tk.Label(self.mainContectFrame)
		self.depositeDueLabel = tk.Label(self.mainContectFrame)
		self.balanceLabel = tk.Label(self.mainContectFrame)
		self.balanceDueLabel = tk.Label(self.mainContectFrame)
		self.statusLabel = tk.Label(self.mainContectFrame)
		

		self.companyLogoLabel["text"] = "logo"
		self.titleLabel["text"] ="Invoice"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"

		self.BookingIDLabel["text"] = "BookingID:"
		self.pickUpLabel["text"] = "Pickup:"
		self.dropOffLabel["text"] = "Drop off:"
		self.costLabel["text"] = "Cost:"
		self.depositeLabel["text"] = "Deposite:"
		self.depositeDueLabel["text"] = "Due:"
		self.balanceLabel["text"] = "Balance:"
		self.balanceDueLabel["text"] = "Due:"
		self.statusLabel["text"] = "Status:"


		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoLabel.pack()
		self.titleLabel.pack()
		self.logOutButton.pack()
		
		self.BookingIDLabel.pack()
		self.pickUpLabel.pack()
		self.dropOffLabel.pack()
		self.costLabel.pack()
		self.depositeLabel.pack()
		self.depositeDueLabel.pack()
		self.balanceLabel.pack()
		self.balanceDueLabel.pack()
		self.statusLabel.pack()
