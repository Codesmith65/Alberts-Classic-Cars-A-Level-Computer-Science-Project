import screens
from application import Application


application = Application()
application.switchForm(screens.Login)

while application.running:
    application.currentScreen.mainLoop()
