from dataclasses import KW_ONLY, dataclass
from uuid import UUID, uuid4


@dataclass
class Task:
	taskName: str
	taskDescription: str
	completed: bool
	parentTask: UUID
	staffID: UUID
	_: KW_ONLY
	importance: int = 3
	taskID: UUID|None = None
	
	def __post_init__(self):
		if self.taskID is None:
			self.taskID = uuid4()

	def getAtributes(self) -> list[UUID|str|bool]:
		return [self.taskID, self.taskName, self.taskDescription, self.completed, self.parentTask, self.staffID, self.importance]
	
	def completeTask(self) -> None:
		self.completed = True