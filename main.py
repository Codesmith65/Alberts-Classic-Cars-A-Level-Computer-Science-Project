import screens
from application import Application
import tkinter as tk



application = Application()
application.switchForm(screens.Booking)


while application.running:
    application.currentScreen.mainLoop()


#testWindow = Login(application)

#testWindow.mainLoop()

from dataTypes.user import User
import pickle

users=[]
with open("data/users.pkl", "rb") as f:
    users = pickle.load(f)
    for user in users:
        print(user.getAtributes())
