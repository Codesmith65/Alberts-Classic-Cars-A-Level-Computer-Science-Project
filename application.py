from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from screens.generic import GenericScreen
    
from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None = None
    
    def setLoggedInUser(self, userID: UUID|None) -> None:
        self.logedInUser = userID
