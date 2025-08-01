import pytest

from Application.Models.Pokemon import Pokemon


# ========================================================================================
# get_offensive_weaknesses(self, atk_type: str) -> list[str]:
# ========================================================================================
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


# ========================================================================================
# get_defensive_weaknesses(self, type_1: str, type_2: str | None) -> list[str]:
# ========================================================================================

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


# ========================================================================================
# get_immunities(self, type_1: str, type_2) -> list[str]:
# ========================================================================================

@pytest.mark.parametrize("input_type, expected", [
    ("ghost", ["normal", "fighting"]), ("flying", ["ground"]), ("ground", ["electric"]), ("steel", ["poison"]),
    ("dark", ["psychic"]), ("normal", ["ghost"]), ("fairy", ["dragon"]), ("fAiRy", ["dragon"]), ("fire", [])
])
def test_get_immunities_valid_mono_type(type_utils, input_type, expected):
    actual: list[str] = type_utils.get_immunities(input_type, None)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type_1, input_type_2, expected", [
    ("fire", "steel", ["poison"]), ("FiRe", "steel", ["poison"]), ("FiRe", "sTeEl", ["poison"]),
    ("fire", "sTeEl", ["poison"]), ("ghost", "normal", ["fighting", "ghost", "normal"]),
    ("electric", "flying", ["ground"]),
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


def test_get_immunities_first_type_does_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities("sound", "fire")

    assert str(error.value) == f"'Sound' is not a valid type"


def test_get_immunities_both_types_do_not_exist(type_utils):
    with pytest.raises(ValueError) as error:
        type_utils.get_immunities("sound", "music")

    assert str(error.value) == f"'Sound' is not a valid type"


# ========================================================================================
# get_immune_defenders(self, attacker: str) -> list[str]:
# ========================================================================================

@pytest.mark.parametrize("input_type, expected", [
    ("normal", ["ghost"]), ("fighting", ["ghost"]), ("fire", []), ("fIrE", []), ("nOrmAl", ["ghost"]),
    ("electric", ["ground"]), ("ground", ["flying"]), ("poison", ["steel"]), ("psychic", ["dark"]),
    ("dragon", ["fairy"])
])
def test_get_immune_defenders_valid_types(type_utils, input_type, expected):
    actual: list[str] = type_utils.get_immune_defenders(input_type)

    assert actual == sorted(expected)

@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_immune_defenders_type_does_not_exist(type_utils, input_type):
    with pytest.raises(ValueError) as error:
        type_utils.get_immune_defenders(input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


# ========================================================================================
# get_weakness_summary(self, pokemon_species: Pokemon):
# ========================================================================================

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

