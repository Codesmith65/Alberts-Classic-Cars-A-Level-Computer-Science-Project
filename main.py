from screens.account import Account

testWindow = Account()

testWindow.mainLoop()

from dataTypes.user import User
import pickle


with open("data/users.pkl", "rb") as f:
    users = pickle.load(f)
    for user in users:
        print(user.getAtributes())
