from re import S
import tkinter as tk
from tkinter import ttk

import screens
from .generic import GenericScreen
from application import Application


class Search(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Search")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.searchEntry = tk.Entry(self.mainContectFrame)
		self.SearchButton = tk.Entry(self.mainContectFrame)
		
		self.searchResultsLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 50
		self.companyLogoHomeButton["height"] = 50
		
		self.titleLabel["text"] ="Search"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.SearchButton["text"] = "s"
		self.searchResultsLabelFrame["text"] = "Search Results"
		
		self.companyLogoHomeButton["command"] = self.goHome
		

		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoHomeButton.pack()
		self.titleLabel.pack()
		self.logOutButton.pack()
		
		self.searchEntry.pack()
		self.SearchButton.pack()
		self.searchResultsLabelFrame.pack()
	
	def goHome(self) -> None:
		self.application.switchForm(screens.Home)
