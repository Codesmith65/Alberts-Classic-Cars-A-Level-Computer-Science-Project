import pickle
import tkinter
from tkinter import ttk, messagebox
from turtle import back
import datetime

from dataTypes.booking import Booking


class BookingEdit:
    # Initilaistion function to creat the screen
    def __init__(self, data) -> None:
        # Open the data file find the data type
        with open("data/bookings.pkl", "rb") as dataFile:
            dataTypes = pickle.load(dataFile)
        
        # Find the current user to edit in the file and its index
        self.currentDataType: Booking|None = None
        self.dataTypeIndex = 0
        for dataType in dataTypes:
            if dataType.bookingID == data["id"]:
                self.currentDataType = dataType
                break
            
            self.dataTypeIndex += 1
        
        # Shows an error if the data type cannot be found
        if self.currentDataType == None:
            messagebox.showerror("Cannot find user selected")
            return

        # Create the ui window and frame, and set the title
        self.topLevel: tkinter.Toplevel = tkinter.Toplevel()

        self.topLevel.title(f"Booking edit - {self.currentDataType.bookingID}")
        self.topLevel.resizable(False, False)
        
        self.contentFrame: tkinter.Frame = tkinter.Frame(self.topLevel, padx=20, pady=10, background="white")
        self.buttonsFrame: tkinter.Frame = tkinter.Frame(self.topLevel)

        # Create all the widgets for the data type and places them and sets the current values
        ## -- Custome per data type between -- ##
        self.staffIDStrVar: tkinter.StringVar = tkinter.StringVar()
        self.clientIDStrVar: tkinter.StringVar = tkinter.StringVar()
        self.vehicleIDStrVar: tkinter.StringVar = tkinter.StringVar()
        self.pickUpDateStrVar: tkinter.StringVar = tkinter.StringVar()
        self.pickUpLocationStrVar: tkinter.StringVar = tkinter.StringVar()
        self.dropOffDateStrVar: tkinter.StringVar = tkinter.StringVar()
        self.dropOffLocationStrVar: tkinter.StringVar = tkinter.StringVar()

        self.staffIDEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.staffIDStrVar)
        self.clientIDEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.clientIDStrVar)
        self.vehicleIDEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.vehicleIDStrVar)
        self.pickUpDateEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.pickUpDateStrVar)
        self.pickUpLocationEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.pickUpLocationStrVar)
        self.dropOffDateEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.dropOffDateStrVar)
        self.dropOffLocationEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.dropOffLocationStrVar)
        self.statusDropDown: ttk.Combobox = ttk.Combobox(self.contentFrame, background="white", state="readonly", values=["Booked", "Deposite paid", "Balanced paid", "Ready", "Complted", "Cancled"])

        self.staffIDLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Staff ID:")
        self.clientIDLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Client ID:")
        self.vehicleIDLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Vehicle ID:")
        self.pickUpDateLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Pickup date:")
        self.pickupLocationLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Pickup location:")
        self.dropoffDateLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Dropoff date:")
        self.dropoffLocationLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Dropoff location:")
        self.statusLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Status:")
        
        self.staffIDLabel.grid(row=0, column=0, padx=3, pady=3, sticky="e")
        self.clientIDLabel.grid(row=1, column=0, padx=3, pady=3, sticky="e")
        self.vehicleIDLabel.grid(row=2, column=0, padx=3, pady=3, sticky="e")
        self.pickUpDateLabel.grid(row=3, column=0, padx=3, pady=3, sticky="e")
        self.pickupLocationLabel.grid(row=4, column=0, padx=3, pady=3, sticky="e")
        self.dropoffDateLabel.grid(row=5, column=0, padx=3, pady=3, sticky="e")
        self.dropoffLocationLabel.grid(row=6, column=0, padx=3, pady=3, sticky="e")
        self.statusLabel.grid(row=7, column=0, padx=3, pady=3, sticky="e")
        
        self.staffIDEntry.grid(row=0, column=1, padx=3, pady=3)
        self.clientIDEntry.grid(row=1, column=1, padx=3, pady=3)
        self.vehicleIDEntry.grid(row=2, column=1, padx=3, pady=3)
        self.pickUpDateEntry.grid(row=3, column=1, padx=3, pady=3)
        self.pickUpLocationEntry.grid(row=4, column=1, padx=3, pady=3)
        self.dropOffDateEntry.grid(row=5, column=1, padx=3, pady=3)
        self.dropOffLocationEntry.grid(row=6, column=1, padx=3, pady=3)
        self.statusDropDown.grid(row=7, column=1, padx=3, pady=3)
        
        self.staffIDStrVar.set(data["staff id"])
        self.clientIDStrVar.set(data["client id"])
        self.vehicleIDStrVar.set(data["vehicle id"])
        self.pickUpDateStrVar.set(f"{datetime.datetime.fromtimestamp(self.currentDataType.pickupDate):%d/%m/%Y}")
        self.pickUpLocationStrVar.set(data["pickup location id"])
        self.dropOffDateStrVar.set(f"{datetime.datetime.fromtimestamp(self.currentDataType.dropoffDate):%d/%m/%Y}")
        self.dropOffLocationStrVar.set(data["dropoff location id"])
        self.statusDropDown.set(data["status"])

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
        self.currentDataType.staffID = self.staffIDStrVar.get()
        self.currentDataType.clientID = self.clientIDStrVar.get()
        self.currentDataType.vehicleID = self.vehicleIDStrVar.get()
        self.currentDataType.pickupDate = datetime.datetime.strptime(self.pickUpDateStrVar.get(), "%d/%m/%Y").timestamp()
        self.currentDataType.pickupLocation = self.pickUpLocationStrVar.get()
        self.currentDataType.dropoffDate = datetime.datetime.strptime(self.dropOffDateStrVar.get(), "%d/%m/%Y").timestamp()
        self.currentDataType.dropoffLocation = self.dropOffLocationStrVar.get()
        self.currentDataType.status = self.statusDropDown.get()
        ## -- Custome per data type between -- ##

        # Opens the data type file to retive data types
        with open("data/bookings.pkl", "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)
        
        # Replaces the saved version with the updated version
        dataTypes[self.dataTypeIndex:self.dataTypeIndex+1] = [self.currentDataType]
        
        # Saves it back to file and closes the window
        with open("data/bookings.pkl", "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
            
        self.topLevel.destroy()
