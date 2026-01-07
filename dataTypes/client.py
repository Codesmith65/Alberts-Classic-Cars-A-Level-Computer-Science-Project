from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Client:
	firstName: str
	lastName: str
	email: str
	address: str
	phoneNumber: str
	clientID: UUID = uuid4()

	def getAtributes(self) -> list[str | UUID]:
		return [self.clientID, self.firstName, self.lastName, self.email, self.address, self.phoneNumber]
	