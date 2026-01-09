from application import Application

from screens.login import Login


application = Application()
application.switchForm(Login)

#testWindow = Login(application)

#testWindow.mainLoop()

from dataTypes.user import User
import pickle


with open("data/users.pkl", "rb") as f:
    users = pickle.load(f)
    for user in users:
        print(user.getAtributes())
