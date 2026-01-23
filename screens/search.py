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
		self.SearchButton = tk.Button(self.mainContectFrame)
		
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
		self.SearchButton["command"] = self.search
		

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


	def createSearchResult(self, title: str, subTitle: str, data: dict) -> None:
		infoText: str = f"{title} Data\n"
		
		for key in data:
			infoText += f"\n{key}: {data[key]}"

		searchResultFrame = tk.Frame(self.searchResultsLabelFrame)
		titleLable: tk.Label = tk.Label(searchResultFrame, text=title)
		subTitle: tk.Label = tk.Label(searchResultFrame, text=subTitle)
		infoButton: tk.Button = tk.Button(searchResultFrame, image=self.infoIcon, command=lambda infoText=infoText: messagebox.showinfo(title, infoText))
		
		titleLable.grid(row=0,column=0)
		subTitle.grid(row=1, column=0)
		infoButton.grid(row=1,column=1)
		searchResultFrame.pack()


	def search(self) -> None:
		searchCriteria: str = self.searchEntry.get()
		
		if searchCriteria == "":
			messagebox.showwarning("Invalid search criteria", "Please enter a seach criteria to serach with")
		
		if self.mode == 0 or self.mode == 1:
			foundUsers: list[tuple[str, list]] = self.__linearSearchFile("data/users.pkl", searchCriteria)
			for user in foundUsers:
				self.createSearchResult("User", user[0], dict(zip(["ID", "Username"], user[1])))
			
	
	def __linearSearchFile(self, path: str, criteria: str) -> list[tuple[str, list]]:
		with open(path, "rb") as file:
			entries: list = pickle.load(file)
				

		print(entries)
			
		if not(type(entries) is list):
			messagebox.showerror("User Data", "There is an issue with the user data stored")
		
		results: list[Tuple[str, list]] = []

		for entry in entries:
			entryAttributes: list[str] = entry.getAtributes()
			
			for attribute in entryAttributes:
				if criteria in str(attribute):
					results.append((str(attribute), entryAttributes))
					continue
		
		return results
