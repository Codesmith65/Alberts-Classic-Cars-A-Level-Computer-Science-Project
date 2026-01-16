import screens
from application import Application




application = Application()
application.switchForm(screens.Login)


while application.running:
    application.currentScreen.mainLoop()


#testWindow = Login(application)

#testWindow.mainLoop()

from dataTypes.user import User
import pickle


with open("data/users.pkl", "rb") as f:
    users = pickle.load(f)
    for user in users:
        print(user.getAtributes())
