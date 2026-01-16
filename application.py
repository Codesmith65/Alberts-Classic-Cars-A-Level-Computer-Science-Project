from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from screens.generic import GenericScreen
    
from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None = None
        self.currentScreen: GenericScreen|None = None
        
        self.running: bool = True
    
    def setLoggedInUser(self, userID: UUID|None) -> None:
        self.logedInUser = userID

    def switchForm(self, newForm: GenericScreen) -> None:
        if self.currentScreen != None:
            self.currentScreen.root.destroy()
        
        self.currentScreen = newForm(self)
