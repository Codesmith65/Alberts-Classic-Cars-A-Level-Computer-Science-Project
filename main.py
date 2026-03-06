import screens
from application import Application


application = Application()
application.switchForm(screens.Search)

while application.running:
    application.currentScreen.mainLoop()
