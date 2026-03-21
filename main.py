import screens
from application import Application
import uuid


application = Application()
application.switchForm(screens.Login)

while application.running:
    application.currentScreen.mainLoop()
