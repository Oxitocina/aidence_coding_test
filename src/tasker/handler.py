from .application import post_task, edit_task, complete_task, list_tasks
from .repository import UserNotFound, TaskNotFound
from .repository_impl import JSONTasksRepository


class BasicTaskerHandler:
    def __init__(self):
        self.router_dict = {
            "->": self.post_task_handler,
            "edit": self.edit_task_handler,
            "complete": self.complete_task_handler,
        }
        self.database_name = "database.json"

    def post_task_handler(self, command: str):
        user_name, task = [a.strip() for a in command.split("->")]
        title, description = [a.strip() for a in task.split(":")]
        repo = JSONTasksRepository(self.database_name)
        try:
            post_task(user_name, title, description, repo)
        except UserNotFound:
            print(f"This user does not exist in our system: {user_name}")

    def edit_task_handler(self, command: str):
        user_name, task = [a.strip() for a in command.split("edit")]
        uid, title, description = [a.strip() for a in task.split(":")]
        repo = JSONTasksRepository(self.database_name)
        try:
            edit_task(user_name, uid, title, description, repo)
        except UserNotFound:
            print(f"This user does not exist in our system: {user_name}")
        except TaskNotFound:
            print(f"This task does not exist in our system: {user_name}")

    def complete_task_handler(self, command: str):
        command_list = command.split()
        user_name = command_list[0].strip()
        uid = command_list[2]
        repo = JSONTasksRepository(self.database_name)
        try:
            complete_task(user_name, uid, repo)
        except UserNotFound:
            print(f"This user does not exist in our system: {user_name}")
        except TaskNotFound:
            print(f"This task does not exist in our system: {user_name}")

    def retrieve_user_tasks_handler(self, command: str):
        user_name = command.strip()
        repo = JSONTasksRepository(self.database_name)
        try:
            user_tasks_str = list_tasks(user_name, repo)
        except UserNotFound:
            print(f"This user does not exist in our system: {user_name}")
            return
        for task_str in user_tasks_str:
            print(task_str)

    def route_command(self, command):
        processed = False
        for key in self.router_dict.keys():
            if command.find(key) != -1 and not processed:
                self.router_dict[key](command)
                processed = True
        if not processed:
            self.retrieve_user_tasks_handler(command)
