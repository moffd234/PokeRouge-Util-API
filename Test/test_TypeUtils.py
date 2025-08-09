import pytest

from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import get_offensive_weaknesses, get_defensive_weaknesses, get_immunities, \
    get_immune_defenders, get_defensive_strengths, get_offensive_strengths, get_weakness_strength_summary, validate_type


# ========================================================================================
# get_offensive_weaknesses(self, atk_type: str) -> list[str]:
# ========================================================================================
@pytest.mark.parametrize("input_type, expected", [
    ("fire", ["fire", "water", "rock", "dragon"]), ("fIrE", ["fire", "water", "rock", "dragon"]),
    ("grass", ["flying", "poison", "bug", "fire", "steel", "grass", "dragon"]),
    ("ghost", ["dark"]), ("fairy", ["poison", "steel", "fire"]), ("normal", ["rock", "steel"])
])
def test_get_offensive_weakness_valid(input_type, expected):
    actual: list[str] = get_offensive_weaknesses(input_type)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_offensive_weakness_type_doesnt_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_offensive_weaknesses(input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


# ========================================================================================
# get_defensive_weaknesses(self, type_1: str, type_2: str | None) -> list[str]:
# ========================================================================================

@pytest.mark.parametrize("input_type, expected", [
    ("fire", ["ground", "rock", "water"]), ("fIrE", ["ground", "rock", "water"]), ("normal", ["fighting"]),
    ("fighting", ["flying", "psychic", "fairy"]), ("flying", ["rock", "electric", "ice"]),
    ("poison", ["ground", "psychic"]), ("dark", ["fighting", "bug", "fairy"])
])
def test_get_defensive_weakness_valid_type(input_type, expected):
    actual: list[str] = get_defensive_weaknesses(input_type, None)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type_1, input_type_2, expected", [
    ("fire", "grass", ["flying", "poison", "rock"]), ("fIrE", "grass", ["flying", "poison", "rock"]),
    ("fire", "GrAsS", ["flying", "poison", "rock"]), ("fIrE", "GrAsS", ["flying", "poison", "rock"]),
    ("ghost", "normal", ["dark"]), ("normal", "ghost", ["dark"]), ("normal", "normal", ["fighting"])
])
def test_get_defensive_weakness_valid_dual_type(input_type_1, input_type_2, expected):
    actual: list[str] = get_defensive_weaknesses(input_type_1, input_type_2)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_weakness_type_1_doesnt_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_defensive_weaknesses(input_type, "fire")

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_weakness_type_2_doesnt_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_defensive_weaknesses("fire", input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


# ========================================================================================
# get_immunities(self, type_1: str, type_2) -> list[str]:
# ========================================================================================

@pytest.mark.parametrize("input_type, expected", [
    ("ghost", ["normal", "fighting"]), ("flying", ["ground"]), ("ground", ["electric"]), ("steel", ["poison"]),
    ("dark", ["psychic"]), ("normal", ["ghost"]), ("fairy", ["dragon"]), ("fAiRy", ["dragon"]), ("fire", [])
])
def test_get_immunities_valid_mono_type(input_type, expected):
    actual: list[str] = get_immunities(input_type, None)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type_1, input_type_2, expected", [
    ("fire", "steel", ["poison"]), ("FiRe", "steel", ["poison"]), ("FiRe", "sTeEl", ["poison"]),
    ("fire", "sTeEl", ["poison"]), ("ghost", "normal", ["fighting", "ghost", "normal"]),
    ("electric", "flying", ["ground"]),
    ("fire", "water", [])
])
def test_get_immunities_valid_dual_type(input_type_1, input_type_2, expected):
    actual: list[str] = get_immunities(input_type_1, input_type_2)
    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_immunities_type_does_not_exist_mono_type(input_type):
    with pytest.raises(ValueError) as error:
        get_immunities(input_type, None)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_immunities_does_not_exist_dual_type(input_type):
    with pytest.raises(ValueError) as error:
        get_immunities("fire", input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


def test_get_immunities_first_type_does_not_exist():
    with pytest.raises(ValueError) as error:
        get_immunities("sound", "fire")

    assert str(error.value) == f"'Sound' is not a valid type"


def test_get_immunities_both_types_do_not_exist():
    with pytest.raises(ValueError) as error:
        get_immunities("sound", "music")

    assert str(error.value) == f"'Sound' is not a valid type"


# ========================================================================================
# get_immune_defenders(self, attacker: str) -> list[str]:
# ========================================================================================

@pytest.mark.parametrize("input_type, expected", [
    ("normal", ["ghost"]), ("fighting", ["ghost"]), ("fire", []), ("fIrE", []), ("nOrmAl", ["ghost"]),
    ("electric", ["ground"]), ("ground", ["flying"]), ("poison", ["steel"]), ("psychic", ["dark"]),
    ("dragon", ["fairy"])
])
def test_get_immune_defenders_valid_types(input_type, expected):
    actual: list[str] = get_immune_defenders(input_type)

    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_immune_defenders_type_does_not_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_immune_defenders(input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


# ========================================================================================
# get_offensive_strengths(self, attacker: str):
# ========================================================================================
@pytest.mark.parametrize("input_type, expected", [
    ("fighting", ["normal", "rock", "steel", "ice", "dark"]), ("normal", []), ("dark", ["ghost", "psychic"])])
def test_get_offensive_strengths_valid(input_type, expected):
    actual: list[str] = get_offensive_strengths(input_type)
    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_offensive_strengths_type_does_not_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_offensive_strengths(input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


# ========================================================================================
# get_defensive_strengths(self, type_1: str, type_2: str | None)
# ========================================================================================
@pytest.mark.parametrize("input_type, expected", [
    ("fighting", ["rock", "bug", "dark"]), ("normal", []), ("dark", ["ghost", "dark"]),
    ("fire", ["bug", "steel", "fire", "grass", "ice", "fairy"]),
    ("fIrE", ["bug", "steel", "fire", "grass", "ice", "fairy"])])
def test_get_defensive_strengths_valid_mono_type(input_type, expected):
    actual: list[str] = get_defensive_strengths(input_type, None)
    assert actual == sorted(expected)


@pytest.mark.parametrize("input_type, expected", [
    ("fighting", ["bug", "steel", "fire", "grass", "ice", "dark"]),
    ("normal", ["bug", "steel", "fire", "grass", "ice", "fairy"]),
    ("dark", ["ghost", "dark", "fire", "steel", "grass", "ice"]),
    ("fire", ["bug", "steel", "fire", "grass", "ice", "fairy"]),
    ("fIrE", ["bug", "steel", "fire", "grass", "ice", "fairy"])])
def test_get_defensive_strengths_valid_dual_type(input_type, expected):
    actual: list[str] = get_defensive_strengths("fire", input_type)
    assert actual == sorted(expected)


def test_get_defensive_strengths_valid_dual_type_no_strength():
    expected: list[str] = []
    actual: list[str] = get_defensive_strengths("normal", "normal")

    assert actual == expected


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_strengths_mono_type_does_not_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_defensive_strengths(input_type, None)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_strengths_dual_type_first_type_does_not_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_defensive_strengths(input_type, "fire")

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_strengths_dual_type_second_type_does_not_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_defensive_strengths("fire", input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"

@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_get_defensive_strengths_dual_type_both_types_do_not_exist(input_type):
    with pytest.raises(ValueError) as error:
        get_defensive_strengths(input_type, input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"


# ========================================================================================
# get_weakness_summary(self, pokemon_species: Pokemon):
# ========================================================================================

def test_get_weakness_strength_summary_bulbasaur():
    expected: dict = {
        "offensive_weaknesses": {"grass": sorted(["flying", "poison", "bug", "steel", "fire", "grass", "dragon"]),
                                 "poison": sorted(["poison", "ground", "rock", "ghost"])},
        "defensive_weaknesses": sorted(["flying", "fire", "psychic", "ice"]),
        "immunities": [],
        "immune_defenders": {"grass": [], "poison": ["steel"]},
        "offensive_strengths": {"grass": sorted(["ground", "rock", "water"]),
                                "poison": sorted(["grass", "fairy"])},
        "defensive_strengths": sorted(["fighting", "water", "electric", "fairy", "grass"])
    }

    actual: dict = get_weakness_strength_summary(Pokemon.query.filter_by(name="BULBASAUR").first())

    assert actual == expected


def test_get_weakness_strength_summary_lunala():
    expected: dict = {

        "offensive_weaknesses": {"psychic": sorted(["steel", "psychic"]), "ghost": ["dark"]},
        "defensive_weaknesses": sorted(["ghost", "dark"]),
        "immunities": sorted(["normal", "fighting"]),
        "immune_defenders": {"psychic": ["dark"], "ghost": ["normal"]},
        "offensive_strengths": {"psychic": sorted(["fighting", "poison"]), "ghost": sorted(["ghost", "psychic"])},
        "defensive_strengths": sorted(["poison", "psychic"])
    }

    actual: dict = get_weakness_strength_summary(Pokemon.query.filter_by(name="LUNALA").first())

    assert actual == expected


def test_get_weakness_summary_invalid_type():
    pokemon: Pokemon = Pokemon.query.filter_by(name="FAKE_POKEMON").first()
    expected: dict = {"error": "'Sound' is not a valid type"}
    actual: dict = get_weakness_strength_summary(pokemon)

    assert actual == expected


# ========================================================================================
# validate_type(self, pokemon_type: str):
# ========================================================================================

@pytest.mark.parametrize("input_type", ["Fire", "fire", "FiRe", "water", "ground", "normal", "fighting", "flying",
                                        "poison", "rock", "bug", "ghost", "steel", "grass", "electric", "psychic",
                                        "ice", "dragon", "dark", "fairy"])
def test_validate_type_valid(input_type):
    expected: str = input_type.lower()
    actual: str = validate_type(input_type)

    assert actual == expected


@pytest.mark.parametrize("input_type", ["sound", "", " ", " fire ", " Fire ", " f"])
def test_validate_type_invalid(input_type):
    with pytest.raises(ValueError) as error:
        validate_type(input_type)

    assert str(error.value) == f"'{input_type.title()}' is not a valid type"
