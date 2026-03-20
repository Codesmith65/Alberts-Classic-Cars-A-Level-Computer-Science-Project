import screens
from application import Application
import uuid


application = Application()
application.switchForm(screens.Task, {"BookingID": uuid.UUID("9cca727b-5030-487b-b6d6-b346064c9bdb")})

while application.running:
    application.currentScreen.mainLoop()
