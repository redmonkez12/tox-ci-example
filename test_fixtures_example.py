from conftest import Pet


def test_add_pet(pets_data):
    print(pets_data)
    pets_data.append(Pet(5, "Ruda"))

    assert len(pets_data) == 5


def test_add_next_pet(pets_data):
    pets_data.append(Pet(6, "Ferda"))

    assert len(pets_data) == 5
