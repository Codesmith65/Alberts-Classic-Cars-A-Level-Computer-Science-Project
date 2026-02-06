from dataclasses import KW_ONLY, dataclass
from uuid import UUID, uuid4


@dataclass
class Location:
	locationName: str
	_: KW_ONLY
	locationID: UUID|None = None
	
	def __post_init__(self):
		if self.locationID is None:
			self.locationID = uuid4()

	def getAtributes(self) -> list[UUID|str]:
		return [self.locationID, self.locationName]
