import json
import os

from src.tasker.application import post_task, edit_task, list_tasks, complete_task
from src.tasker.repository_impl import JSONTasksRepository


def test_post_task(domain_user):
    repo = JSONTasksRepository("database_test.json")
    post_task(domain_user.name, "test title", "test_description", repo)

    assert os.path.getsize("database_test.json") > 0
    with open("database_test.json") as json_file:
        database_dict = json.load(json_file)
    assert len(database_dict[0]["tasks"]) == 1
    assert database_dict[0]["tasks"][0]["title"] == "test title"
    assert database_dict[0]["tasks"][0]["description"] == "test_description"


def test_edit_task(domain_user_with_tasks):
    repo = JSONTasksRepository("database_test.json")
    task_uid = "fakeuid2"
    edit_task(domain_user_with_tasks.name, task_uid, "New Title", "New Description", repo)

    with open("database_test.json") as json_file:
        database_dict = json.load(json_file)
    task_dict = next(task for task in database_dict[0]["tasks"] if task["uid"] == task_uid)
    assert task_dict["title"] == "New Title"
    assert task_dict["description"] == "New Description"


def test_list_tasks(domain_user_with_tasks):
    repo = JSONTasksRepository("database_test.json")
    tasks = list_tasks(domain_user_with_tasks.name, repo)
    assert tasks
    assert len(tasks) == 2


def test_complete_task(domain_user_with_tasks):
    repo = JSONTasksRepository("database_test.json")
    task_uid = "fakeuid2"
    complete_task(domain_user_with_tasks.name, task_uid, repo)
    with open("database_test.json") as json_file:
        database_dict = json.load(json_file)
    task_dict = next(task for task in database_dict[0]["tasks"] if task["uid"] == task_uid)
    assert task_dict["completed"] == "True"
