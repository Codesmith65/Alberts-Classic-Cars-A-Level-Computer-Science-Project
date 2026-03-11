from dataclasses import KW_ONLY, dataclass
from uuid import UUID, uuid4


@dataclass
class User:
	username: str
	password: str
	_: KW_ONLY
	admin: bool = False
	userID: UUID|None = None
	
	def __post_init__(self):
		if self.userID is None:
			self.userID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return[self.userID, self.username]
	
	def checkCredentials(self, username: str, password: str) -> bool:
		#TODO potentialy add encryption to password
		if (username == self.username) & (password == self.password):
			return True
		
		return False
