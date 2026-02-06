from dataclasses import KW_ONLY, dataclass
from uuid import UUID, uuid4


@dataclass
class Client:
	firstName: str
	lastName: str
	email: str
	address: str
	phoneNumber: str
	_: KW_ONLY
	clientID: UUID|None = None
	
	def __post_init__(self):
		if self.clientID is None:
			self.clientID = uuid4()

	def getAtributes(self) -> list[str | UUID]:
		return [self.clientID, self.firstName, self.lastName, self.email, self.address, self.phoneNumber]
	