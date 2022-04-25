from typing import List

from .repository import TasksRepository
from ..models.domain.models import Task


def post_task(user_name: str, title: str, description: str, repo: TasksRepository):
    user = repo.get_user(user_name)
    task = Task(title=title, description=description)
    repo.post(user, task)


def edit_task(
    user_name: str, task_uid: str, title: str, description: str, repo: TasksRepository
):
    user = repo.get_user(user_name)
    task = repo.get_task(user, task_uid)
    task.title = title
    task.description = description
    repo.edit(user, task)


def list_tasks(user_name: str, repo: TasksRepository) -> List[str]:
    user = repo.get_user(user_name)
    user_tasks = user.tasks
    task_list = []
    for task in user_tasks:
        task_str = f"""{task.title} ({task.uid}) - STATUS: {'COMPLETED' if task.completed else 'PENDING'}
                        DESC: {task.description}"""
        task_list.append(task_str)
    return task_list


def complete_task(user_name: str, task_uid: str, repo: TasksRepository):
    user = repo.get_user(user_name)
    task = repo.get_task(user, task_uid)
    task.complete_task()
    repo.edit(user, task)
