from uuid import UUID


class Application:
    def __init__(self) -> None:
        self.logedInUser: UUID|None = None
