from application import Application

import tkinter as tk


class GenericScreen:
	def __init__(self, application: Application) -> None:
		self.application: Application = application
		self.root = tk.Tk()
		
		self.root.geometry("1000x600")
		self.root.resizable(False, False)
	
	def mainLoop(self) -> None:
		self.root.mainloop()