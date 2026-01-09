import tkinter as tk
from tkinter import ttk
from .generic import Generic
from ..application import Application


class Login(Generic):
	def __init__(self, application: Application) -> None:
		super().__init__(application)

		self.root.title("Albert's Classic Car - Login")

		self.leftFrame: tk.Frame = tk.Frame(self.root)
		self.rightFrame: tk.Frame = tk.Frame(self.root)
		self.loginFrame: tk.Frame = tk.Frame(self.rightFrame)

		self.loginTitleLabel: tk.Label = tk.Label(self.loginFrame)
		self.usernameEntry: tk.Entry = tk.Entry(self.loginFrame)
		self.passwordEntry: tk.Entry = tk.Entry(self.loginFrame)
		self.loginButton: tk.Button = tk.Button(self.loginFrame)
		self.forgotPasswordLabel: tk.Label = tk.Label(self.loginFrame)


		self.loginTitleLabel["text"] = "Login"
		self.loginTitleLabel["font"] = ("Helvetica", 40)
		self.loginButton["text"] = "Login"
		self.forgotPasswordLabel["text"] = "Forgot password? Contact admin."

		self.loginButton["command"] = self.login


		self.rightFrame.pack()
		self.loginFrame.pack()

		self.loginTitleLabel.pack()
		self.usernameEntry.pack()
		self.passwordEntry.pack()
		self.loginButton.pack()
		self.forgotPasswordLabel.pack()