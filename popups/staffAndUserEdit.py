import pickle
import tkinter
from tkinter import ttk, messagebox

from dataTypes.staff import Staff
from dataTypes.user import User


class StaffAndUserEdit:
    # Initilaistion function to creat the screen
    def __init__(self, data) -> None:
        # Open the data file find the data type
        with open("data/staff.pkl", "rb") as dataFile:
            dataTypes = pickle.load(dataFile)
        
        # Find the current user to edit in the file and its index
        self.currentDataType: Staff|None = None
        self.dataTypeIndex = 0
        for dataType in dataTypes:
            if dataType.staffID == data["id"]:
                self.currentDataType = dataType
                break
            
            self.dataTypeIndex += 1
        
        # Shows an error if the data type cannot be found
        if self.currentDataType == None:
            messagebox.showerror("Cannot find staff selected")
            return
        
        # Open the data file find the data type
        with open("data/users.pkl", "rb") as dataFile:
            dataTypes = pickle.load(dataFile)
        
        # Find the current user to edit in the file and its index
        self.currentDataTypeUser: User|None = None
        self.dataTypeIndexUser = 0
        for dataType in dataTypes:
            if dataType.userID == self.currentDataType.userID:
                self.currentDataTypeUser = dataType
                break
            
            self.dataTypeIndexUser += 1
        
        # Shows an error if the data type cannot be found
        if self.currentDataTypeUser == None:
            messagebox.showerror("Cannot find user selected")
            return
        
        # Create the ui window and frame, and set the title
        self.topLevel: tkinter.Toplevel = tkinter.Toplevel()

        self.topLevel.title(f"Staff and user edit - s:{self.currentDataType.staffID} & u:{self.currentDataType.userID}")
        self.topLevel.resizable(False, False)
        
        self.contentFrame: tkinter.Frame = tkinter.Frame(self.topLevel, padx=20, pady=10, background="white")
        self.buttonsFrame: tkinter.Frame = tkinter.Frame(self.topLevel)

        # Create all the widgets for the data type and places them and sets the current values
        ## -- Custome per data type between -- ##
        self.firstNameStrVar: tkinter.StringVar = tkinter.StringVar()
        self.lastNameStrVar: tkinter.StringVar = tkinter.StringVar()
        self.addressStrVar: tkinter.StringVar = tkinter.StringVar()
        self.phoneNumberStrVar: tkinter.StringVar = tkinter.StringVar()
        self.usernameStrVar: tkinter.StringVar = tkinter.StringVar()
        self.adminBoolVar: tkinter.BooleanVar = tkinter.BooleanVar()

        self.firstNameEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.firstNameStrVar)
        self.lastNameEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.lastNameStrVar)
        self.addressEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.addressStrVar)
        self.phoneNumberEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.phoneNumberStrVar)
        self.usernameEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.usernameStrVar)
        self.adminTickBox: ttk.Checkbutton = ttk.Checkbutton(self.contentFrame, variable=self.adminBoolVar, onvalue=1, offvalue=0)
        
        self.firstNameLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Fist name:")
        self.lastNameLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Last name:")
        self.addressLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Address:")
        self.phoneLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Phone number:")
        self.usernameLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Username:")
        self.adminLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Admin:")
        
        self.firstNameLabel.grid(row=0, column=0, padx=3, pady=3, sticky="e")
        self.lastNameLabel.grid(row=1, column=0, padx=3, pady=3, sticky="e")
        self.addressLabel.grid(row=2, column=0, padx=3, pady=3, sticky="e")
        self.phoneLabel.grid(row=3, column=0, padx=3, pady=3, sticky="e")
        self.usernameLabel.grid(row=4, column=0, padx=3, pady=3, sticky="e")
        self.adminLabel.grid(row=5, column=0, padx=3, pady=3, sticky="e")
        
        self.firstNameEntry.grid(row=0, column=1, padx=3, pady=3)
        self.lastNameEntry.grid(row=1, column=1, padx=3, pady=3)
        self.addressEntry.grid(row=2, column=1, padx=3, pady=3)
        self.phoneNumberEntry.grid(row=3, column=1, padx=3, pady=3)
        self.usernameEntry.grid(row=4, column=1, padx=3, pady=3)
        self.adminTickBox.grid(row=5, column=1, padx=3, pady=3)
        
        self.firstNameStrVar.set(data["first name"])
        self.lastNameStrVar.set(data["last name"])
        self.addressStrVar.set(data["address"])
        self.phoneNumberStrVar.set(data["phone number"])
        self.usernameStrVar.set(data["username"])
        self.adminBoolVar.set(data["admin"])

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
        self.currentDataType.firstName = self.firstNameStrVar.get()
        self.currentDataType.lastName = self.lastNameStrVar.get()
        self.currentDataType.address = self.addressStrVar.get()
        self.currentDataType.phoneNumber = self.phoneNumberStrVar.get()
        self.currentDataTypeUser.username = self.usernameStrVar.get()
        self.currentDataTypeUser.admin = self.adminBoolVar.get()
        ## -- Custome per data type between -- ##

        # Opens the data type file to retive data types
        with open("data/staff.pkl", "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)
        
        # Replaces the saved version with the updated version
        dataTypes[self.dataTypeIndex:self.dataTypeIndex+1] = [self.currentDataType]
        
        # Saves it back to file and closes the window
        with open("data/staff.pkl", "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
        
        # Opens the data type file to retive data types
        with open("data/users.pkl", "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)
        
        # Replaces the saved version with the updated version
        dataTypes[self.dataTypeIndexUser:self.dataTypeIndexUser+1] = [self.currentDataTypeUser]
        
        # Saves it back to file and closes the window
        with open("data/users.pkl", "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
            
        self.topLevel.destroy()
