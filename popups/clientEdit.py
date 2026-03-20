import pickle
import tkinter
from tkinter import ttk, messagebox

from dataTypes.client import Client


class ClientEdit:
    # Initilaistion function to creat the screen
    def __init__(self, data) -> None:
        # Open the data file find the data type
        self.filePath = "data/clients.pkl"
        with open(self.filePath, "rb") as dataFile:
            dataTypes = pickle.load(dataFile)
        
        # Find the current user to edit in the file and its index
        self.currentDataType: Client|None = None
        self.dataTypeIndex = 0
        for dataType in dataTypes:
            if dataType.clientID == data["id"]:
                self.currentDataType = dataType
                break
            
            self.dataTypeIndex += 1
        
        # Shows an error if the data type cannot be found
        if self.currentDataType == None:
            messagebox.showerror("Cannot find user selected")
            return

        # Create the ui window and frame, and set the title
        self.topLevel: tkinter.Toplevel = tkinter.Toplevel()

        self.topLevel.title(f"Client edit - {self.currentDataType.clientID}")
        self.topLevel.resizable(False, False)
        
        self.contentFrame: tkinter.Frame = tkinter.Frame(self.topLevel, padx=20, pady=10, background="white")
        self.buttonsFrame: tkinter.Frame = tkinter.Frame(self.topLevel)        

        # Create all the widgets for the data type and places them and sets the current values
        ## -- Custome per data type between -- ##
        self.firstNameStrVar: tkinter.StringVar = tkinter.StringVar()
        self.lastNameStrVar: tkinter.StringVar = tkinter.StringVar()
        self.emailStrVar: tkinter.StringVar = tkinter.StringVar()
        self.addressStrVar: tkinter.StringVar = tkinter.StringVar()
        self.phoneNumberStrVar: tkinter.StringVar = tkinter.StringVar()

        self.firstNameEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.firstNameStrVar)
        self.lastNameEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.lastNameStrVar)
        self.emailEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.emailStrVar)
        self.addressEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.addressStrVar)
        self.phoneNumberEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.phoneNumberStrVar)
        
        self.firstNameLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Fist name:")
        self.lastNameLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Last name:")
        self.emailLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Email:")
        self.addressLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Address:")
        self.phoneLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Phone number:")
        
        self.firstNameLabel.grid(row=0, column=0, padx=3, pady=3, sticky="e")
        self.lastNameLabel.grid(row=1, column=0, padx=3, pady=3, sticky="e")
        self.emailLabel.grid(row=2, column=0, padx=3, pady=3, sticky="e")
        self.addressLabel.grid(row=3, column=0, padx=3, pady=3, sticky="e")
        self.phoneLabel.grid(row=4, column=0, padx=3, pady=3, sticky="e")
        
        self.firstNameEntry.grid(row=0, column=1, padx=3, pady=3)
        self.lastNameEntry.grid(row=1, column=1, padx=3, pady=3)
        self.emailEntry.grid(row=2, column=1, padx=3, pady=3)
        self.addressEntry.grid(row=3, column=1, padx=3, pady=3)
        self.phoneNumberEntry.grid(row=4, column=1, padx=3, pady=3)
        
        self.firstNameStrVar.set(data["first name"])
        self.lastNameStrVar.set(data["last name"])
        self.emailStrVar.set(data["email"])
        self.addressStrVar.set(data["address"])
        self.phoneNumberStrVar.set(data["phone number"])

        ## -- Custome per data type between -- ##
        
        # Creats and diplays the save and cancel buttons and also adds the frames to the screen
        self.newButton: ttk.Button = ttk.Button(self.buttonsFrame, text="New", command=self.__new)
        self.deleteButton: ttk.Button = ttk.Button(self.buttonsFrame, text="Delete", command=self.__delete)
        self.saveButton: ttk.Button = ttk.Button(self.buttonsFrame, text="Save", command=self.__save)
        self.cancelButton: ttk.Button = ttk.Button(self.buttonsFrame, text="Cancel", command=self.topLevel.destroy)      

        self.newButton.grid(row=0, column=0, padx=2)
        self.deleteButton.grid(row=0, column=1, padx=2)
        self.saveButton.grid(row=0, column=2, padx=2)
        self.cancelButton.grid(row=0, column=3, padx=2)
        
        self.contentFrame.pack(fill="x")
        self.buttonsFrame.pack(expand=True, anchor="e", padx=15, pady=10)
    
    # Used to save the data that was edited
    def __save(self):
        # Gets all the values and updates the data type
        ## -- Custome per data type between -- ##
        self.currentDataType.firstName = self.firstNameStrVar.get()
        self.currentDataType.lastName = self.lastNameStrVar.get()
        self.currentDataType.email = self.emailStrVar.get()
        self.currentDataType.address = self.addressStrVar.get()
        self.currentDataType.phoneNumber = self.phoneNumberStrVar.get()
        ## -- Custome per data type between -- ##

        # Opens the data type file to retive data types
        with open(self.filePath, "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)
        
        # Replaces the saved version with the updated version
        dataTypes[self.dataTypeIndex:self.dataTypeIndex+1] = [self.currentDataType]
        
        # Saves it back to file and closes the window
        with open(self.filePath, "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
            
        self.topLevel.destroy()
    
    # Used to creae a new version of the data type to be edited
    def __new(self):
        with open(self.filePath, "br") as dataFile:
            data: list[Client] = pickle.load(dataFile)
            
        newClient = Client("", "", "", "", "")
        data.append(newClient)
        
        with open(self.filePath, "bw") as dataFile:
            pickle.dump(data, dataFile)
            
        ClientEdit(dict(zip(["id", "first name", "last name", "email", "address", "phone number"], newClient.getAtributes())))
    
    def __delete(self):
        # Opens the data type file to retive data types
        with open(self.filePath, "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)

        dataTypes.pop(self.dataTypeIndex)
        self.topLevel.destroy()

        # Saves it back to file and closes the window
        with open(self.filePath, "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
