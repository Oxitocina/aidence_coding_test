import json

from src.models.domain.models import User


def domain_user_object_mother(name: str) -> User:
    return User(name=name)


def database_user_object_mother(name: str):
    database_dict = [{"uid": "fakeuid", "name": name, "tasks": []}]
    with open("database_test.json", "a+") as file:
        json.dump(database_dict, file)


def database_user_with_tasks_object_mother(name: str):
    database_dict = [
        {
            "uid": "fakeuid",
            "name": name,
            "tasks": [
                {
                    "uid": "fakeuid2",
                    "title": "Title",
                    "description": "Hello world",
                    "completed": "False",
                },
                {
                    "uid": "fakeuid3",
                    "title": "Title_2",
                    "description": "Hello world_2",
                    "completed": "False",
                },
            ],
        }
    ]
    with open("database_test.json", "a+") as file:
        json.dump(database_dict, file)


def clean_db():
    f = open("database_test.json", "w")
    f.close()
