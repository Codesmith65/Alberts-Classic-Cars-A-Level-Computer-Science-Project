import tkinter as tk


class Generic:
	def __init__(self) -> None:
		self.root = tk.Tk()
		
		self.root.geometry("1000x600")
		self.root.resizable(False, False)
	
	def mainLoop(self) -> None:
		self.root.mainloop()