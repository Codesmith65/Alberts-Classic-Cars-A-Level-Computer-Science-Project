from __future__ import annotations #https://stackoverflow.com/questions/744373/what-happens-when-using-mutual-or-circular-cyclic-imports/67673741#67673741
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from screens.generic import GenericScreen
    
from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None = UUID("b40fe4be-ad61-45a8-8692-494a568be704")
        self.currentScreen: GenericScreen|None = None
        
        self.running: bool = True
    
    def setLoggedInUser(self, userID: UUID|None) -> None:
        self.logedInUser = userID

    def switchForm(self, newForm: GenericScreen) -> None:
        if self.currentScreen != None:
            self.currentScreen.root.destroy()
        
        self.currentScreen: GenericScreen = newForm(self)
        
        self.currentScreen.root.protocol("WM_DELETE_WINDOW", self.closeWindow)
    
    def closeWindow(self):
        self.running = False
        self.currentScreen.root.destroy()
