import pytest

from Application.Models.Pokemon import Pokemon


def test_get_offensive_weakness_fire(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fire")

    assert actual == sorted(expected)


def test_get_offensive_weakness_grass(type_utils):
    expected: list[str] = ["flying", "poison", "bug", "fire", "steel", "grass", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("grass")

    assert actual == sorted(expected)


def test_get_offensive_weakness_ghost(type_utils):
    expected: list[str] = ["dark"]
    actual: list[str] = type_utils.get_offensive_weaknesses("ghost")

    assert actual == sorted(expected)


def test_get_fairy_offensive_weakness(type_utils):
    expected: list[str] = ["poison", "steel", "fire"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fairy")

    assert actual == sorted(expected)


def test_get_offensive_weakness_fire_uppercase(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("FIRE")

    assert actual == sorted(expected)


def test_get_offensive_weakness_fire_mix_case(type_utils):
    expected: list[str] = ["fire", "water", "rock", "dragon"]
    actual: list[str] = type_utils.get_offensive_weaknesses("fIrE")

    assert actual == sorted(expected)


def test_get_offensive_weakness_type_doesnt_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_offensive_weaknesses("sound")

    assert str(error.value) == "'Sound' is not a valid type"


def test_get_defensive_weakness_fire(type_utils):
    expected: list[str] = ["ground", "rock", "water"]
    actual: list[str] = type_utils.get_defensive_weaknesses("fire", None)

    assert actual == sorted(expected)


def test_get_defensive_weakness_fire_grass(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("fire", "grass")

    assert actual == sorted(expected)


def test_get_defensive_weakness_ghost_normal(type_utils):
    expected: list[str] = ["dark"]
    actual: list[str] = type_utils.get_defensive_weaknesses("ghost", "normal")

    assert actual == sorted(expected)


def test_get_defensive_weakness_mixed_case_type_1(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("FIRe", "grass")

    assert actual == sorted(expected)


def test_get_defensive_weakness_mixed_case_type_2(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("fire", "gRasS")

    assert actual == sorted(expected)


def test_get_defensive_weakness_mixed_case_both_type(type_utils):
    expected: list[str] = ["flying", "poison", "rock"]
    actual: list[str] = type_utils.get_defensive_weaknesses("FiRe", "gRasS")

    assert actual == sorted(expected)


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
    actual: list[str] = type_utils.get_immunities("ghost", None)

    assert actual == sorted(expected)


def test_get_immunities_flying(type_utils):
    expected: list[str] = ["ground"]
    actual: list[str] = type_utils.get_immunities("flying", None)

    assert actual == sorted(expected)


def test_get_immunities_ground(type_utils):
    expected: list[str] = ["electric"]
    actual: list[str] = type_utils.get_immunities("ground", None)

    assert actual == sorted(expected)


def test_get_immunities_poison(type_utils):
    expected: list[str] = ["poison"]
    actual: list[str] = type_utils.get_immunities("steel", None)

    assert actual == sorted(expected)


def test_get_immunities_dark(type_utils):
    expected: list[str] = ["psychic"]
    actual: list[str] = type_utils.get_immunities("dark", None)

    assert actual == sorted(expected)


def test_get_immunities_normal(type_utils):
    expected: list[str] = ["ghost"]
    actual: list[str] = type_utils.get_immunities("normal", None)

    assert actual == sorted(expected)


def test_get_immunities_fair(type_utils):
    expected: list[str] = ["dragon"]
    actual: list[str] = type_utils.get_immunities("fairy", None)

    assert actual == sorted(expected)


def test_get_immunities_fire_steel(type_utils):
    expected: list[str] = ["poison"]
    actual: list[str] = type_utils.get_immunities("fire", "steel")
    assert actual == sorted(expected)


# Test for a dual-type that gets itself as 2 of the immunities
def test_get_immunities_ghost_normal(type_utils):
    expected: list[str] = ["fighting", "ghost", "normal"]
    actual: list[str] = type_utils.get_immunities("ghost", "normal")
    assert actual == sorted(expected)


# Test for a dual-type that gets 1 type's weakness as its immunity
def test_get_immunities_electric_flying(type_utils):
    expected: list[str] = ["ground"]
    actual: list[str] = type_utils.get_immunities("electric", "flying")
    assert actual == sorted(expected)


def test_get_immunities_mixed_case(type_utils):
    expected: list[str] = ["normal", "fighting"]
    actual: list[str] = type_utils.get_immunities("GhOsT", None)
    assert actual == sorted(expected)


def test_get_immunities_type_does_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities("sound", None)

    assert str(error.value) == "'Sound' is not a valid type"


def test_get_immunities_type_2_does_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities("fire", "sound")

    assert str(error.value) == "'Sound' is not a valid type"


# Tests for a type that does not have any immunities
def test_get_immunities_fire(type_utils):
    expected: list[str] = []
    actual: list[str] = type_utils.get_immunities("fire", None)

    assert actual == expected


# Test for dual-type that does not have any immunities
def test_get_immunities_fire_water(type_utils):
    expected: list[str] = []
    actual: list[str] = type_utils.get_immunities("fire", "water")
    assert actual == expected


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
