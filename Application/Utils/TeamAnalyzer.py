from Application.Utils.TypeUtils import *


def get_team_resistances(team: list[Pokemon]) -> dict[str, int]:
    """
    Calculates the number of Pokémon in the given team that resist each Pokémon type.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each Pokémon type to the number of team members
             that resist it.
    """
    resistances: dict = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        for resistance in get_defensive_strengths(pokemon.type_1, pokemon.type_2):
            resistances[resistance] += 1

    return resistances


def get_team_immunities(team: list[Pokemon]) -> dict[str, int]:
    immunities: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        for immunity in get_immunities(pokemon.type_1, pokemon.type_2):
            immunities[immunity] += 1

    return immunities


def get_team_defensive_weaknesses(team: list[Pokemon]) -> dict[str, int]:
    weaknesses: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        for weakness in get_defensive_weaknesses(pokemon.type_1, pokemon.type_2):
            weaknesses[weakness] += 1

    return weaknesses
