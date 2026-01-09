import tkinter as tk
from tkinter import ttk
from .generic import GenericScreen
from ..application import Application


class Task(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Task")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage
		self.companyLogoLabel = tk.Label(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = tk.Button(self.topBarFrame)
		
		self.urgentLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.importantLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.soonLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.laterLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		tk.Frame(self.urgentLabelFrame).pack()
		tk.Frame(self.importantLabelFrame).pack()
		tk.Frame(self.soonLabelFrame).pack()
		tk.Frame(self.laterLabelFrame).pack()
		

		self.companyLogoLabel["text"] = "logo"
		self.titleLabel["text"] ="Task"
		self.titleLabel["font"] = ("Helvetica", 40)
		self.logOutButton["text"] = "Logout"
		
		self.urgentLabelFrame["text"] = "Urgent"
		self.importantLabelFrame["text"] = "Important"
		self.soonLabelFrame["text"] = "Soon"
		self.laterLabelFrame["text"] = "Later"
		

		self.topBarFrame.pack()
		self.mainContectFrame.pack()

		self.companyLogoLabel.pack()
		self.titleLabel.pack()
		self.logOutButton.pack()
		
		self.urgentLabelFrame.grid(row=0, column=0)
		self.importantLabelFrame.grid(row=0, column=1)
		self.soonLabelFrame.grid(row=0, column=2)
		self.laterLabelFrame.grid(row=0, column=3)