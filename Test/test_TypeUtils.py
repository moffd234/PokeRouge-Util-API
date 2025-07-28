import pytest


def test_get_offensive_weakness_fire(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fire")

    assert sorted(actual) == sorted(expected)


def test_get_offensive_weakness_grass(type_utils):
    expected: list[str] = ["flying", "poison", "bug", "fire", "steel", "grass", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("grass")

    assert sorted(actual) == sorted(expected)


def test_get_offensive_weakness_ghost(type_utils):
    expected: list[str] = ["dark"]
    actual: list[str] = type_utils.get_offensive_weaknesses("ghost")

    assert sorted(actual) == sorted(expected)


def test_get_fairy_offensive_weakness(type_utils):
    expected: list[str] = ["poison", "steel", "fire"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fairy")

    assert sorted(actual) == sorted(expected)


def test_get_offensive_weakness_fire_uppercase(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("FIRE")

    assert actual == expected


def test_get_offensive_weakness_fire_mix_case(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fIrE")

    assert actual == expected


def test_get_offensive_weakness_type_doesnt_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_offensive_weaknesses("Sound")

    assert str(error.value) == "'Sound' is not a valid type"
