from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Vehicle:
	make: str
	model: str
	colour: str
	registration: str
	vin: str
	vehicleID: UUID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return [self.vehicleID, self.make, self.model, self.colour, self.registration, self.vin]
