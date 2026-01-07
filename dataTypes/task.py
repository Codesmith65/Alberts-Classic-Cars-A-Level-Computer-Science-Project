from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Task:
	taskName: str
	taskDescription: str
	completed: bool
	parentTask: UUID
	staffID: UUID
	taskID: UUID = uuid4()

	def getAtributes(self) -> list[UUID|str|bool]:
		return [self.taskID, self.taskName, self.taskDescription, self.completed, self.parentTask, self.staffID]
	
	def completeTask(self) -> None:
		self.completed = True