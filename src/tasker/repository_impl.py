import json

from .repository import TasksRepository, UserNotFound, TaskNotFound
from ..models.domain.models import User, Task
from ..models.json.models import JSONUser


class JSONTasksRepository(TasksRepository):
    def __init__(self, database_name):
        self.database_name = database_name
        with open(database_name) as json_file:
            database_dict = json.load(json_file)
        self.json_users = [JSONUser(user_dict) for user_dict in database_dict]

    def get_user(self, user_name: str) -> User:
        user_json = next(
            (
                user_json
                for user_json in self.json_users
                if user_json.user_json["name"] == user_name
            ),
            None,
        )
        if not user_json:
            raise UserNotFound
        return user_json.to_domain()

    def get_task(self, user: User, task_uid: str) -> Task:
        task = next((task for task in user.tasks if task.uid == task_uid), None)
        if task is None:
            raise TaskNotFound
        return task

    def post(self, user: User, task: Task):
        user.tasks.append(task)
        user_json = JSONUser.from_domain(user)
        self.json_users = [
            i for i in self.json_users if not (i.user_json["name"] == user.name)
        ]
        self.json_users.append(user_json)
        self.save()

    def edit(self, user: User, task: Task):
        user.tasks = list(filter(lambda x: x.uid != task.uid, user.tasks))
        user.tasks.append(task)
        user_json = JSONUser.from_domain(user)
        self.json_users = [
            i for i in self.json_users if not (i.user_json["name"] == user.name)
        ]
        self.json_users.append(user_json)
        self.save()

    def save(self):
        database_dict = [a.user_json for a in self.json_users]
        with open(self.database_name, "r+") as file:
            file.truncate(0)
            json.dump(database_dict, file)
