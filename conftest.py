import string
import random

from pytest import fixture


uri = "https://reqres.in/api"

@fixture(scope='function')
def user_uri():
    return f"{uri}/users"

@fixture(scope='function')
def register_uri():
    return f"{uri}/register"

@fixture(scope='function')
def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))
