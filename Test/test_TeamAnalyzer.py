import pytest

from Application.Models.Pokemon import Pokemon
from Application.Utils.TeamAnalyzer import get_team_resistances, get_team_immunities
from Test.conftest import example_team

type_dict_zeros: dict[str, int] = {"normal": 0, "fire": 0, "water": 0, "electric": 0, "grass": 0, "ice": 0,
                                   "fighting": 0, "poison": 0, "ground": 0, "flying": 0, "psychic": 0, "bug": 0,
                                   "rock": 0, "ghost": 0, "dragon": 0, "dark": 0, "steel": 0, "fairy": 0}

@pytest.mark.parametrize('method', [get_team_immunities, get_team_resistances])
def test_empty_teams(method):
    expected: dict[str, int] = type_dict_zeros
    actual: dict[str, int] = method([])

    assert actual == expected

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

