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


class Account(GenericScreen):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Accounts")

		self.infoIcon = tk.PhotoImage(file="assets/info.png")

		self.topBarFrame = tk.Frame(self.root)
		self.mainContectFrame = tk.Frame(self.root)

		self.companyLogo = tk.PhotoImage(file="assets/logo.png")
		self.companyLogoHomeButton = tk.Button(self.topBarFrame)
		self.titleLabel = tk.Label(self.topBarFrame)
		self.logOutButton = ttk.Button(self.topBarFrame)
		
		self.newAccountLabelFrame = tk.LabelFrame(self.mainContectFrame)
		self.accountsLabelFrame = tk.LabelFrame(self.mainContectFrame)
		
		self.newAccountUsernameEntry = ttk.Entry(self.newAccountLabelFrame)
		self.newAccountUsernameLabel = ttk.Label(self.newAccountLabelFrame)
		self.newAccountCreateButton = ttk.Button(self.newAccountLabelFrame)

		self.populateAccounts()


		self.companyLogoHomeButton["image"] = self.companyLogo
		self.companyLogoHomeButton["relief"] = "flat"
		self.companyLogoHomeButton["borderwidth"] = 0
		self.companyLogoHomeButton["width"] = 50
		self.companyLogoHomeButton["height"] = 50
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
		

		self.topBarFrame.pack()
		#fill="both", expand=1, anchor="center")

		self.companyLogoHomeButton.pack()
		self.titleLabel.pack()
		self.logOutButton.pack()
		
		self.newAccountLabelFrame.pack(side="left", expand=1)
		self.newAccountUsernameLabel.grid(row=0, column=0)
		self.newAccountUsernameEntry.grid(row=0, column=1)
		self.newAccountCreateButton.grid(row=1, column=0, columnspan=2)
		
		self.accountsLabelFrame.pack(side="right", fill="both", expand=1)

		self.mainContectFrame.pack(fill="both", expand=1)
	
	def goHome(self):
		self.application.switchForm(screens.Home)
	
	def logOut(self):
		self.application.switchForm(screens.Login)
		self.application.setLoggedInStaff(None)
		self.application.setLoggedInUser(None)
	
	def populateAccounts(self):
		with open("data/staff.pkl", "br") as staffFile:
			staff: list[Staff] = pickle.load(staffFile)
		
		userIdToStaffIndex = {}
		index = 0
		for staffMember in staff:
			userIdToStaffIndex[staffMember.userID] = index
			index += 1

		with open("data/users.pkl", "br") as userFile:
			users: list[User] = pickle.load(userFile)
		
		canvas: tk.Canvas = tk.Canvas(self.accountsLabelFrame)
		accountsScrollFrame = tk.Frame(canvas)
		scrollBar: tk.Scrollbar = tk.Scrollbar(self.accountsLabelFrame, orient=tk.VERTICAL, command=canvas.yview)
		
		index = 0
		for user in users:
			staffMember = staff[userIdToStaffIndex[user.userID]]
			userFrame = tk.Frame(accountsScrollFrame)

			infoText = f"username: {user.username}\nname: {staffMember.firstName} {staffMember.lastName}\n" \
			f"userID: {user.userID}\nstaffID: {staffMember.staffID}"

			tk.Label(userFrame, text=f"username: {user.username}").grid(row=0, column=0)
			tk.Label(userFrame, text=f"name: {staffMember.firstName} {staffMember.lastName}").grid(row=0, column=1)
			tk.Button(userFrame, image=self.infoIcon, command=lambda: popups.MessageBoxInfoEditButton("Staff member", infoText, print)).grid(row=0, column=2)
			ttk.Button(userFrame, text="Reset password", command=lambda user=user, index=index: self.resetPassword(user, index)).grid(row=0, column=3)

			userFrame.pack(anchor="w")

			index += 1
		
		canvas.configure(yscrollcommand=scrollBar.set)
		canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
		canvas.create_window((0,0), window=accountsScrollFrame, anchor="nw")
		canvas.pack(fill="both", expand=1, side="left")
		scrollBar.pack(side="right", fill="y")
		
	def resetPassword(self, user: User, index: int):
		newPassword = self.randomPassword()

		user.password = newPassword

		with open("data/users.pkl", "br") as f:
			users = pickle.load(f)

		users[index] = user

		with open("data/users.pkl", "bw") as f:
			pickle.dump(users, f)
		
		messagebox.showinfo("Password rest", f"The password of account: {user.username}\nHas been reset to\n\n{newPassword}\n\nMake a note to log into the system")

	def addUserAccount(self):
		username = self.newAccountUsernameEntry.get()
		password = self.randomPassword()

		newUser = User(username, password)

		with open("data/users.pkl", "br") as userFile:
			users: list[User] = pickle.load(userFile)
		
		users.append(newUser)

		with open("data/users.pkl", "bw") as userFile:
			pickle.dump(users, userFile)
		
		messagebox.showinfo("New user password", f"The new user '{username}' has the password:\n\n{password}\n\nMake a note to log into the account")

	def randomPassword(self):
		password = ""
		length = random.randint(10, 20)
		characters = string.printable[:94]
		random.shuffle(list(characters))

		for n in range(length):
			charNum = random.randint(0, len(characters)-1)
			password += characters[charNum]
		
		return password