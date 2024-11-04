from barbarian import Barbarian
from weapon import Weapon
from unittest.mock import patch, Mock

def test_attack_high_damage():
    with patch.object(Weapon, "attack") as mock_weapon:
        mock_weapon.return_value = 20
        weapon = Weapon(20, 30, 10, 10, 100)
        barbarian = Barbarian(60, 100, weapon)
        assert barbarian.attack() == 90

    # mock_weapon = Mock(spec=Weapon)
    # mock_weapon.attack.return_value = 20
    #
    # barbarian = Barbarian(60, 100, mock_weapon)
    #
    # assert barbarian.attack() == 90

import pytest

def test_attack_with_broken_weapon():
    mock_weapon = Mock(spec=Weapon)
    mock_weapon.attack.side_effect = Exception("Nemuzu utocit 1")

    barbarian = Barbarian(60, 100, mock_weapon)

    with pytest.raises(Exception) as e:
        barbarian.attack()

    assert str(e.value) == "Nemuzu utocit 1"

    # with pytest.raises(Exception, match="Nemuzu utocit"):
    #     barbarian.attack()
