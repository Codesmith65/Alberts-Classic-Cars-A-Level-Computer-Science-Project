import pickle
from re import S
import tkinter as tk
from tkinter import ttk, messagebox

import screens
from .generic import GenericScreen
from application import Application


class Search(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)
		
		self.mode = 0

		self.root.title("Albert's Classic Car - Search")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.searchIcon = tk.PhotoImage(file="assets/serach.png")
		self.infoIcon = tk.PhotoImage(file="assets/info.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.searchEntry = tk.Entry(self.mainContectFrame)
		self.SearchButton = tk.Button(self.mainContectFrame)

		self.canvas: tk.Canvas = tk.Canvas(self.mainContectFrame)
		self.searchResultsLabelFrame = tk.LabelFrame(self.canvas)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.mainContectFrame, orient=tk.VERTICAL, command=self.canvas.yview)

		for x in range(10):
			self.createSearchResult(str(x), str(x), {})
		

		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

		
		self.searchResultsLabelFrame["width"] = 100
		self.searchResultsLabelFrame["height"] = 100

		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 50
		self.companyLogoHomeButton["height"] = 50
		
		self.titleLabel["text"] ="Search"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.SearchButton["image"] = self.searchIcon
		self.searchResultsLabelFrame["text"] = "Search Results"
		
		self.companyLogoHomeButton["command"] = self.goHome
		self.SearchButton["command"] = self.search
		


		self.topBarFrame.pack()
		self.mainContectFrame.pack(fill=tk.BOTH, expand=1)

		self.companyLogoHomeButton.pack()
		self.titleLabel.pack()
		self.logOutButton.pack()
		
		self.searchEntry.pack()
		self.SearchButton.pack()
		
		self.canvas.create_window((0, 0), window=self.searchResultsLabelFrame, anchor="nw")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
		
	
	def goHome(self) -> None:
		self.application.switchForm(screens.Home)
	

	def createSearchResult(self, title: str, subTitle: str, data: dict) -> None:
		infoText: str = f"{title} Data\n"
		
		for key in data:
			infoText += f"\n{key}: {data[key]}"

		searchResultFrame = tk.Frame(self.searchResultsLabelFrame)
		titleLable: tk.Label = tk.Label(searchResultFrame, text=title)
		subTitleLable: tk.Label = tk.Label(searchResultFrame, text=subTitle)
		infoButton: tk.Button = tk.Button(searchResultFrame, image=self.infoIcon, command=lambda infoText=infoText: messagebox.showinfo(title, infoText))
		
		titleLable.grid(row=0,column=0)
		subTitleLable.grid(row=1, column=0)
		infoButton.grid(row=1,column=1)
		searchResultFrame.pack()


	def search(self) -> None:
		searchCriteria: str = self.searchEntry.get()

		self.canvas.destroy()
		self.scrollBar.destroy()

		self.canvas: tk.Canvas = tk.Canvas(self.mainContectFrame)
		self.searchResultsLabelFrame = tk.LabelFrame(self.canvas)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.mainContectFrame, orient=tk.VERTICAL, command=self.canvas.yview)
		
		if searchCriteria == "":
			messagebox.showwarning("Invalid search criteria", "Please enter a seach criteria to serach with")
		
		if self.mode == 0 or self.mode == 1:
			foundUsers: list[tuple[str, list]] = self.__linearSearchFile("data/users.pkl", searchCriteria)
			for user in foundUsers:
				self.createSearchResult("User", user[0], dict(zip(["ID", "Username"], user[1])))
		
		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.searchResultsLabelFrame, anchor="nw")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
			
	
	def __linearSearchFile(self, path: str, criteria: str) -> list[tuple[str, list]]:
		with open(path, "rb") as file:
			entries: list = pickle.load(file)
				

		print(entries)
			
		if not(type(entries) is list):
			messagebox.showerror("File Data", "There is an issue with the file data stored")
			return
		
		results: list[Tuple[str, list]] = []

		for entry in entries:
			entryAttributes: list[str] = entry.getAtributes()
			
			for attribute in entryAttributes:
				if criteria in str(attribute):
					results.append((str(attribute), entryAttributes))
					continue
		
		return results
