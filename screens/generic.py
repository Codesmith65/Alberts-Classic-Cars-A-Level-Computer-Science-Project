import tkinter as tk
from application import Application


class GenericScreen:
	def __init__(self, application: Application) -> None:
		self.application = application
		self.root = tk.Tk()
		
		self.root.geometry("1000x600")
		self.root.resizable(False, False)
	
	def mainLoop(self) -> None:
		self.root.mainloop()