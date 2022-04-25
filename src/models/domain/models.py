import uuid
from typing import List


class Task:
    def __init__(
        self,
        uid: str = None,
        title: str = None,
        description: str = None,
        completed: bool = False,
    ):
        self.uid = uuid.uuid4().hex if not uid else uid
        self.title = title
        self.description = description
        self.completed = completed

    def complete_task(self):
        self.completed = True


class User:
    def __init__(self, uid: str = None, name: str = None, tasks: List[Task] = None):
        self.uid = uuid.uuid4().hex if not uid else uid
        self.name = name
        self.tasks = tasks if tasks else []
