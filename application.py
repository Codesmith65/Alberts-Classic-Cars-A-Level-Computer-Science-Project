from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None = None
    
    def setLoggedInUser(self, userID: UUID|None) -> None:
        self.logedInUser = userID
