from dataclasses import KW_ONLY, dataclass
from uuid import UUID, uuid4


@dataclass
class Booking:
	staffID: UUID
	clientID: UUID
	vehicleID: UUID
	pickupDate: int
	pickupLocation: UUID
	dropoffDate: int
	dropoffLocation: UUID
	_: KW_ONLY
	bookingID: UUID|None = None
	
	def __post_init__(self):
		if self.bookingID is None:
			self.bookingID = uuid4()

	def getAtributes(self) -> list[UUID|int]:
		return [self.bookingID, self.staffID, self.clientID, self.vehicleID, self.pickupDate, self.pickupLocation, self.dropoffDate, self.pickupLocation]
