import tkinter as tk
from tkinter import ttk, messagebox
from .generic import GenericScreen
from application import Application
import screens, popups
import random
import string
import pickle

from dataTypes.user import User
from dataTypes.staff import Staff

import colourPallet as pallet


class Account(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		# Creates the styling for the screen for ttk widgets
		style = ttk.Style()
		style.configure("generic.TButton", background=pallet.bg)
		style.configure("generic.TLabel", background=pallet.bg)
		style.configure("nav.TButton", background=pallet.bg2)
		style.configure("generic.TEntry", background=pallet.bg, highlightcolor=pallet.highlight)
		style.configure("generic.TCombobox", background=pallet.bg, highlightcolor=pallet.highlight)
		
		# Sets the window title
		self.root.title("Albert's Classic Car - Accounts")

		# Creates the frames for the ui
		self.topBarFrame = tk.Frame(self.root, bg=pallet.bg2)
		self.mainContectFrame = tk.Frame(self.root, bg=pallet.bg)

		# Creates the widgets for the UI
		self.infoIcon = tk.PhotoImage(file="assets/info.png")
		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame, bg=pallet.bg2)
		self.titleLabel = tk.Label(self.topBarFrame, bg=pallet.bg2)
		self.logOutButton = ttk.Button(self.topBarFrame, style="nav.TButton")
		
		self.newAccountLabelFrame = tk.LabelFrame(self.mainContectFrame, bg=pallet.bg)
		self.accountsLabelFrame = tk.LabelFrame(self.mainContectFrame, bg=pallet.bg)
		
		self.newAccountUsernameEntry = ttk.Entry(self.newAccountLabelFrame, style="generic.TEntry")
		self.newAccountUsernameLabel = ttk.Label(self.newAccountLabelFrame, style="generic.TLabel")
		self.newAccountCreateButton = ttk.Button(self.newAccountLabelFrame, style="generic.TButton")

		self.populateAccounts()


		# Configures UI widgets
		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 100
		self.companyLogoHomeButton["height"] = 100
		self.companyLogoHomeButton["command"] = self.goHome

		self.titleLabel["text"] ="Accounts"
		self.titleLabel["font"] = ("Helvetica", 40)

		self.logOutButton["text"] = "Logout"
		self.logOutButton["command"] = self.logOut
		
		self.newAccountLabelFrame["text"] = "New Account"
		self.accountsLabelFrame["text"] = "Accounts"

		self.newAccountUsernameLabel["text"] = "Username:"

		self.newAccountCreateButton["text"] = "Create Account"
		self.newAccountCreateButton["command"] = self.addUserAccount
		

		# Place widgets on the UI
		self.topBarFrame.pack(fill="x")

		self.companyLogoHomeButton.grid(row=0, column=0, sticky="w")
		self.titleLabel.grid(row=0, column=1)
		self.logOutButton.grid(row=0, column=2, sticky="e", padx=5)

		self.topBarFrame.columnconfigure(0, weight=1)
		self.topBarFrame.columnconfigure(1, weight=1)
		self.topBarFrame.columnconfigure(2, weight=1)
		
		self.newAccountLabelFrame.pack(side="left", expand=1)
		self.newAccountUsernameLabel.grid(row=0, column=0)
		self.newAccountUsernameEntry.grid(row=0, column=1)
		self.newAccountCreateButton.grid(row=1, column=0, columnspan=2)
		
		self.accountsLabelFrame.pack(side="right", fill="both", expand=1)

		self.mainContectFrame.pack(fill="both", expand=1)
	
	# Takes the user to the home screen
	def goHome(self):
		self.application.switchForm(screens.Home)
	
	# Loggs the user out and takes them to the login screen
	def logOut(self):
		self.application.switchForm(screens.Login)
		self.application.setLoggedInStaff(None)
		self.application.setLoggedInUser(None)
	
	# Populates the accounts frame
	def populateAccounts(self):
		# Opens the staff file and loads the current staff
		with open("data/staff.pkl", "br") as staffFile:
			staff: list[Staff] = pickle.load(staffFile)
		
		# Creates a map fo user ids to staff indexes by loaping over all staff and setting the map value to teh id and the valeu to the index
		userIdToStaffIndex = {}
		index = 0
		for staffMember in staff:
			userIdToStaffIndex[staffMember.userID] = index
			index += 1

		# Opens the user file and gets all the users
		with open("data/users.pkl", "br") as userFile:
			users: list[User] = pickle.load(userFile)
		
		# Creates the widgets for the scroll bar
		canvas: tk.Canvas = tk.Canvas(self.accountsLabelFrame, bg=pallet.bg, borderwidth=0)
		accountsScrollFrame = tk.Frame(canvas, bg=pallet.bg)
		scrollBar: tk.Scrollbar = tk.Scrollbar(self.accountsLabelFrame, orient=tk.VERTICAL, command=canvas.yview, bg=pallet.bg, borderwidth=0)
		
		# Loops through all users and creates a record in the scroll container
		index = 0
		for user in users:
			# Gets the asociated staff member and creates the widget fram
			staffMember = staff[userIdToStaffIndex[user.userID]]
			userFrame = tk.Frame(accountsScrollFrame, bg=pallet.bg)

			# Creates the info text for the info popup
			infoText = f"username: {user.username}\nname: {staffMember.firstName} {staffMember.lastName}\n" \
			f"userID: {user.userID}\nstaffID: {staffMember.staffID}\nstaff address: {staffMember.address}\nstaff phone number: {staffMember.phoneNumber}"
			
			# Creates the data dict of the user and staff
			data = {"id": staffMember.staffID, "first name": staffMember.firstName, "last name": staffMember.lastName, "address": staffMember.address, "phone number": staffMember.phoneNumber, "username": user.username, "admin": user.admin}

			# Creates the widgets for displaying the info
			usernameLabel = tk.Label(userFrame, text=f"username: {user.username}", bg=pallet.bg)			
			nameLaberl = tk.Label(userFrame, text=f"name: {staffMember.firstName} {staffMember.lastName}", bg=pallet.bg)
			infoButton = ttk.Button(userFrame, image=self.infoIcon, command=lambda infoText=infoText, data=data: popups.MessageBoxInfoEditButton("Staff member", infoText, lambda data=data: popups.StaffAndUserEdit(data)), style="generic.TButton")
			resetButton = ttk.Button(userFrame, text="Reset password", command=lambda user=user, index=index: self.resetPassword(user, index), style="generic.TButton")

			# Binds the mouse wheel to scroll the label on the widgets
			usernameLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/60)), "units"))
			nameLaberl.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/60)), "units"))
			infoButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/60)), "units"))
			resetButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/60)), "units"))
			
			# Places the widgets in the frame in a grid
			usernameLabel.grid(row=0, column=0)
			nameLaberl.grid(row=0, column=1)
			infoButton.grid(row=0, column=2)
			resetButton.grid(row=0, column=3)

			userFrame.pack(anchor="w")

			index += 1
		
		# Configures the scroll bar and canvas for a scroll container
		canvas.configure(yscrollcommand=scrollBar.set)
		canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
		canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/60)), "units"))
		canvas.create_window((0,0), window=accountsScrollFrame, anchor="nw")
		canvas.pack(fill="both", expand=1, side="left")
		scrollBar.pack(side="right", fill="y")
	
	# Used to reset the password to a new random password
	def resetPassword(self, user: User, index: int):
		# Generates a random password and sets it
		newPassword = self.randomPassword()
		user.password = newPassword

		# Opens the user file and reads the data
		with open("data/users.pkl", "br") as f:
			users = pickle.load(f)

		# Changes the user at the index to the updated version
		users[index] = user

		# Writes it to the file
		with open("data/users.pkl", "bw") as f:
			pickle.dump(users, f)
		
		# Shows an info box to say the password was rest and displays the newpassword
		messagebox.showinfo("Password rest", f"The password of account: {user.username}\nHas been reset to\n\n{newPassword}\n\nMake a note to log into the system")

	# Allows the user to add a new account
	def addUserAccount(self):
		# Gets the username and generates a random password
		username = self.newAccountUsernameEntry.get()
		password = self.randomPassword()

		# Creates the new user
		newUser = User(username, password)

		# Opens the user file and loads ths data
		with open("data/users.pkl", "br") as userFile:
			users: list[User] = pickle.load(userFile)
		
		# Adds the new user
		users.append(newUser)

		# Saves the new user
		with open("data/users.pkl", "bw") as userFile:
			pickle.dump(users, userFile)
		
		# Displays an info box to say that the account has been created and its random password
		messagebox.showinfo("New user password", f"The new user '{username}' has the password:\n\n{password}\n\nMake a note to log into the account")

	# Generates a random password
	def randomPassword(self):
		# Inalises variables, picks a random length and suffles a list of caharcters it can use
		password = ""
		length = random.randint(10, 20)
		characters = string.printable[:94]
		random.shuffle(list(characters))

		# Loops through the length and picks a random character
		for n in range(length):
			charNum = random.randint(0, len(characters)-1)
			password += characters[charNum]
		
		return password