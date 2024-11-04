from weapon import Weapon
from unittest.mock import patch
import random

def test_attack_new_weapon():
    weapon = Weapon(20, 30, 10, 10, 100)

    with patch.object(random, "randint", side_effect=[8, 2]):
        result = weapon.attack()
        assert result == 22
        assert weapon.health == 99

    # with patch.object(random, "randint", return_value=10):
    #     result = weapon.attack()
    #     assert result == 30

    # with patch.object(weapon, "health", 5):
    #     assert weapon.attack() == 0
    # result = weapon.attack()
    # assert result == 20
