from Application.Utils.TypeUtils import TypeUtils

type_utils: TypeUtils = TypeUtils()

from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import TypeUtils

type_util: TypeUtils = TypeUtils()


def get_team_weaknesses(team: list[Pokemon]) -> dict[str, set[str]]:
    output: dict[str, set[str]] = {"defensive_weakness": set(), "immunities": set(), "immune_defenders": set()}

    for pokemon in team:
        output["defensive_weakness"].update(type_util.get_defensive_weaknesses(pokemon.type_1, pokemon.type_2))
        output["immune_defenders"].update(
            type_util.get_immune_defenders(pokemon.type_1) + type_util.get_immune_defenders(pokemon.type_2))

    output["defensive_weakness"] -= output["immunities"]

    return output
