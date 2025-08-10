from Application.Utils.TypeUtils import *


def get_team_weaknesses(team: list[Pokemon]) -> dict[str, set[str]]:
    output: dict[str, set[str]] = {"defensive_weakness": set(), "immunities": set(), "immune_defenders": set()}

    for pokemon in team:
        output["defensive_weakness"].update(get_defensive_weaknesses(pokemon.type_1, pokemon.type_2))
        output["immune_defenders"].update(get_immune_defenders(pokemon.type_1) + get_immune_defenders(pokemon.type_2))

    output["defensive_weakness"] -= output["immunities"]

    return output


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
