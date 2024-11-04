import pytest
from planning_poker import Developer, identify_extremes, Estimate

pepa = Developer(1, "Pepa")
franta = Developer(2, "Franta")
anicka = Developer(3, "Anicka")
romana = Developer(4, "Romana")

# class UserException(Exception):
#     pass

def test_planning_poker_none():
    with pytest.raises(Exception) as ex:
        identify_extremes(None)

    assert str(ex.value) == "Estimates cannot be None 2"

def test_planning_poker_one_developer():
    with pytest.raises(Exception) as ex:
        identify_extremes([
            Estimate(romana, 2),
        ])

    assert str(ex.value) == "Not enough developers"

def test_planning_poker():
    estimates = [
        Estimate(pepa, 8),
        Estimate(franta, 16),
        Estimate(anicka, 4),
        Estimate(romana, 2),
    ]

    output = identify_extremes(estimates)
    assert output == (romana, franta)


def test_planning_poker_from_lowest_to_highest():
    estimates = [
        Estimate(pepa, 2),
        Estimate(franta, 4),
        Estimate(anicka, 8),
        Estimate(romana, 16),
    ]

    output = identify_extremes(estimates)
    assert output == (pepa, romana)