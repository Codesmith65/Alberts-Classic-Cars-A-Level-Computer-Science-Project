import pickle
from re import S
import tkinter as tk
from tkinter import ttk, messagebox

import screens
import popups
from .generic import GenericScreen
from application import Application


class Search(GenericScreen):
	def __init__(self, application: Application, mode: int = 0) -> None:
		super().__init__(application)
		
		self.mode: int = mode
		if "mode" in application.crossScreenDataStore and type(application.crossScreenDataStore["mode"]) is int:
			self.mdoe = application.crossScreenDataStore["mode"]

		self.root.title("Albert's Classic Car - Search")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.searchIcon = tk.PhotoImage(file="assets/serach.png")
		self.infoIcon = tk.PhotoImage(file="assets/info.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = ttk.Button(self.topBarFrame)
		
		self.searchEntry = tk.Entry(self.mainContectFrame)
		self.SearchButton = tk.Button(self.mainContectFrame)

		self.canvas: tk.Canvas = tk.Canvas(self.mainContectFrame)
		self.searchResultsLabelFrame = tk.LabelFrame(self.canvas)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.mainContectFrame, orient=tk.VERTICAL, command=self.canvas.yview)
		

		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

		self.searchResultsLabelFrame["width"] = 100
		self.searchResultsLabelFrame["height"] = 100

		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 100
		self.companyLogoHomeButton["height"] = 100
		
		self.titleLabel["text"] ="Search"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.SearchButton["image"] = self.searchIcon
		self.searchResultsLabelFrame["text"] = "Search Results"
		
		self.companyLogoHomeButton["command"] = self.goHome
		self.SearchButton["command"] = self.search
		self.logOutButton["command"] = self.logout


		self.topBarFrame.pack(fill="x")
		self.mainContectFrame.pack(fill=tk.BOTH, expand=1)

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLabel.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
		
		self.searchEntry.pack()
		self.SearchButton.pack()
		
		self.canvas.create_window((0, 0), window=self.searchResultsLabelFrame, anchor="nw")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
	
	
	def goHome(self) -> None:
		self.application.switchForm(screens.Home)

	def logout(self) -> None:
		self.application.setLoggedInUser(None)
		self.application.setLoggedInStaff(None)
		self.application.switchForm(screens.Login)
	

	def search(self) -> None:
		searchCriteria: str = self.searchEntry.get()

		self.canvas.destroy()
		self.scrollBar.destroy()

		self.canvas: tk.Canvas = tk.Canvas(self.mainContectFrame)
		self.searchResultsLabelFrame = tk.LabelFrame(self.canvas)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.mainContectFrame, orient=tk.VERTICAL, command=self.canvas.yview)

		self.mainContectFrame.update()
		
		if searchCriteria == "":
			messagebox.showinfo("Mising search criteria", "Please enter a seach criteria to narrow down search results.\nShowng all values")
		
		searchCap = 800
		resultNumber = 0
		
		
		if self.mode == 1:
			foundUsers: list[tuple[str, list]] = self.__linearSearchFile("data/users.pkl", searchCriteria)
			for user in foundUsers:
				self.__createSearchResult("User", user[0], dict(zip(["id", "username"], user[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
			foundStaff: list[tuple[str, list]] = self.__linearSearchFile("data/staff.pkl", searchCriteria)
			for staff in foundStaff:
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
				self.__createSearchResult("Staff", user[0], dict(zip(["id", "username"], user[1])))
				resultNumber += 1
				
		
		if (self.mode == 0 or self.mode == 2) and resultNumber < searchCap:
			foundClients: list[tuple[str, list]] = self.__linearSearchFile("data/clients.pkl", searchCriteria)
			for client in foundClients:
				self.__createSearchResult("Client", client[0], dict(zip(["id", "first name", "last name", "email", "address", "phone number"], client[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		if (self.mode == 0 or self.mode == 3) and resultNumber < searchCap:
			foundBookings: list[tuple[str, list]] = self.__linearSearchFile("data/bookings.pkl", searchCriteria)
			for booking in foundBookings:
				self.__createSearchResult("Booking", booking[0], dict(zip(["id", "staff id", "client id", "vehicle id", "pick up date", "pickup location id", "drop off date", "dropoff location id", "status"], booking[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		if (self.mode == 0 or self.mode == 4) and resultNumber < searchCap:
			foundVehicles: list[tuple[str, list]] = self.__linearSearchFile("data/vehicles.pkl", searchCriteria)
			for vehicle in foundVehicles:
				self.__createSearchResult("Vehicle", vehicle[0], dict(zip(["id", "make", "model", "colour", "registration", "vin"], vehicle[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		if (self.mode == 0 or self.mode == 5) and resultNumber < searchCap:
			foundLocation: list[tuple[str, list]] = self.__linearSearchFile("data/locations.pkl", searchCriteria)
			for location in foundLocation:
				self.__createSearchResult("Location", location[0], dict(zip(["id", "make", "model", "colour", "registration", "vin"], location[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		if (self.mode == 0 or self.mode == 6) and resultNumber < searchCap:
			foundTasks: list[tuple[str, list]] = self.__linearSearchFile("data/tasks.pkl", searchCriteria)
			for task in foundTasks:
				self.__createSearchResult("Task", task[0], dict(zip(["id", "make", "model", "colour", "registration", "vin"], task[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		print(resultNumber)
		
		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.searchResultsLabelFrame, anchor="center")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
			
	
	def __linearSearchFile(self, path: str, criteria: str) -> list[tuple[str, list]]:
		with open(path, "rb") as file:
			entries: list = pickle.load(file)
			
		if not(type(entries) is list):
			messagebox.showerror("File Data", "There is an issue with the file data stored")
			return
		
		results: list[Tuple[str, list]] = []

		for entry in entries:
			entryAttributes: list[str] = entry.getAtributes()
			
			for attribute in entryAttributes:
				if criteria.lower() in str(attribute).lower():
					results.append((str(attribute), entryAttributes))
					continue
		
		return results
	
	def __createSearchResult(self, title: str, subTitle: str, data: dict) -> None:
		infoText: str = f"{title} Data\n"
		
		for key in data:
			infoText += f"\n{key}: {data[key]}"

		searchResultFrame = tk.Frame(self.searchResultsLabelFrame)
		titleLable: tk.Label = tk.Label(searchResultFrame, text=title)
		subTitleLable: tk.Label = tk.Label(searchResultFrame, text=subTitle)
		infoButton: tk.Button = tk.Button(searchResultFrame, image=self.infoIcon, command=lambda infoText=infoText: popups.MessageBoxInfoEditButton(title, infoText, lambda dataType=title, data=data: self.__openEdit(dataType, data)))
		
		titleLable.grid(row=0,column=0)
		subTitleLable.grid(row=1, column=0)
		infoButton.grid(row=1,column=1)
		searchResultFrame.pack()
	
	def __openEdit(self, dataType: str, data: dict):
		if dataType.lower() == "user":
			pass
		elif dataType.lower() == "staff":
			pass
		elif dataType.lower() == "client":
			popups.ClientEdit(data)
		elif dataType.lower() == "booking":
			popups.BookingEdit(data)
		elif dataType.lower() == "vehicle":
			popups.VehicleEdit(data)
		elif dataType.lower() == "location":
			pass
		elif dataType.lower() == "task":
			pass
