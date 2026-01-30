import pickle
from re import S
import tkinter as tk
from tkinter import messagebox


class SearchPopup:
	def __init__(self, mode: int = 0) -> None:
		self.topLevel = tk.Toplevel()
		self.topLevel.title("Albert's Classic Car - Search")
		self.topLevel.geometry("1000x600")
		self.topLevel.resizable(False, False)

		self.mode: int = mode
        
		self.topBarFrame = tk.Frame(self.topLevel)
		self.mainContectFrame = tk.Frame(self.topLevel)
        
		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.searchIcon = tk.PhotoImage(file="assets/serach.png")
		self.infoIcon = tk.PhotoImage(file="assets/info.png")
		self.companyLogoLabel: tk.Label = tk.Label(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
        
		self.searchEntry = tk.Entry(self.mainContectFrame)
		self.SearchButton = tk.Button(self.mainContectFrame)
        
		self.canvas: tk.Canvas = tk.Canvas(self.mainContectFrame)
		self.searchResultsLabelFrame = tk.LabelFrame(self.canvas)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.mainContectFrame, orient=tk.VERTICAL, command=self.canvas.yview)
		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.searchResultsLabelFrame["width"] = 100
		self.searchResultsLabelFrame["height"] = 100
        
		self.companyLogoLabel["image"] = self.companyLogo
		self.companyLogoLabel["relief"] = "flat"
		self.companyLogoLabel["borderwidth"] = 0
		self.companyLogoLabel["width"] = 50
		self.companyLogoLabel["height"] = 50
		self.titleLabel["text"] ="Search"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.SearchButton["image"] = self.searchIcon
		self.searchResultsLabelFrame["text"] = "Search Results"
		self.SearchButton["command"] = self.search		
		

		self.topBarFrame.pack()
		self.mainContectFrame.pack()
        
		self.companyLogoLabel.pack()
		self.titleLabel.pack()
        
		self.searchEntry.pack()
		self.SearchButton.pack()
        
		self.canvas.create_window((0, 0), window=self.searchResultsLabelFrame, anchor="nw")
		self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
    
	def search(self) -> None:
		searchCriteria: str = self.searchEntry.get()

		self.canvas.destroy()
		self.scrollBar.destroy()

		self.canvas: tk.Canvas = tk.Canvas(self.mainContectFrame)
		self.searchResultsLabelFrame = tk.LabelFrame(self.canvas)
		self.scrollBar: tk.Scrollbar = tk.Scrollbar(self.mainContectFrame, orient=tk.VERTICAL, command=self.canvas.yview)
		
		if searchCriteria == "":
			messagebox.showinfo("Mising search criteria", "Please enter a seach criteria to narrow down search results.\nShowng all values")
		
		if self.mode == 0 or self.mode == 1:
			foundUsers: list[tuple[str, list]] = self.__linearSearchFile("data/users.pkl", searchCriteria)
			for user in foundUsers:
				self.__createSearchResult("User", user[0], dict(zip(["ID", "Username"], user[1])))
		
		self.canvas.config(yscrollcommand=self.scrollBar.set)
		self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0, 0), window=self.searchResultsLabelFrame, anchor="nw")
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
				if criteria in str(attribute):
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
		infoButton: tk.Button = tk.Button(searchResultFrame, image=self.infoIcon, command=lambda infoText=infoText: messagebox.showinfo(title, infoText))
		selectButton: tk.Button = tk.Button(searchResultFrame, text="Select", command=lambda id="": self.__select(id))						
		
		titleLable.grid(row=0,column=0)
		subTitleLable.grid(row=1, column=0)
		infoButton.grid(row=1,column=1)
		selectButton.grid(row=2, column=0)		
		searchResultFrame.pack()

	def __select(self, id) -> None:
		children = self.searchResultsLabelFrame.children
				
		for child in children:
			children[child].configure(bg="SystemButtonFace")	
		