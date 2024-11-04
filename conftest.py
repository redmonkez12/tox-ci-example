import pytest
from collections import namedtuple

Pet = namedtuple("Pet", "id, name")

@pytest.fixture(scope="function")
def pets_data():
    """ Ziskavani dat z databaze """
    # setup
    fake_db = [
        Pet(id=1, name="Black"),
        Pet(id=2, name="Johny"),
        Pet(id=3, name="Star"),
        Pet(id=4, name="Luna"),
    ]

    yield fake_db

    # teardown

    print("Zaviram databazi...")

import time

# autouse
@pytest.fixture(autouse=True)
def measure_time():
    start = time.time()
    yield
    end = time.time()

    delta = end - start
    print("\ndelka testu: {:0.3} sekund".format(delta))
