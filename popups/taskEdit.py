import pickle
import tkinter
from tkinter import ttk, messagebox
import uuid

from dataTypes.task import Task


class TaskEdit:
    # Initilaistion function to creat the screen
    def __init__(self, data) -> None:
        # Open the data file find the data type
        self.filePath = "data/tasks.pkl"
        with open(self.filePath, "rb") as dataFile:
            dataTypes = pickle.load(dataFile)
        
        # Find the current user to edit in the file and its index
        self.currentDataType: Task|None = None
        self.dataTypeIndex = 0
        for dataType in dataTypes:
            if dataType.taskID == data["id"]:
                self.currentDataType = dataType
                break
            
            self.dataTypeIndex += 1
        
        # Shows an error if the data type cannot be found
        if self.currentDataType == None:
            messagebox.showerror("Cannot find user selected")
            return

        # Create the ui window and frame, and set the title
        self.topLevel: tkinter.Toplevel = tkinter.Toplevel()

        self.topLevel.title(f"Task edit - {self.currentDataType.taskID}")
        self.topLevel.resizable(False, False)
        
        self.contentFrame: tkinter.Frame = tkinter.Frame(self.topLevel, padx=20, pady=10, background="white")
        self.buttonsFrame: tkinter.Frame = tkinter.Frame(self.topLevel)        

        # Create all the widgets for the data type and places them and sets the current values
        ## -- Custome per data type between -- ##
        self.taskNameStrVar: tkinter.StringVar = tkinter.StringVar()
        self.taskDescriptionStrVar: tkinter.StringVar = tkinter.StringVar()
        self.completedBoolVar: tkinter.BooleanVar = tkinter.BooleanVar()
        self.parentTaskStrVar: tkinter.StringVar = tkinter.StringVar()
        self.staffIDStrVar: tkinter.StringVar = tkinter.StringVar()
        self.importanceStrVar: tkinter.StringVar = tkinter.StringVar()

        self.taskNameEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.taskNameStrVar)
        self.taskDescriptionEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.taskDescriptionStrVar)
        self.completedCheckButton: ttk.Checkbutton = ttk.Checkbutton(self.contentFrame, textvariable=self.completedBoolVar, onvalue=1, offvalue=0)
        self.parentTaskEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.parentTaskStrVar)
        self.staffIDEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.staffIDStrVar)
        self.importanceEntry: ttk.Entry = ttk.Entry(self.contentFrame, background="white", textvariable=self.importanceStrVar)
        
        self.taskNameLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Task name:")
        self.taskDescriptionLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Task description:")
        self.completedLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="completed:")
        self.parentTaskLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Parent task:")
        self.staffIDLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Staff id:")
        self.importanceLabel: ttk.Label = ttk.Label(self.contentFrame, background="white", text="Importance level:")
        
        self.taskNameLabel.grid(row=0, column=0, padx=3, pady=3, sticky="e")
        self.taskDescriptionLabel.grid(row=1, column=0, padx=3, pady=3, sticky="e")
        self.completedLabel.grid(row=2, column=0, padx=3, pady=3, sticky="e")
        self.parentTaskLabel.grid(row=3, column=0, padx=3, pady=3, sticky="e")
        self.staffIDLabel.grid(row=4, column=0, padx=3, pady=3, sticky="e")
        self.importanceLabel.grid(row=5, column=0, padx=3, pady=3, sticky="e")
        
        self.taskNameEntry.grid(row=0, column=1, padx=3, pady=3)
        self.taskDescriptionEntry.grid(row=1, column=1, padx=3, pady=3)
        self.completedCheckButton.grid(row=2, column=1, padx=3, pady=3)
        self.parentTaskEntry.grid(row=3, column=1, padx=3, pady=3)
        self.staffIDEntry.grid(row=4, column=1, padx=3, pady=3)
        self.importanceEntry.grid(row=5, column=1, padx=3, pady=3)
        
        self.taskNameStrVar.set(data["task name"])
        self.taskDescriptionStrVar.set(data["task description"])
        self.completedBoolVar.set(data["completed"])
        self.parentTaskStrVar.set(data["parent task"])
        self.staffIDStrVar.set(data["staff id"])
        self.importanceStrVar.set(data["importance"])

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
        self.currentDataType.taskName = self.taskNameStrVar.get()
        self.currentDataType.taskDescription = self.taskDescriptionStrVar.get()
        self.currentDataType.completed = self.completedBoolVar.get()
        self.currentDataType.parentTask = self.parentTaskStrVar.get()
        self.currentDataType.staffID = self.staffIDStrVar.get()
        self.currentDataType.importance = self.importanceStrVar.get()
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
            data: list[Task] = pickle.load(dataFile)
            
        newTask = Task("", "", False, uuid.uuid4(), uuid.uuid4())
        data.append(newTask)
        
        with open(self.filePath, "bw") as dataFile:
            pickle.dump(data, dataFile)
            
        TaskEdit(dict(zip(["id", "task name", "task description", "completed", "parent task", "staff id", "importance"], newTask.getAtributes())))
    
    def __delete(self):
        # Opens the data type file to retive data types
        with open(self.filePath, "rb") as dataTypeFile:
            dataTypes: list = pickle.load(dataTypeFile)

        dataTypes.pop(self.dataTypeIndex)
        self.topLevel.destroy()

        # Saves it back to file and closes the window
        with open(self.filePath, "wb") as dataTypeFile:
            pickle.dump(dataTypes, dataTypeFile)
