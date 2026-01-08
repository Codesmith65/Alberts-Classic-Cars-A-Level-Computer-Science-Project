import tkinter as tk
from tkinter import ttk
from .generic import Generic


class Login(Generic):
	def __init__(self) -> None:
		super().__init__()

		self.root.title("Albert's Classic Car - Login")

		self.leftFrame = tk.Frame(self.root)
		self.rightFrame = tk.Frame(self.root)
		self.loginFrame = tk.Frame(self.rightFrame)

		self.loginTitleLabel = tk.Label(self.loginFrame)
		self.usernameEntry = tk.Entry(self.loginFrame)
		self.passwordEntry = tk.Entry(self.loginFrame)
		self.loginButton = tk.Button(self.loginFrame)
		self.forgotPasswordLabel = tk.Label(self.loginFrame)


		self.loginTitleLabel["text"] = "Login"
		self.loginTitleLabel["font"] = ("Helvetica", 40)
		self.loginButton["text"] = "Login"
		self.forgotPasswordLabel["text"] = "Forgot password? Contact admin."


		self.rightFrame.pack()
		self.loginFrame.pack()

		self.loginTitleLabel.pack()
		self.usernameEntry.pack()
		self.passwordEntry.pack()
		self.loginButton.pack()
		self.forgotPasswordLabel.pack()