from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
	username: str
	password: str
	userID: UUID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return[self.userID, self.username]
	
	def checkCredentials(self, username: str, password: str) -> bool:
		#TODO potentialy add encryption to password
		if (username == self.username) & (password == self.password):
			return True
		
		return False
