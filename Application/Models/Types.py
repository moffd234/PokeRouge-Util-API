from enum import Enum


class Types(Enum):

    def __init__(self, super_effective_to: list[str],
                 super_effective_from: list[str], weak_to: list[str], weak_from: list[str], no_effect_to: list[str],
                 no_effect_from: list[str]):
        """
        Initialize a type interaction profile for a Pokémon type.

        :param super_effective_to: A list of type names that this type is strong against (deals double damage to).
        :param super_effective_from: A list of type names that are strong against this type (takes double damage from).
        :param weak_to: A list of type names that this type is weak against (deals half damage to).
        :param weak_from: A list of type names that this type takes reduced damage from (takes half damage from).
        :param no_effect_to: A list of type names that this type cannot affect (deals no damage to).
        :param no_effect_from: A list of type names that cannot affect this type (takes no damage from).
        """
        self.super_effective_to = super_effective_to
        self.super_effective_from = super_effective_from
        self.weak_to = weak_to
        self.weak_from = weak_from
        self.no_effect_to = no_effect_to
        self.no_effect_from = no_effect_from

    NORMAL = ([], ["Fighting"], ["Rock", "Steel"], [], ["Ghost"],[])
    FIRE = (["Grass", "Bug", "Ice", "Steel"], ["Water", "Ground", "Rock"], ["Fire", "Grass", "Ice", "Steel", "Fairy", "Bug"],
            ["Fire", "Water", "Rock", "Dragon"], [], [])
    WATER = (['Fire', "Ground", "Rock"], ["Grass", "Electric"], ["Steel", "Water", "Fire", "Ice"],
             ["Water", "Grass", "Dragon"], [], [])
    GRASS = (["Water", "Ground", "Rock"], ["Fire", "Flying", "Bug", "Poison", "Ice"],
             ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"], ["Water", "Electric", "Grass"], [], [])

    ELECTRIC = (["Water", "Flying"], ["Ground"], ["Electric", "Flying", "Steel"], ["Grass", "Electric", "Dragon"],
                ["Ground"], [])
    ICE = (["Grass", "Ground", "Flying", "Dragon"], ["Fire", "Fighting", "Rock", "Steel"], ["Ice"],
           ["Fire", "Water", "Steel"], [], [])
    FIGHTING = (["Normal", "Steel", "Ice", "Rock", "Dark"], ["Psychic", "Fairy", "Flying"], ["Bug", "Rock", "Dark"],
                ["Poison", "Flying", "Psychic", "Bug", "Fairy"], [], [])
    POISON = (["Grass", "Fairy"], ["Ground", "Psychic"], ["Grass", "Fighting", "Poison", "Bug", "Fairy"],
              ["Poison", "Ground", "Rock", "Ghost"], ["Steel"], [])
    GROUND = (["Electric", "Fire", "Poison", "Rock", "Steel"], ["Water", "Grass", "Ice"], ["Poison", "Rock"],
              ["Grass", "Bug"], ["Flying"], ["Electric"])
    FLYING = (["Fighting", "Grass", "Bug"], ["Electric", "Ice", "Rock"], ["Fighting", "Grass", "Bug"],
              ["Electric", "Rock", "Steel"], ["Ground"], [])
    PSYCHIC = (["Fighting", "Poison"], ["Bug", "Ghost", "Dark"], ["Fighting", "Psychic"], ["Psychic", "Steel"],
               ["Dark"], [])
    BUG = (["Grass", "Psychic", "Dark"], ["Fire", "Flying", "Rock"], ["Grass", "Fighting", "Ground"],
           ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"], [], [])
    ROCK = (["Fire", "Ice", "Flying", "Bug"], ["Water", "Grass", "Fighting", "Ground", "Steel"],
            ["Normal", "Fire", "Poison", "Flying"], ["Fighting", "Ground", "Steel"], [], [])
    GHOST = (["Psychic", "Ghost"], ["Ghost", "Dark"], ["Poison", "Bug"], ["Dark"], [], ["Normal", "Fighting"])
    DRAGON = (["Dragon"], ["Dragon", "Fairy"], ["Fire", "Grass", "Water", "Electric"], ["Steel"], [], ["Fairy"])
    DARK = (["Psychic", "Ghost"], ["Fighting", "Bug", "Fairy"], ["Ghost", "Dark"], ["Fighting", "Fairy"],
            [], ["Psychic"])
    STEEL = (["Ice", "Rock", "Fairy"], ["Fire", "Fighting", "Ground"],
             ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"],
             ["Fire", "Water", "Electric", "Steel"], [], [])
    FAIRY = (["Dragon", "Fighting", "Dark"], ["Poison", "Steel"], ["Fighting", "Bug", "Dark"],
             ["Fire", "Poison", "Steel"], [], [])

    def to_dict(self) -> dict[str, list[str]]:
        return {
            "super_effective_to": self.super_effective_to,
            "super_effective_from": self.super_effective_from,
            "weak_to": self.weak_to,
            "weak_from": self.weak_from,
            "no_effect_to": self.no_effect_to,
            "no_effect_from": self.no_effect_from,
        }
