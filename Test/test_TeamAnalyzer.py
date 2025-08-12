import pytest

from Application.Models.Pokemon import Pokemon
from Application.Utils.TeamAnalyzer import get_team_resistances, get_team_immunities, get_team_defensive_weaknesses, \
    get_team_defensive_summary, get_team_offensive_weaknesses, get_team_offensive_strengths, get_team_immune_defenders
from Test.conftest import example_team

type_dict_zeros: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                   "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                   "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}


@pytest.mark.parametrize('method', [get_team_immunities, get_team_resistances, get_team_defensive_weaknesses,
                                    get_team_offensive_weaknesses, get_team_offensive_strengths,
                                    get_team_immune_defenders])
def test_empty_teams(method):
    expected: dict[str, int] = type_dict_zeros
    actual: dict[str, int] = method([])

    assert actual == expected


# ========================================================================================
# def get_team_resistances(team: list[Pokemon]) -> dict[str, int]:
# ========================================================================================
def test_get_team_resistances_full_team(example_team):
    expected: dict = {"normal": 2, "fire": 2, "water": 2, "electric": 2, "grass": 2, "ice": 2, "fighting": 2,
                      "poison": 1, "ground": 0, "flying": 3, "psychic": 2, "bug": 2, "rock": 2, "ghost": 0,
                      "dragon": 1, "dark": 1, "steel": 3, "fairy": 2}

    actual: dict = get_team_resistances(example_team)

    assert actual == expected


def test_get_team_resistances_one_member():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="BULBASAUR").first()]

    expected: dict = {"normal": 0, "fire": 0, "water": 1, "electric": 1, "grass": 1, "ice": 0, "fighting": 1,
                      "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0, "rock": 0, "ghost": 0,
                      "dragon": 0, "dark": 0, "steel": 0, "fairy": 1}

    actual: dict = get_team_resistances(team)

    assert actual == expected


def test_get_team_resistances_all_bulbasaur():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first()]

    expected: dict = {"normal": 0, "fire": 0, "water": 6, "electric": 6, "grass": 6, "ice": 0, "fighting": 6,
                      "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0, "rock": 0, "ghost": 0,
                      "dragon": 0, "dark": 0, "steel": 0, "fairy": 6}

    actual: dict = get_team_resistances(team)

    assert actual == expected


def test_get_team_resistances_all_types_resisted():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="GYARADOS").first(),
                           Pokemon.query.filter_by(name="STEELIX").first(),
                           Pokemon.query.filter_by(name="HOUNDOOM").first(),
                           Pokemon.query.filter_by(name="GOLEM").first(),
                           Pokemon.query.filter_by(name="TANGELA").first()]

    expected: dict = {"normal": 2, "fire": 3, "water": 2, "electric": 1, "grass": 2, "ice": 1, "fighting": 1,
                      "poison": 1, "ground": 1, "flying": 2, "psychic": 1, "bug": 2, "rock": 2, "ghost": 1,
                      "dragon": 1, "dark": 1, "steel": 3, "fairy": 1}
    actual: dict = get_team_resistances(team)

    assert actual == expected


def test_get_team_resistances_no_resistances():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="DITTO").first(),
                           Pokemon.query.filter_by(name="SNORLAX").first()]

    actual: dict = get_team_resistances(team)

    assert actual == type_dict_zeros


# ========================================================================================
# def get_team_immunities(team: list[Pokemon]) -> dict[str, int]:
# Notes:
#   We can't have a team that is weak to every type (nothing is immune to Fire, Water, etc.)
# ========================================================================================

def test_get_team_immunities_full_team(example_team):
    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 1, "grass": 0, "ice": 0,
                                "fighting": 0, "poison": 1, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}

    actual: dict[str, int] = get_team_immunities(example_team)
    assert actual == expected


def test_get_team_immunities_one_member():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 0, "ghost": 1, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}
    actual: dict[str, int] = get_team_immunities(team)

    assert actual == expected


def test_get_team_immunities_all_eevee():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 0, "ghost": 6, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}
    actual: dict[str, int] = get_team_immunities(team)

    assert actual == expected


def test_get_team_immunities_no_immunities():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="FLAREON").first(),
                           Pokemon.query.filter_by(name="VAPOREON").first(),
                           Pokemon.query.filter_by(name="LEAFEON").first(),
                           Pokemon.query.filter_by(name="GLACEON").first(),
                           Pokemon.query.filter_by(name="ESPEON").first(), ]

    expected: dict[str, int] = type_dict_zeros
    actual: dict[str, int] = get_team_immunities(team)

    assert actual == expected


def test_get_team_immunities_dual_type():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="GLISCOR").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 1, "grass": 0, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 1, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}
    actual: dict[str, int] = get_team_immunities(team)

    assert actual == expected


# ========================================================================================
# def get_team_defensive_weaknesses(team: list[Pokemon]) -> dict[str, int]:
#
# Notes:
#   We can't have a team that is weak to every type (nothing is weak to Normal)
#   No team can have 0 weaknesses as every type has a weaknesses as of gen 6+
# ========================================================================================

def test_get_team_defensive_weaknesses_full_team(example_team):
    expected: dict[str, int] = {"normal": 0, "fire": 1, "water": 2, "electric": 1, "grass": 1, "ice": 2,
                                "fighting": 2, "poison": 0, "ground": 4, "flying": 2, "psychic": 2, "bug": 1,
                                "rock": 0, "ghost": 1, "dragon": 0, "dark": 1, "steel": 1, "fairy": 0}
    actual: dict[str, int] = get_team_defensive_weaknesses(example_team)

    assert actual == expected


def test_get_team_defensive_weaknesses_one_member():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="VAPOREON").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 1, "grass": 1, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}
    actual: dict[str, int] = get_team_defensive_weaknesses(team)

    assert actual == expected


def test_get_team_defensive_weaknesses_all_eevee():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                "fighting": 6, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}
    actual: dict[str, int] = get_team_defensive_weaknesses(team)

    assert actual == expected


def test_get_team_defensive_weaknesses_dual_type():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="VOLCANION").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 1, "grass": 0, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 1, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 1, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}
    actual: dict[str, int] = get_team_defensive_weaknesses(team)

    assert actual == expected


# ========================================================================================
# def get_team_defensive_summary(team: list[Pokemon]) -> dict[str, dict[str, int]]:
# ========================================================================================


def test_get_team_defensive_summary(example_team):
    expected: dict[str, dict[str, int]] = {
        "defensive_weaknesses": {"normal": 0, "fire": 1, "water": 2, "electric": 1, "grass": 1, "ice": 2,
                                 "fighting": 2, "poison": 0, "ground": 4, "flying": 2, "psychic": 2, "bug": 1,
                                 "rock": 0, "ghost": 1, "dragon": 0, "dark": 1, "steel": 1, "fairy": 0},
        "immunities": {"normal": 0, "fire": 0, "water": 0, "electric": 1, "grass": 0, "ice": 0,
                       "fighting": 0, "poison": 1, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                       "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0},
        "resistances": {"normal": 2, "fire": 2, "water": 2, "electric": 2, "grass": 2, "ice": 2, "fighting": 2,
                        "poison": 1, "ground": 0, "flying": 3, "psychic": 2, "bug": 2, "rock": 2, "ghost": 0,
                        "dragon": 1, "dark": 1, "steel": 3, "fairy": 2}
    }

    actual: dict[str, dict[str, int]] = get_team_defensive_summary(example_team)

    assert actual == expected


def test_get_team_defensive_summary_empty_team():
    expected: dict[str, dict[str, int]] = {
        "defensive_weaknesses": type_dict_zeros,
        "immunities": type_dict_zeros,
        "resistances": type_dict_zeros
    }

    actual: dict[str, dict[str, int]] = get_team_defensive_summary([])

    assert actual == expected


def test_get_team_defensive_summary_all_eevee():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="EEVEE").first()]

    expected: dict[str, dict[str, int]] = {
        "defensive_weaknesses": {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                 "fighting": 6, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                 "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0},
        "immunities": {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                       "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                       "rock": 0, "ghost": 6, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0},
        "resistances": {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                        "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                        "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0},
    }

    actual: dict[str, dict[str, int]] = get_team_defensive_summary(team)

    assert actual == expected


# ========================================================================================
# def get_team_offensive_weaknesses(team: list[Pokemon]) -> dict[str, int]:
# ========================================================================================
def test_get_team_offensive_weaknesses(example_team):
    expected: dict[str, int] = {"normal": 0, "fire": 3, "water": 2, "electric": 2, "grass": 4, "ice": 0,
                                "fighting": 1, "poison": 2, "ground": 2, "flying": 2, "psychic": 2, "bug": 3,
                                "rock": 2, "ghost": 1, "dragon": 4, "dark": 0, "steel": 4, "fairy": 1}
    actual: dict[str, int] = get_team_offensive_weaknesses(example_team)

    assert actual == expected


def test_get_offensive_weakness_one_member():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 1, "ghost": 0, "dragon": 0, "dark": 0, "steel": 1, "fairy": 0}
    actual: dict[str, int] = get_team_offensive_weaknesses(team)

    assert actual == expected


def test_get_offensive_weaknesses_all_bulbasaur():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 6, "water": 0, "electric": 0, "grass": 6, "ice": 0,
                                "fighting": 0, "poison": 6, "ground": 6, "flying": 6, "psychic": 0, "bug": 6,
                                "rock": 6, "ghost": 6, "dragon": 6, "dark": 0, "steel": 6, "fairy": 0}
    actual: dict[str, int] = get_team_offensive_weaknesses(team)

    assert actual == expected


def test_get_offensive_weakness_dual_type():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="BULBASAUR").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 1, "water": 0, "electric": 0, "grass": 1, "ice": 0,
                                "fighting": 0, "poison": 1, "ground": 1, "flying": 1, "psychic": 0, "bug": 1,
                                "rock": 1, "ghost": 1, "dragon": 1, "dark": 0, "steel": 1, "fairy": 0}
    actual: dict[str, int] = get_team_offensive_weaknesses(team)

    assert actual == expected


# ========================================================================================
# def get_team_offensive_strengths(team: list[Pokemon]) -> dict[str, int]:
# ========================================================================================

def test_get_offensive_strengths(example_team):
    expected: dict[str, int] = {"normal": 1, "fire": 2, "water": 2, "electric": 1, "grass": 2, "ice": 3,
                                "fighting": 1, "poison": 2, "ground": 2, "flying": 2, "psychic": 0, "bug": 2,
                                "rock": 4, "ghost": 0, "dragon": 0, "dark": 1, "steel": 2, "fairy": 2}
    actual: dict[str, int] = get_team_offensive_strengths(example_team)

    assert actual == expected


def test_get_offensive_strengths_one_member():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="BULBASAUR").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 1, "electric": 0, "grass": 1, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 1, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 1, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 1}
    actual: dict[str, int] = get_team_offensive_strengths(team)

    assert actual == expected


def test_get_offensive_strengths_all_bulbasaur():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first(),
                           Pokemon.query.filter_by(name="BULBASAUR").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 0, "water": 6, "electric": 0, "grass": 6, "ice": 0,
                                "fighting": 0, "poison": 0, "ground": 6, "flying": 0, "psychic": 0, "bug": 0,
                                "rock": 6, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 6}
    actual: dict[str, int] = get_team_offensive_strengths(team)

    assert actual == expected


def test_get_team_offensive_strengths_mono_type():
    team: list[Pokemon] = [Pokemon.query.filter_by(name="EEVEE").first(),
                           Pokemon.query.filter_by(name="VAPOREON").first(),
                           Pokemon.query.filter_by(name="JOLTEON").first(),
                           Pokemon.query.filter_by(name="FLAREON").first(),
                           Pokemon.query.filter_by(name="ESPEON").first(),
                           Pokemon.query.filter_by(name="UMBREON").first()]

    expected: dict[str, int] = {"normal": 0, "fire": 1, "water": 1, "electric": 0, "grass": 1, "ice": 1,
                                "fighting": 1, "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1,
                                "rock": 1, "ghost": 1, "dragon": 0, "dark": 0, "steel": 1, "fairy": 0}
    actual: dict[str, int] = get_team_offensive_strengths(team)

    assert actual == expected

