import pickle
import tkinter as tk
from tkinter import ttk
import tkinter
import uuid

import screens
from .generic import GenericScreen
from application import Application

from dataTypes.task import Task as TaskDataType

import colourPallet as pallet


class Task(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)
		
		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("generic.TEntry", background=pallet.bg, highlightcolor=pallet.highlight)
		style.configure("generic.TCombobox", background=pallet.bg, highlightcolor=pallet.highlight)
		style.configure("generic.TCheckbutton", background=pallet.bg, highlightcolor=pallet.highlight)

		# Sets teh window title
		self.root.title("Albert's Classic Car - Task")
		self.root.configure(bg=pallet.bg)

		# Creates the frames for the UI
		self.topBarFrame = tk.Frame(self.root, bg=pallet.bg2)
		self.mainContectFrame = tk.Frame(self.root, bg=pallet.bg)

		# Created widgets for the UI
		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame, bg=pallet.bg2)
		self.titleLabel = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.logOutButton = ttk.Button(self.topBarFrame, style="nav.TButton")
		
		self.urgentLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, bg=pallet.bg)
		self.importantLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, bg=pallet.bg)
		self.soonLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, bg=pallet.bg)
		self.laterLabelFrame = tk.LabelFrame(self.mainContectFrame, border=0, bg=pallet.bg)
		
		self.saveButton = ttk.Button(self.mainContectFrame, style="generic.TButton")
		

		# Configure the widgets for the UI
		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 100
		self.companyLogoHomeButton["height"] = 100
		self.companyLogoHomeButton["command"] = self.goHome
		
		self.saveButton["text"] = "Save"
		self.saveButton["command"] = self.save
		
		self.titleLabel["text"] ="Task"
		self.titleLabel["font"] = ("Helvetica", 40)
		
		self.logOutButton["text"] = "Logout"
		self.logOutButton["command"] = self.logOut
		
		self.urgentLabelFrame["text"] = "Urgent"
		self.importantLabelFrame["text"] = "Important"
		self.soonLabelFrame["text"] = "Soon"
		self.laterLabelFrame["text"] = "Later"
		

		# Place the widgets for the UI
		self.topBarFrame.pack(fill="both")
		self.mainContectFrame.pack(expand=1, fill="both")

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLabel.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
		
		self.urgentLabelFrame.grid(row=0, column=0)
		self.importantLabelFrame.grid(row=0, column=1)
		self.soonLabelFrame.grid(row=0, column=2)
		self.laterLabelFrame.grid(row=0, column=3)
		self.saveButton.grid(row=1, column=3, sticky="se")
		
		self.mainContectFrame.columnconfigure(0, weight=1)
		self.mainContectFrame.columnconfigure(1, weight=1)
		self.mainContectFrame.columnconfigure(2, weight=1)
		self.mainContectFrame.columnconfigure(3, weight=1)
		
		self.tasksComplete = []
		
		self.populateTasks()
	
	def populateTasks(self):
		# Open task file
		with open("data/tasks.pkl", "br") as taskFile:
			tasks: list[TaskDataType] = pickle.load(taskFile)
		
		# Getting user tasks
		userTasks: list[TaskDataType] = []
		for task in tasks:
			if task.staffID == self.application.loggedInStaff:
				userTasks.append(task)
		
		# Create scrolling canvases and frames for each task type
		urgentCanvas: tk.Canvas = tk.Canvas(self.urgentLabelFrame, bg=pallet.bg)
		urgentScrollFrame = tk.Frame(urgentCanvas, bg=pallet.bg)
		urgentScrollBar: tk.Scrollbar = tk.Scrollbar(self.urgentLabelFrame, orient="vertical", command=urgentCanvas.yview, bg=pallet.bg)
		
		importantCanvas: tk.Canvas = tk.Canvas(self.importantLabelFrame, bg=pallet.bg)
		importantScrollFrame = tk.Frame(importantCanvas, bg=pallet.bg)
		importantScrollBar: tk.Scrollbar = tk.Scrollbar(self.importantLabelFrame, orient="vertical", command=importantCanvas.yview, bg=pallet.bg)
		
		soonCanvas: tk.Canvas = tk.Canvas(self.soonLabelFrame, bg=pallet.bg)
		soonScrollFrame = tk.Frame(soonCanvas, bg=pallet.bg)
		soonScrollBar: tk.Scrollbar = tk.Scrollbar(self.soonLabelFrame, orient="vertical", command=soonCanvas.yview, bg=pallet.bg)

		laterCanvas: tk.Canvas = tk.Canvas(self.laterLabelFrame, bg=pallet.bg)
		laterScrollFrame = tk.Frame(laterCanvas, bg=pallet.bg)
		laterScrollBar: tk.Scrollbar = tk.Scrollbar(self.laterLabelFrame, orient="vertical", command=laterCanvas.yview, bg=pallet.bg)
		
		# Populate the diffrent tasks feilds
		for task in userTasks:
			if task.importance == 0:
				parent = urgentScrollFrame
			elif task.importance == 1:
				parent = importantScrollFrame
			elif task.importance == 2:
				parent = soonScrollFrame
			elif task.importance == 3:
				parent = laterScrollFrame
			else:
				parent = laterScrollFrame
			
			taskFrame = tk.Frame(parent, bg=pallet.bg)
			taskNameLabel = tk.Label(taskFrame, text=task.taskName, justify="left", font=("Helvetica", 12, "bold"), bg=pallet.bg)
			taskDescriptionLabel = tk.Label(taskFrame, text=task.taskDescription, justify="left", bg=pallet.bg)
			boolVar = tkinter.BooleanVar()
			taskTickBox = ttk.Checkbutton(taskFrame, text="completed", variable=boolVar, command=lambda boolVar=boolVar, taskId=task.taskID: self.__changeState(boolVar, taskId), style="generic.TCheckbutton")
			boolVar.set(False)
			
			taskFrame.pack()
			taskNameLabel.pack(anchor="w")
			taskDescriptionLabel.pack(anchor="w")
			taskTickBox.pack(anchor="w")
		
		# Configure the scrolling canvases to allwo the scoll of the tasks
		urgentCanvas.configure(yscrollcommand=urgentScrollBar.set)
		urgentCanvas.bind("<Configure>", lambda e: urgentCanvas.configure(scrollregion=urgentCanvas.bbox("all")))
		urgentCanvas.bind("<MouseWheel>", lambda event: urgentCanvas.yview_scroll(int(-1*(event.delta/60)), "units"))
		urgentCanvas.create_window((0,0), window=urgentScrollFrame, anchor="nw")
		urgentCanvas.pack(fill="both", expand=0, side="left")
		urgentScrollBar.pack(side="right", fill="y")
		
		importantCanvas.configure(yscrollcommand=importantScrollBar.set)
		importantCanvas.bind("<Configure>", lambda e: importantCanvas.configure(scrollregion=importantCanvas.bbox("all")))
		importantCanvas.bind("<MouseWheel>", lambda event: importantCanvas.yview_scroll(int(-1*(event.delta/60)), "units"))
		importantCanvas.create_window((0,0), window=importantScrollFrame, anchor="nw")
		importantCanvas.pack(fill="both", expand=0, side="left")
		importantScrollBar.pack(side="right", fill="y")
		
		soonCanvas.configure(yscrollcommand=soonScrollBar.set)
		soonCanvas.bind("<Configure>", lambda e: soonCanvas.configure(scrollregion=soonCanvas.bbox("all")))
		soonCanvas.bind("<MouseWheel>", lambda event: soonCanvas.yview_scroll(int(-1*(event.delta/60)), "units"))
		soonCanvas.create_window((0,0), window=soonScrollFrame, anchor="nw")
		soonCanvas.pack(fill="both", expand=0, side="left")
		soonScrollBar.pack(side="right", fill="y")
		
		laterCanvas.configure(yscrollcommand=laterScrollBar.set)
		laterCanvas.bind("<Configure>", lambda e: laterCanvas.configure(scrollregion=laterCanvas.bbox("all")))
		laterCanvas.bind("<MouseWheel>", lambda event: laterCanvas.yview_scroll(int(-1*(event.delta/60)), "units"))
		laterCanvas.create_window((0,0), window=laterScrollFrame, anchor="nw")
		laterCanvas.pack(fill="both", expand=0, side="left")
		laterScrollBar.pack(side="right", fill="y")

		self.urgentLabelFrame.update()
		self.importantLabelFrame.update()
		self.soonLabelFrame.update()
		self.laterLabelFrame.update()
	
	# Used to send the user home
	def goHome(self):
		self.application.switchForm(screens.Home)
	
	# Loggs the user out and takes them to the login screen
	def logOut(self):
		self.application.setLoggedInUser(None)
		self.application.setLoggedInStaff(None)
		self.application.switchForm(screens.Login)
	
	# Saves the tasks that have been complted
	def save(self):
		with open("data/tasks.pkl", "br") as taskFile:
			tasks: list[TaskDataType] = pickle.load(taskFile)
		
		index = 0
		for task in tasks:
			if task.taskID in self.tasksComplete:
				tasks.pop(index)
			
			index += 1
		
		with open("data/tasks.pkl", "bw") as taskFile:
			pickle.dump(tasks, taskFile)
	
	# Called when a checkbox changes state to record it
	def __changeState(self, boolVar: tk.BooleanVar, taskId: uuid.UUID):
		if boolVar.get():
			if taskId in self.tasksComplete:
				return
			else:
				self.tasksComplete.append(taskId)
		
		else:
			if taskId in self.tasksComplete:
				self.tasksComplete.remove(taskId)