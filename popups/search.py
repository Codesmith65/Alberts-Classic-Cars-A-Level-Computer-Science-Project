import pickle
from re import S
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import popups
import colourPallet as pallet


class SearchPopup:
	def __init__(self, mode: int = 0) -> None:
		self.selctedData: dict = {}

		# Configures the popup window
		self.topLevel = tk.Toplevel()
		self.topLevel.title("Albert's Classic Car - Search")
		self.topLevel.geometry("1000x600")
		self.topLevel.resizable(False, False)

		# Gets the mode set
		self.mode: int = mode

		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("generic.TEntry", background=pallet.bg2, highlightcolor=pallet.highlight)
        
		# Creatingthe frame for the UI
		self.topBarFrame = tk.Frame(self.topLevel, bg=pallet.bg2)
		self.mainContectFrame = tk.Frame(self.topLevel, bg=pallet.bg)
		self.serachResultsContainer = tk.Frame(self.mainContectFrame, bg=pallet.bg)
		self.searchCriteriaContainer = tk.Frame(self.mainContectFrame, bg=pallet.bg)
        
		# Creating widgets for UI
		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.searchIcon = tk.PhotoImage(file="assets/serach.png")
		self.infoIcon = tk.PhotoImage(file="assets/info.png")
		self.companyLogoLabel: tk.Label = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.titleLabel = tk.Label(self.topBarFrame, bg=pallet.bg2)
        
		self.searchEntry = ttk.Entry(self.searchCriteriaContainer, style="generic.TEntry")
		self.SearchButton = ttk.Button(self.searchCriteriaContainer, style="generic.TButton")
        
		self.canvas: tk.Canvas = tk.Canvas(self.serachResultsContainer, bg=pallet.bg)
		self.searchResultsFrame = tk.Frame(self.canvas, bg=pallet.bg)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.serachResultsContainer, orient=tk.VERTICAL, command=self.canvas.yview)
		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		

		# Configuring the widgets
		self.searchResultsFrame["width"] = 100
		self.searchResultsFrame["height"] = 100
        
		self.companyLogoLabel["image"] = self.companyLogo
		self.companyLogoLabel["relief"] = "flat"
		self.companyLogoLabel["borderwidth"] = 0
		self.companyLogoLabel["width"] = 100
		self.companyLogoLabel["height"] = 100
		self.titleLabel["text"] ="Search"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.SearchButton["image"] = self.searchIcon
		self.SearchButton["command"] = self.search		
		

		# Places the widgets on the window
		self.topBarFrame.pack(fill="x")
		self.mainContectFrame.pack(fill=tk.BOTH, expand=1)
        
		self.companyLogoLabel.grid(row=0, column=0, sticky="w")
		self.titleLabel.grid(row=0, column=1)
		tk.Frame(self.topBarFrame, width=50, bg=pallet.bg2).grid(row=0, column=2)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
        
		self.searchEntry.pack(side="left", fill="x", expand=1)
		self.SearchButton.pack(side="right")
		self.searchCriteriaContainer.pack(side="top", fill="x")
		self.serachResultsContainer.pack(side="bottom", expand=1, fill="both")
        
		self.canvas.create_window((0, 0), window=self.searchResultsFrame, anchor="nw")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
    
	# preforms the searching functions
	def search(self) -> None:
		# Gets the searching criteria
		searchCriteria: str = self.searchEntry.get()

		# Removes the old scrol container and scroll bar
		self.canvas.destroy()
		self.scrollBar.destroy()

		# Creates the new scroll container and scroll bar
		self.canvas: tk.Canvas = tk.Canvas(self.serachResultsContainer, bg=pallet.bg)
		self.searchResultsFrame = tk.Frame(self.canvas, bg=pallet.bg)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.serachResultsContainer, orient=tk.VERTICAL, command=self.canvas.yview, bg=pallet.bg)

		# Updates the the container so scroll bar shows
		self.serachResultsContainer.update()

		# Shows a info box if no criteria is entered
		if searchCriteria == "":
			messagebox.showinfo("Mising search criteria", "Please enter a seach criteria to narrow down search results.\nShowng all values")
		
		# Sets the search max and a counter to keep track
		searchCap = 800
		resultNumber = 0

		# Preforms searches based on the mode
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
				self.__createSearchResult("Location", location[0], dict(zip(["id", "location name"], location[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		if (self.mode == 0 or self.mode == 6) and resultNumber < searchCap:
			foundTasks: list[tuple[str, list]] = self.__linearSearchFile("data/tasks.pkl", searchCriteria)
			for task in foundTasks:
				self.__createSearchResult("Task", task[0], dict(zip(["id", "task name", "task description", "completed", "parent task", "staff id", "importance"], task[1])))
				resultNumber += 1
				if resultNumber > searchCap:
					messagebox.showerror("Search cap reached", "Search cap has been reached, use the search box to narrow down your results\nThe last results have been exculded")
					break
		
		# Configures and places the new canvas and scroll bar in UI
		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.searchResultsFrame, anchor="center")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
	
	# Linearly searches through the file to find the results
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
	
	# Creates the search results display
	def __createSearchResult(self, title: str, subTitle: str, data: dict) -> None:
		infoText: str = f"{title} Data\n"
		
		for key in data:
			infoText += f"\n{key}: {data[key]}"

		searchResultFrame = tk.Frame(self.searchResultsFrame, bg=pallet.bg)
		titleLable: tk.Label = tk.Label(searchResultFrame, text=title, bg=pallet.bg)
		subTitleLable: tk.Label = tk.Label(searchResultFrame, text=subTitle, bg=pallet.bg)
		infoButton: ttk.Button = ttk.Button(searchResultFrame, image=self.infoIcon, command=lambda title=title, infoText=infoText: popups.MessageBoxInfoEditButton(title, infoText, print), style="generic.TButton")
		selectButton: ttk.Button = ttk.Button(searchResultFrame, text="Select", command=lambda frame=searchResultFrame, data=data: self.__select(frame, data), style="generic.TButton")						
		
		titleLable.grid(row=0,column=0)
		subTitleLable.grid(row=1, column=0)
		infoButton.grid(row=1,column=1)
		selectButton.grid(row=2, column=0)		
		searchResultFrame.pack()

	# Used to select a result to be used
	def __select(self, frame: tk.Frame, data: dict) -> None:
		children = self.searchResultsFrame.children
				
		for child in children:
			children[child].configure(bg=pallet.bg)
		
		frame.configure(bg="Blue")
		self.selctedData = data
	
	# Used to take the user to the correct edit popup
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
			popups.TaskEdit(data)
		