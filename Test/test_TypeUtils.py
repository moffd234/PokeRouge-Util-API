import pytest

from Application.Models.Pokemon import Pokemon


@pytest.mark.parametrize("input_type, expected", [
    ("fire", ["fire", "water", "rock", "dragon"]), ("fIrE", ["fire", "water", "rock", "dragon"]),
    ("grass", ["flying", "poison", "bug", "fire", "steel", "grass", "dragon"]),
    ("ghost", ["dark"]), ("fairy", ["poison", "steel", "fire"]), ("normal", ["rock", "steel"])
])
def test_get_offensive_weakness_valid(type_utils, input_type, expected):
    actual: list[str] = type_utils.get_offensive_weaknesses(input_type)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_offensive_weakness_type_doesnt_exist(type_utils, input_type):
    with pytest.raises(ValueError) as error:
        type_utils.get_offensive_weaknesses(input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type, expected", [
    ("fire", ["ground", "rock", "water"]), ("fIrE", ["ground", "rock", "water"]), ("normal", ["fighting"]),
    ("fighting", ["flying", "psychic", "fairy"]), ("flying", ["rock", "electric", "ice"]),
    ("poison", ["ground", "psychic"]), ("dark", ["fighting", "bug", "fairy"])
])
def test_get_defensive_weakness_valid_type(type_utils, input_type, expected):
    actual: list[str] = type_utils.get_defensive_weaknesses(input_type, None)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type_1, input_type_2, expected", [
    ("fire", "grass", ["flying", "poison", "rock"]), ("fIrE", "grass", ["flying", "poison", "rock"]),
    ("fire", "GrAsS", ["flying", "poison", "rock"]), ("fIrE", "GrAsS", ["flying", "poison", "rock"]),
    ("ghost", "normal", ["dark"]), ("normal", "ghost", ["dark"]), ("normal", "normal", ["fighting"])
])
def test_get_defensive_weakness_valid_dual_type(type_utils, input_type_1, input_type_2, expected):
    actual: list[str] = type_utils.get_defensive_weaknesses(input_type_1, input_type_2)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_weakness_type_1_doesnt_exist(type_utils, input_type):
    with pytest.raises(ValueError) as error:
        type_utils.get_defensive_weaknesses(input_type, "fire")

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_weakness_type_2_doesnt_exist(type_utils, input_type):
    with pytest.raises(ValueError) as error:
        type_utils.get_defensive_weaknesses("fire", input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type, expected", [
    ("ghost", ["normal", "fighting"]), ("flying", ["ground"]), ("ground", ["electric"]), ("steel", ["poison"]),
    ("dark", ["psychic"]), ("normal", ["ghost"]), ("fairy", ["dragon"]), ("fAiRy", ["dragon"]), ("fire", [])
])
def test_get_immunities_valid_mono_type(type_utils, input_type, expected):
    actual: list[str] = type_utils.get_immunities(input_type, None)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type_1, input_type_2, expected", [
    ("fire", "steel", ["poison"]), ("FiRe", "steel", ["poison"]), ("FiRe", "sTeEl", ["poison"]),
    ("fire", "sTeEl", ["poison"]), ("ghost", "normal", ["fighting", "ghost", "normal"]), ("electric", "flying", ["ground"]),
    ("fire", "water", [])
])
def test_get_immunities_valid_dual_type(type_utils, input_type_1, input_type_2, expected):
    actual: list[str] = type_utils.get_immunities(input_type_1, input_type_2)
    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_immunities_type_does_not_exist_mono_type(type_utils, input_type):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities(input_type, None)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"

@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_immunities_does_not_exist_dual_type(type_utils, input_type):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities("fire", input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"

def test_get_immune_defenders_normal(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immune_defenders("normal")

    assert actual == sorted(expected)


def test_get_immune_defenders_fighting(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immune_defenders("fighting")

    assert actual == sorted(expected)


def test_get_immune_defenders_electric(type_utils):
    expected: list[str] = ["ground"]
    actual: list[str] = type_utils.get_immune_defenders("electric")

    assert actual == sorted(expected)


def test_get_immune_defenders_ground(type_utils):
    expected: list[str] = ["flying"]
    actual: list[str] = type_utils.get_immune_defenders("ground")

    assert actual == sorted(expected)


def test_get_immune_defenders_poison(type_utils):
    expected: list[str] = ["steel"]
    actual: list[str] = type_utils.get_immune_defenders("poison")

    assert actual == sorted(expected)


def test_get_immune_defenders_psychic(type_utils):
    expected: list[str] = ["dark"]
    actual: list[str] = type_utils.get_immune_defenders("psychic")

    assert actual == sorted(expected)


def test_get_immune_defenders_dragon(type_utils):
    expected: list[str] = ["fairy"]
    actual: list[str] = type_utils.get_immune_defenders("dragon")

    assert actual == sorted(expected)


def test_get_immune_defenders_type_does_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immune_defenders("sound")

    assert str(error.value) == "'Sound' is not a valid type"


# Tests for a type that does not have any immune defenders
def test_get_immune_defenders_fire(type_utils):
    expected: list[str] = []
    actual: list[str] = type_utils.get_immune_defenders("fire")

    assert actual == expected


def test_get_immune_defenders_mixed_case(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immune_defenders("NoRmAl")
    assert actual == sorted(expected)


def test_get_weakness_summary_bulbasaur(type_utils, example_pokemon):
    expected: dict = {
        "offensive_weaknesses": {"grass": sorted(["flying", "poison", "bug", "steel", "fire", "grass", "dragon"]),
                                 "poison": sorted(["poison", "ground", "rock", "ghost"])},
        "defensive_weaknesses": sorted(["flying", "fire", "psychic", "ice"]),
        "immunities": [],
        "immune_defenders": {"grass": [], "poison": ["steel"]},
    }

    actual: dict = type_utils.get_weakness_summary(example_pokemon["bulbasaur"])

    assert actual == expected


def test_get_weakness_summary_lunala(type_utils, example_pokemon):
    expected: dict = {

        "offensive_weaknesses": {"psychic": sorted(["steel", "psychic"]), "ghost": ["dark"]},
        "defensive_weaknesses": sorted(["ghost", "dark"]),
        "immunities": sorted(["normal", "fighting"]),
        "immune_defenders": {"psychic": ["dark"], "ghost": ["normal"]},
    }

    actual: dict = type_utils.get_weakness_summary(example_pokemon["lunala"])

    assert actual == expected


def test_get_weakness_summary_invalid_type(type_utils, example_pokemon):
    pokemon: Pokemon = example_pokemon["fake"]
    expected: dict = {"error": "'Sound' is not a valid type"}
    actual: dict = type_utils.get_weakness_summary(pokemon)

    assert actual == expected
