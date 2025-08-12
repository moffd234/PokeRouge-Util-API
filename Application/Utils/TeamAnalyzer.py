from typing import Callable

from Application.Utils.TypeUtils import *


def get_team_defensive_info(team: list[Pokemon], defensive_func: Callable) -> dict[str, int]:
    """
    Counts how many Pokémon in the team meet a given defensive condition.

    The given `defensive_method` should take two type strings (type_1, type_2)
    and return a list of types that satisfy the condition (i.e., resistances, weaknesses, immunities).

    :param team: List of Pokémon objects representing the team.
    :param defensive_func: Function returning a list of types matching the defensive condition.
    :return: Dictionary mapping each type to the number of Pokémon that meet the condition.
    """
    output: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        for item in defensive_func(pokemon.type_1, pokemon.type_2):
            output[item] += 1

    return output


def get_team_resistances(team: list[Pokemon]) -> dict[str, int]:
    """
    Calculates the number of Pokémon in the given team that resist each Pokémon type.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each Pokémon type to the number of team members
             that resist it.
    """
    return get_team_defensive_info(team, get_defensive_strengths)


def get_team_immunities(team: list[Pokemon]) -> dict[str, int]:
    """
    Calculates how many Pokémon in the team are immune to each Pokémon type.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each type to the number of Pokémon immune to it.
    """
    return get_team_defensive_info(team, get_immunities)


def get_team_defensive_weaknesses(team: list[Pokemon]) -> dict[str, int]:
    """
    Calculates how many Pokémon in the team are defensively weak to each Pokémon type.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each type to the number of Pokémon defensively weak to it.
    """
    return get_team_defensive_info(team, get_defensive_weaknesses)


def get_team_defensive_summary(team: list[Pokemon]) -> dict[str, dict[str, int]]:
    """
    Generates a defensive summary for the team.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary containing counts for defensive weaknesses, immunities, and resistances.
    """
    return {
        "defensive_weaknesses": get_team_defensive_weaknesses(team),
        "immunities": get_team_immunities(team),
        "resistances": get_team_resistances(team)
    }


def get_team_offensive_info(team: list[Pokemon], offensive_func: Callable) -> dict[str, int]:
    """
    Counts how many Pokémon in the team meet a given offensive condition. (i.e. offensively strong against a type)

    :param team: List of Pokémon objects representing the team.
    :param offensive_func: Function returning a list of types matching the defensive condition/
    :return: Dictionary mapping each target type to the number of Pokémon
             that can hit it effectively.
    """
    output: dict[str, int] = {pkm_type: 0 for pkm_type in pokemon_types}

    for pokemon in team:
        pokemon_set = set()

        pokemon_set.update(offensive_func(pokemon.type_1))

        if pokemon.type_2 is not None:
            pokemon_set.update(offensive_func(pokemon.type_2))

        for item in pokemon_set:
            output[item] += 1

    return output


def get_team_offensive_weaknesses(team: list[Pokemon]) -> dict[str, int]:
    return get_team_offensive_info(team, get_offensive_weaknesses)


def get_team_offensive_strengths(team: list[Pokemon]) -> dict[str, int]:
    return get_team_offensive_info(team, get_offensive_strengths)


def get_team_immune_defenders(team: list[Pokemon]) -> dict[str, int]:
    return get_team_offensive_info(team, get_immune_defenders)


def get_team_offensive_summary(team: list[Pokemon]) -> dict[str, dict[str, int]]:
    return {"offensive_weaknesses": get_team_offensive_weaknesses(team),
            "offensive_strengths": get_team_offensive_strengths(team),
            "immune_defenders": get_team_immune_defenders(team)}


def get_full_team_summary(team: list[Pokemon]) -> dict[str, dict[str, dict[str, int]]]:
    return {"offensive": get_team_offensive_summary(team),
            "defensive": get_team_defensive_summary(team)}
