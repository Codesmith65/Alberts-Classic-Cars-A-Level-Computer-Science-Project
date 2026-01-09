from calendar import setfirstweekday
import tkinter as tk
from tkinter import ttk
from .generic import Generic


class Account(Generic):
	def __init__(self) -> None:
		super().__init__()

		self.root.title("Albert's Classic Car - Accounts")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage
		self.companyLogoLabel = tk.Label(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.newAccountLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.accountsLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		self.newAccountUsernameEntry = tk.Entry(self.newAccountLabelFrame)
		self.newAccountCreateButton = tk.Button(self.newAccountLabelFrame)

		tk.Frame(self.accountsLabelFrame).pack()


		self.companyLogoLabel["text"] = "logo"
		self.titleLabel["text"] ="Accounts"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.newAccountLabelFrame["text"] = "New Account"
		self.accountsLabelFrame["text"] = "Accounts"

		self.newAccountCreateButton["text"] = "Create Account"
		

		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoLabel.pack()
		self.titleLabel.pack()
		self.logOutButton.pack()
		
		self.newAccountLabelFrame.grid(row=0, column=1)
		self.newAccountUsernameEntry.pack()
		self.newAccountCreateButton.pack()
		
		self.accountsLabelFrame.grid(row=0, column=1)
		