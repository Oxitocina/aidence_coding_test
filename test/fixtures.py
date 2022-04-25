from _pytest.fixtures import fixture

from src.models.domain.models import User
from .object_mothers import (
    domain_user_object_mother,
    database_user_object_mother,
    clean_db,
    database_user_with_tasks_object_mother,
)


@fixture
def domain_user() -> User:
    user = domain_user_object_mother(name="TestUser")
    database_user_object_mother(name="TestUser")
    yield user
    clean_db()


@fixture
def domain_user_with_tasks() -> User:
    user = domain_user_object_mother(name="TestUser")
    database_user_with_tasks_object_mother(name="TestUser")
    yield user
    clean_db()

