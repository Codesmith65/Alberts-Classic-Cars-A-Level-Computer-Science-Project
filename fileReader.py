import pickle
import os.path


dataFolderPath = "K:\\A-Level Course Work\\Alberts-Classic-Cars-A-Level-Computer-Science-Project\\data\\"

running = True
while running:
    fileName = input("Enter file name: ")
    
    filePath = dataFolderPath + fileName
    
    if not os.path.isfile(filePath):
        print("No file found")
        continue
    
    with open(filePath, "rb") as f:
        fileData = pickle.load(f)
    
    for record in fileData:
        print(record)