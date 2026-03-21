from __future__ import annotations #https://stackoverflow.com/questions/744373/what-happens-when-using-mutual-or-circular-cyclic-imports/67673741#67673741
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from screens.generic import GenericScreen
    
from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None
        self.loggedInStaff: UUID|None
        self.currentScreen: GenericScreen|None = None
        self.crossScreenDataStore: dict = {}
        
        self.running: bool = True
    
    # Sets the user which is loged in
    def setLoggedInUser(self, userID: UUID|None) -> None:
        self.logedInUser = userID
    
    # Sets the staf which is loged in
    def setLoggedInStaff(self, staffID: UUID|None) ->None:
        self.loggedInStaff = staffID

    # Swu=itches form
    def switchForm(self, newForm: GenericScreen, crossScreenData: dict = {}) -> None:
        # Crears the data store and sets it to new data
        self.crossScreenDataStore.clear()
        self.crossScreenDataStore = crossScreenData

        # Destroys the old screen
        if self.currentScreen != None:
            self.currentScreen.root.destroy()
        
        # Opems the new screen
        self.currentScreen: GenericScreen = newForm(self)
        
        # Attaches to the close event
        self.currentScreen.root.protocol("WM_DELETE_WINDOW", self.closeWindow)
    
    # Attached to the close event to know when to stop the infinte loop and destroys the window
    def closeWindow(self):
        self.running = False
        self.currentScreen.root.destroy()
