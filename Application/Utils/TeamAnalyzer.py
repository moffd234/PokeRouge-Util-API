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
    """
    Calculates how many Pokémon in the team are offensively weak against each type.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each type to the number of Pokémon weak against it offensively.
    """
    return get_team_offensive_info(team, get_offensive_weaknesses)


def get_team_offensive_strengths(team: list[Pokemon]) -> dict[str, int]:
    """
    Calculates how many Pokémon in the team are offensively strong against each type.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each type to the number of Pokémon strong against it offensively.
    """
    return get_team_offensive_info(team, get_offensive_strengths)


def get_team_immune_defenders(team: list[Pokemon]) -> dict[str, int]:
    """
    Calculates how many Pokémon in the team are resisted by each type
    (i.e. ghost would be resisted 2 times if the team was Eevee, Snorlax, and Infernape).

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary mapping each type to the number of Pokémon in the team that doesn't affect that type.
    """
    return get_team_offensive_info(team, get_immune_defenders)


def get_team_offensive_summary(team: list[Pokemon]) -> dict[str, dict[str, int]]:
    """
    Generates an offensive summary for the team.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary containing counts for offensive weaknesses, strengths, and immune defenders.
    """
    return {"offensive_weaknesses": get_team_offensive_weaknesses(team),
            "offensive_strengths": get_team_offensive_strengths(team),
            "immune_defenders": get_team_immune_defenders(team)}


def get_full_team_summary(team: list[Pokemon]) -> dict[str, dict[str, dict[str, int]]]:
    """
    Generates a complete offensive and defensive summary for the team.

    :param team: List of Pokémon objects representing the team.
    :return: Dictionary containing both offensive and defensive summaries.
    """
    return {"offensive": get_team_offensive_summary(team),
            "defensive": get_team_defensive_summary(team)}


def get_recommended_offensive_types(team: list[Pokemon]) -> set[str]:
    """
    Suggests Pokémon types to improve the team's offensive coverage.

    :param team: List of Pokémon to analyze.
    :return: Set of suggested Pokémon types to improve offensive coverage.
    """
    summary: dict[str, dict[str, int]] = get_team_offensive_summary(team)
    suggested: set[str] = set()

    for defender_type, weakness_count in summary["offensive_weaknesses"].items():

        if weakness_count > 0 and summary["offensive_strengths"][defender_type] == 0:
            suggested.update(get_defensive_weaknesses(defender_type, None))

    for immune_type, weakness_count in summary["immune_defenders"].items():

        if weakness_count > 0 and summary["offensive_strengths"][immune_type] == 0:
            suggested.update(get_defensive_weaknesses(immune_type, None))

    return suggested


def get_recommended_defensive_types(team: list[Pokemon]) -> set[str]:
    """
    Suggests Pokémon types to improve the team's defensive coverage.

    :param team: List of Pokémon to analyze.
    :return: Set of suggested Pokémon types to improve defensive coverage.
    """
    summary: dict[str, dict[str, int]] = get_team_defensive_summary(team)
    suggested: set[str] = set()

    for attacking_type, weakness_count in summary["defensive_weaknesses"].items():

        if weakness_count > 0 and summary["resistances"][attacking_type] == 0 and summary["immunities"][
            attacking_type] == 0:
            suggested.update(get_defensive_strengths(attacking_type, None) + get_immunities(attacking_type, None))

    return suggested
