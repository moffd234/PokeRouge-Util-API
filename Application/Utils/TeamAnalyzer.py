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


def get_team_defensive_summary(team: list[Pokemon]) -> dict[str, dict[str, int]]:
    return {
        "defensive_weaknesses": get_team_defensive_weaknesses(team),
        "immunities": get_team_immunities(team),
        "resistances": get_team_resistances(team)
    }


def get_team_offensive_weaknesses(team: list[Pokemon]) -> dict[str, int]:
    weaknesses: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        pokemon_weaknesses = set()

        pokemon_weaknesses.update(get_offensive_weaknesses(pokemon.type_1))
        pokemon_weaknesses.update(get_offensive_weaknesses(pokemon.type_2))

        for weakness in pokemon_weaknesses:
            weaknesses[weakness] += 1

    return weaknesses


def get_team_offensive_strengths(team: list[Pokemon]) -> dict[str, int]:
    strengths: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        pokemon_strengths = set()

        pokemon_strengths.update(get_offensive_strengths(pokemon.type_1))
        pokemon_strengths.update(get_offensive_strengths(pokemon.type_2))

        for weakness in pokemon_strengths:
            strengths[weakness] += 1

    return strengths


def get_team_immune_defenders(team: list[Pokemon]) -> dict[str, int]:
    defenders: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        immune_defenders = set()

        immune_defenders.update(get_immune_defenders(pokemon.type_1))
        immune_defenders.update(get_immune_defenders(pokemon.type_2))

        for weakness in immune_defenders:
            defenders[weakness] += 1

    return defenders


def get_team_offensive_summary(team: list[Pokemon]) -> dict[str, dict[str, int]]:
    return {"offensive_weaknesses": get_team_offensive_weaknesses(team),
            "offensive_strengths": get_team_offensive_strengths(team),
            "immune_defenders": get_team_immune_defenders(team)}
