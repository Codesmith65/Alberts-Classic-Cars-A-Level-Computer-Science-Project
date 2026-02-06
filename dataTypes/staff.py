from dataclasses import KW_ONLY, dataclass
from uuid import UUID, uuid4


@dataclass
class Staff:
	userID: UUID
	firstName: str
	lastName: str
	address: str
	phoneNumber: str
	_: KW_ONLY
	staffID: UUID|None = None
	
	def __post_init__(self):
		if self.staffID is None:
			self.staffID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return [self.staffID, self.userID, self.firstName, self.lastName, self.address, self.phoneNumber]
