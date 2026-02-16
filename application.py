from __future__ import annotations #https://stackoverflow.com/questions/744373/what-happens-when-using-mutual-or-circular-cyclic-imports/67673741#67673741
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from screens.generic import GenericScreen
    
from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None = UUID("d8eec26b-91c3-4144-b2f7-97ec1f20d064")
        self.loggedInStaff: UUID|None = UUID("e22e4c85-589f-4370-b052-599cb3dabbc9")
        self.currentScreen: GenericScreen|None = None
        self.crossScreenDataStore: dict = {}
        
        self.running: bool = True
    
    def setLoggedInUser(self, userID: UUID|None) -> None:
        self.logedInUser = userID
    
    def setLoggedInStaff(self, staffID: UUID|None) ->None:
        self.loggedInStaff = staffID

    def switchForm(self, newForm: GenericScreen, crossScreenData: dict) -> None:
        self.crossScreenDataStore.clear()
        self.crossScreenDataStore = crossScreenData

        if self.currentScreen != None:
            self.currentScreen.root.destroy()
        
        self.currentScreen: GenericScreen = newForm(self)
        
        self.currentScreen.root.protocol("WM_DELETE_WINDOW", self.closeWindow)
    
    def closeWindow(self):
        self.running = False
        self.currentScreen.root.destroy()
