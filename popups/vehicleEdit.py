import pickle
import tkinter
from tkinter import ttk, messagebox
from turtle import back

from dataTypes.vehicle import Vehicle


class VehicleEdit:
    # Initilaistion function to creat the screen
    def __init__(self, data) -> None:
        # Open the data file find the data type
        with open("data/vehicles.pkl", "rb") as dataFile:
            dataTypes = pickle.load(dataFile)
        
        # Find the current user to edit in the file and its index
        self.currentDataType: Vehicle|None = None
        self.dataTypeIndex = 0
        for dataType in dataTypes:
            if dataType.vehicleID == data["id"]:
                self.currentDataType = dataType
                break
            
            self.dataTypeIndex += 1
        
        # Shows an error if the data type cannot be found
        if self.currentDataType == None:
            messagebox.showerror("Cannot find vehicle selected")
            return

        # Create the ui window and frame, and set the title
        self.topLevel: tkinter.Toplevel = tkinter.Toplevel()

        self.topLevel.title(f"Vehicle edit - {self.currentDataType.vehicleID}")
        self.topLevel.resizable(False, False)
        
        self.contentFrame: tkinter.Frame = tkinter.Frame(self.topLevel, padx=20, pady=10, background="white")
        self.buttonsFrame: tkinter.Frame = tkinter.Frame(self.topLevel)

        # Create all the widgets for the data type and places them and sets the current values
        ## -- Custome per data type between -- ##
        self.makeStrVar: tkinter.StringVar = tkinter.StringVar()
        self.modelStrVar: tkinter.StringVar = tkinter.StringVar()
        self.colourStrVar: tkinter.StringVar = tkinter.StringVar()
        self.registrationStrVar: tkinter.StringVar = tkinter.StringVar()
        self.vinNumberStrVar: tkinter.StringVar = tkinter.StringVar()

        self.makeEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.makeStrVar)
        self.modelEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.modelStrVar)
        self.colourEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.colourStrVar)
        self.registrationEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.registrationStrVar)
        self.vinNumberEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.vinNumberStrVar)
        
        self.makeLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Make:")
        self.modelLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Model:")
        self.colourLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Colour:")
        self.registrationLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Registration:")
        self.vinLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Vin:")
        
        self.makeLabel.grid(row=0, column=0, padx=3, pady=3, sticky="e")
        self.modelLabel.grid(row=1, column=0, padx=3, pady=3, sticky="e")
        self.colourLabel.grid(row=2, column=0, padx=3, pady=3, sticky="e")
        self.registrationLabel.grid(row=3, column=0, padx=3, pady=3, sticky="e")
        self.vinLabel.grid(row=4, column=0, padx=3, pady=3, sticky="e")
        
        self.makeEntry.grid(row=0, column=1, padx=3, pady=3)
        self.modelEntry.grid(row=1, column=1, padx=3, pady=3)
        self.colourEntry.grid(row=2, column=1, padx=3, pady=3)
        self.registrationEntry.grid(row=3, column=1, padx=3, pady=3)
        self.vinNumberEntry.grid(row=4, column=1, padx=3, pady=3)
        
        self.makeStrVar.set(data["make"])
        self.modelStrVar.set(data["model"])
        self.colourStrVar.set(data["colour"])
        self.registrationStrVar.set(data["registration"])
        self.vinNumberStrVar.set(data["vin"])

        ## -- Custome per data type between -- ##
        
        # Creats and diplays the save and cancel buttons and also adds the frames to the screen
        self.saveButton: ttk.Button = ttk.Button(self.buttonsFrame, text="Save", command=self.__save)
        self.cancelButton: ttk.Button = ttk.Button(self.buttonsFrame, text="Cancel", command=self.topLevel.destroy)
        
        self.saveButton.grid(row=0, column=0, padx=2)
        self.cancelButton.grid(row=0, column=1, padx=2)
        
        self.contentFrame.pack()
        self.buttonsFrame.pack(expand=True, anchor="e", padx=15, pady=10)
    
    # Used to save the data that was edited
    def __save(self):
        # Gets all the values and updates the data type
        ## -- Custome per data type between -- ##
        self.currentDataType.make = self.makeStrVar.get()
        self.currentDataType.model = self.modelStrVar.get()
        self.currentDataType.colour = self.colourStrVar.get()
        self.currentDataType.registration = self.registrationStrVar.get()
        self.currentDataType.vin = self.vinNumberStrVar.get()
        ## -- Custome per data type between -- ##

        # Opens the data type file to retive data types
        with open("data/vehicles.pkl", "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)
        
        # Replaces the saved version with the updated version
        dataTypes[self.dataTypeIndex:self.dataTypeIndex+1] = [self.currentDataType]
        
        # Saves it back to file and closes the window
        with open("data/vehicles.pkl", "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
            
        self.topLevel.destroy()
