import tkinter
from tkinter import ttk


class MessageBoxInfoEditButton:
    def __init__(self, title, text, editCallback) -> None:
        self.topLevel: tkinter.Toplevel = tkinter.Toplevel()

        self.topLevel.title(title)
        
        self.contentFrame: tkinter.Frame = tkinter.Frame(self.topLevel, padx=20, pady=10, background="white")
        self.buttonsFrame: tkinter.Frame = tkinter.Frame(self.topLevel)
        
        self.icon: tkinter.Label = tkinter.Label(self.contentFrame, image="::tk::icons::information", justify="left", background="white")
        self.infoLable: tkinter.Label = tkinter.Label(self.contentFrame, text=text, justify="left", background="white")
        
        self.okButton: ttk.Button = ttk.Button(self.buttonsFrame, text="OK", command=self.topLevel.destroy)
        self.editButton: ttk.Button = ttk.Button(self.buttonsFrame, text="Edit", command=editCallback)
        
        self.icon.grid(row=0, column=0, padx=2, pady=2, sticky="n")
        self.infoLable.grid(row=0, column=1)
        
        self.editButton.grid(row=0, column=0)
        self.okButton.grid(row=0, column=1)
        
        self.contentFrame.pack()
        self.buttonsFrame.pack(expand=True, anchor="e", padx=15, pady=10)
    