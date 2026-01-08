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


		self.companyLogoLabel["text"] = "logo"
		self.titleLable["text"] ="Booking"
		self.titleLable["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"


		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoLabel.pack()
		self.titleLable.pack()
		self.logOutButton.pack()