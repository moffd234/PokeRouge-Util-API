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

    assert sorted(actual) == sorted(expected)


def test_get_offensive_weakness_fire_mix_case(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fIrE")

    assert sorted(actual) == sorted(expected)


def test_get_offensive_weakness_type_doesnt_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_offensive_weaknesses("sound")

    assert str(error.value) == "'Sound' is not a valid type"


def test_get_defensive_weakness_fire(type_utils):
    expected: list[str] = ["ground", "rock", "water"]
    actual: list[str] = type_utils.get_defensive_weaknesses("fire", None)

    assert sorted(actual) == sorted(expected)


def test_get_defensive_weakness_fire_grass(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("fire", "grass")

    assert sorted(actual) == sorted(expected)


def test_get_defensive_weakness_ghost_normal(type_utils):
    expected: list[str] = ["dark"]
    actual: list[str] = type_utils.get_defensive_weaknesses("ghost", "normal")

    assert sorted(actual) == sorted(expected)


def test_get_defensive_weakness_mixed_case_type_1(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("FIRe", "grass")

    assert sorted(actual) == sorted(expected)


def test_get_defensive_weakness_mixed_case_type_2(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("fire", "gRasS")

    assert sorted(actual) == sorted(expected)


def test_get_defensive_weakness_mixed_case_both_type(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("FiRe", "gRasS")

    assert sorted(actual) == sorted(expected)


def test_get_defensive_weakness_value_type_1_doesnt_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_defensive_weaknesses("fire", "sound")

    assert str(error.value) == "'Sound' is not a valid type"


def test_get_defensive_weakness_value_type_2_doesnt_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_defensive_weaknesses("sound", "fire")

    assert str(error.value) == "'Sound' is not a valid type"


def test_get_immunities_ghost(type_utils):
    expected: list[str] = ["normal", "fighting"]
    actual: list[str] = type_utils.get_immunities("ghost")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_flying(type_utils):
    expected: list[str] = ["ground"]
    actual: list[str] = type_utils.get_immunities("flying")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_ground(type_utils):
    expected: list[str] = ["electric"]
    actual: list[str] = type_utils.get_immunities("ground")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_poison(type_utils):
    expected: list[str] = ["poison"]
    actual: list[str] = type_utils.get_immunities("steel")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_dark(type_utils):
    expected: list[str] = ["psychic"]
    actual: list[str] = type_utils.get_immunities("dark")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_normal(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immunities("normal")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_fair(type_utils):
    expected: list[str] = ["dragon"]
    actual: list[str] = type_utils.get_immunities("fairy")

    assert sorted(actual) == sorted(expected)


def test_get_immunities_type_does_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities("sound")

    assert str(error.value) == "'Sound' is not a valid type"

# Tests for a type that does not have any immunities
def test_get_immunities_fire(type_utils):
    expected: list[str] = []
    actual: list[str] = type_utils.get_immunities("fire")

    assert actual == expected


def test_get_immune_defenders_normal(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immune_defenders("normal")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_fighting(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immune_defenders("fighting")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_electric(type_utils):
    expected: list[str] = ["ground"]
    actual: list[str] = type_utils.get_immune_defenders("electric")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_ground(type_utils):
    expected: list[str] = ["flying"]
    actual: list[str] = type_utils.get_immune_defenders("ground")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_poison(type_utils):
    expected: list[str] = ["steel"]
    actual: list[str] = type_utils.get_immune_defenders("poison")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_psychic(type_utils):
    expected: list[str] = ["dark"]
    actual: list[str] = type_utils.get_immune_defenders("psychic")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_dragon(type_utils):
    expected: list[str] = ["fairy"]
    actual: list[str] = type_utils.get_immune_defenders("dragon")

    assert sorted(actual) == sorted(expected)


def test_get_immune_defenders_type_does_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immune_defenders("sound")

    assert str(error.value) == "'Sound' is not a valid type"


# Tests for a type that does not have any immune defenders
def test_get_immune_defenders_fire(type_utils):
    expected: list[str] = []
    actual: list[str] = type_utils.get_immune_defenders("fire")

    assert actual == expected
