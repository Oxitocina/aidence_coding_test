from ..domain.models import User, Task


class JSONUser:
    def __init__(self, user_json: dict):
        self.user_json = user_json

    @staticmethod
    def from_domain(user: User) -> "JSONUser":
        tasks_json = [
            {
                "uid": task.uid,
                "title": task.title,
                "description": task.description,
                "completed": str(task.completed),
            }
            for task in user.tasks
        ]
        return JSONUser(
            {
                "uid": user.uid,
                "name": user.name,
                "tasks": tasks_json,
            }
        )

    def to_domain(self) -> User:
        tasks_json = self.user_json["tasks"]
        tasks = [
            Task(
                uid=task_json["uid"],
                title=task_json["title"],
                description=task_json["description"],
                completed=True if task_json["completed"] == "True" else False,
            )
            for task_json in tasks_json
        ]
        return User(
            uid=self.user_json["uid"],
            name=self.user_json["name"],
            tasks=tasks,
        )
