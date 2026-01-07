from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Staff:
	userID: UUID
	firstName: str
	lastName: str
	address: str
	phoneNumber: str
	staffID: UUID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return [self.staffID, self.userID, self.firstName, self.lastName, self.address, self.phoneNumber]