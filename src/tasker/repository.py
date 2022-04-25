from abc import ABC, abstractmethod
from typing import List

from src.models.domain.models import User, Task


class TasksRepository(ABC):
    @abstractmethod
    def get_user(self, user_name: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_task(self, user: User, task_uid: str) -> Task:
        raise NotImplementedError

    @abstractmethod
    def post(self, user: User, task: Task):
        raise NotImplementedError

    @abstractmethod
    def edit(self, user: User, task: Task):
        raise NotImplementedError


class UserNotFound(Exception):
    pass


class TaskNotFound(Exception):
    pass
