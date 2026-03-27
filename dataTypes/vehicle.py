from dataclasses import dataclass, KW_ONLY
from uuid import UUID, uuid4


@dataclass
class Vehicle:
	make: str
	model: str
	colour: str
	registration: str
	vin: str
	_: KW_ONLY
	costPerDay: int = 20
	vehicleID: UUID|None = None
	
	def __post_init__(self):
		if self.vehicleID is None:
			self.vehicleID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return [self.vehicleID, self.make, self.model, self.colour, self.registration, self.vin, self.costPerDay]
