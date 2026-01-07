from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Location:
	locationName: str
	locationID: UUID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return [self.locationID, self.locationName]
