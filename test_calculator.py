import pytest
from _pytest.fixtures import SubRequest

from calculator import Calculator

# implementace bude trida
# a kazda metoda bude prijimat dve cisla

# Varianta 1 - hardcoded string v listu - kolik itemu v listu tolik itemu v ids
# Varianta 2 - str vezme data udela z toho string
# Varianta 3 - lambda maximalni kontrola nad tim co se ma vypisovat

@pytest.fixture()
def data_with_auth(request: SubRequest):
    data = request.param

    print("Prihlaseni")

    yield data

    print("Odhlaseni")

@pytest.mark.parametrize("data_with_auth", [
    pytest.param({"a": 5, "b": -1, "result": 4}, id="Mam prioritu jsem hustej"),
    {"a": 7, "b": 8, "result": 15},
    {"a": 1, "b": -1, "result": 0},
], ids=lambda row: f'{row["a"]}+{row["b"]}={row["result"]}', indirect=["data_with_auth"])
def test_sum(data_with_auth):
    calculator = Calculator()
    output = calculator.sum(data_with_auth["a"], data_with_auth["b"])
    assert output == data_with_auth["result"]

# def test_sum():
#     calculator = Calculator()
#     data = [
#         {"a": 5, "b": -1, "result": 4},
#         {"a": 7, "b": 8, "result": 15},
#         {"a": 1, "b": -1, "result": 0},
#     ]
#
#     for item in data:
#         result = calculator.sum(item["a"], item["b"])
#         assert result + 1 == item["result"]


# def test_sum_1():
#     calculator = Calculator()
#     result = calculator.sum(7, 8)
#
#     assert result == 15
#
# def test_sum_2():
#     calculator = Calculator()
#     result = calculator.sum(1, -1)
#
#     assert result == 0

# napsat test na odcitani + napsat metodu do calculator tridy

# def test_subtract():
#     calculator = Calculator()
#     result = calculator.subtract(4, 5)
#
#     assert result == -1