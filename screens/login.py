import tkinter as tk
from tkinter import ttk
from .generic import Generic


class Login(Generic):
	def __init__(self) -> None:
		super().__init__()

		self.root.title("Albert's Classic Car - Login")

		self.leftFrame = tk.Frame()
		self.rightFrame = tk.Frame()
		self.loginFrame = tk.Frame(self.rightFrame)

		self.rightFrame.pack()
		self.loginFrame.pack()

		self.loginText = ttk.Label(self.loginFrame)
		self.usernameEntry = tk.Entry(self.loginFrame)
		self.passwordEntry = tk.Entry(self.loginFrame)
		self.forgotPasswordLabel = ttk.Label(self.loginFrame)

		self.loginText["text"] = "Login"
		self.loginText["font"] = ("Helvetica", 40)
		self.forgotPasswordLabel["text"] = "Forgot password? Contact admin."


		self.loginText.pack()
		self.usernameEntry.pack()
		self.passwordEntry.pack()
		self.forgotPasswordLabel.pack()