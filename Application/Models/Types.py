from enum import Enum


class Types(Enum):

    def __init__(self, offensively_strong: list[str], defensively_weak: list[str],
                 offensively_weak: list[str], defensively_strong: list[str], no_effect_to: list[str],
                 no_effect_from: list[str], offensively_neutral: list[str], defensively_neutral: list[str]):
        """
        Initialize a type interaction profile for a Pokémon type.

        :param offensively_strong: A list of type names that this type is strong against (deals double damage to).
        :param defensively_weak: A list of type names that are strong against this type (takes double damage from).
        :param offensively_weak: A list of type names that this type is weak against (deals half damage to).
        :param defensively_strong: A list of type names that this type takes reduced damage from (takes half damage from).
        :param no_effect_to: A list of type names that this type cannot affect (deals no damage to).
        :param no_effect_from: A list of type names that cannot affect this type (takes no damage from).
        :param offensively_neutral: A list of type names that are neutral against this type (deals 1x damage from ).
        :param defensively_neutral: A list of type names that are neutral against this type (takes 1x damage from).
        """
        self.offensively_strong = offensively_strong
        self.defensively_weak = defensively_weak
        self.offensively_weak = offensively_weak
        self.defensively_strong = defensively_strong
        self.no_effect_to = no_effect_to
        self.no_effect_from = no_effect_from
        self.offensively_neutral = offensively_neutral
        self.defensively_neutral = defensively_neutral

    NORMAL = ([], ["Fighting"], ["Rock", "Steel"], [], ["Ghost"],
              ["Normal", "Fighting", "Flying", "Poison", "Ground", "Bug", "FIre", "Water", "Grass", "Electric",
               "Psychic", "Ice", "Dragon", "Dark", "Fairy"],
              ["Normal", "Flying", "Poison", "Ground", "Rock", "Bug", "Steel", "Fire", "Water", "Grass", "Electric",
               "Psychic", "Ice", "Dragon", "Dark", "Fairy"])

    FIRE = (["Grass", "Bug", "Ice", "Steel"], ["Water", "Ground", "Rock"],
            ["Fire", "Grass", "Ice", "Steel", "Fairy", "Bug"],
            ["Fire", "Water", "Rock", "Dragon"], [], [],
            ["Normal", "Fighting", "Flying", "Poison", "Ground", "Ghost", "Electric", "Psychic", "Dark", "Fairy"],
            ["Normal", "Fighting", "Flying", "Poison", "Ghost", "Electric", "Psychic", "Dragon", "Dark"])

    WATER = (['Fire', "Ground", "Rock"], ["Grass", "Electric"], ["Steel", "Water", "Fire", "Ice"],
             ["Water", "Grass", "Dragon"], [], [],
             ["Normal", "Fighting", "Flying", "Poison", "Bug", "Ghost", "Steel", "Electric", "Psychic", "Ice", "Dark",
              "Fairy"],
             ["Normal", "Fighting," "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Psychic", "Dragon", "Dark",
              "Fairy"])
    GRASS = (["Water", "Ground", "Rock"], ["Fire", "Flying", "Bug", "Poison", "Ice"],
             ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"], ["Water", "Electric", "Grass"], [], [],
             ["Normal", "Fighting", "Ghost", "Electric", "Psychic", "Ice", "Dark", "Fairy"],
             ["Normal", "Fighting", "Rock", "Ghost", "Steel", "Psychic", "Dragon", "Dark", "Fairy"])

    ELECTRIC = (["Water", "Flying"], ["Ground"], ["Electric", "Flying", "Steel"], ["Grass", "Electric", "Dragon"],
                ["Ground"], [],
                ["Normal", "Fighting", "Poison", "Rock", "Bug", "Ghost", "Steel", "Fire", "Psychic", "Ice", "Dark",
                 "Fairy"],
                ["Normal", "Fighting", "Poison", "Rock", "Bug", "Ghost", "Fire", "Water", "Grass", "Psychic", "Ice",
                 "Dragon", "Dark", "Fairy"])

    ICE = (["Grass", "Ground", "Flying", "Dragon"], ["Fire", "Fighting", "Rock", "Steel"], ["Ice"],
           ["Fire", "Water", "Steel"], [], [],
           ["Normal", "Fighting", "Poison", "Rock", "Bug", "Ghost", "Electric", "Psychic", "Dark", "Fairy"],
           ["Normal", "Flying", "Poison", "Ground", "Bug", "Ghost", "Water", "Grass", "Electric", "Psychic", "Dragon",
            "Dark", "Fairy"])

    FIGHTING = (["Normal", "Steel", "Ice", "Rock", "Dark"], ["Psychic", "Fairy", "Flying"], ["Bug", "Rock", "Dark"],
                ["Poison", "Flying", "Psychic", "Bug", "Fairy"], [], [],
                ["Fighting", "Ground", "Fire", "Water", "Grass", "Electric", "Dragon"],
                ["Normal", "fighting", "Poison", "Ground", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric",
                 "Ice", "Dragon"])

    POISON = (["Grass", "Fairy"], ["Ground", "Psychic"], ["Grass", "Fighting", "Poison", "Bug", "Fairy"],
              ["Poison", "Ground", "Rock", "Ghost"], ["Steel"], [],
              ["Normal", "Fighting", "Flying", "Bug", "Fire", "Water", "Electric", "Psychic", "Ice", "Dragon", "Dark"],
              ["Normal", "Flying", "Rock", "Ghost", "Steel", "Fire", "Water", "Electric", "Ice", "Dragon", "Dark"])

    GROUND = (["Electric", "Fire", "Poison", "Rock", "Steel"], ["Water", "Grass", "Ice"], ["Poison", "Rock"],
              ["Grass", "Bug"], ["Flying"], ["Electric"],
              ["Normal", "Fighting", "Ground", "Ghost", "Water", "Psychic", "Ice", "Dragon", "Dark", "Fairy"],
              ["Normal", "Fighting", "Flying", "Ground", "Bug", "Ghost", "Steel", "Fire", "Psychic", "Dragon", "Dark",
               "Fairy"])

    FLYING = (["Fighting", "Grass", "Bug"], ["Electric", "Ice", "Rock"], ["Fighting", "Grass", "Bug"],
              ["Electric", "Rock", "Steel"], ["Ground"], [],
              ["Normal", "Flying", "Poison", "Ground", "Ghost", "Fire", "Water", "Psychic", "Ice", "Dragon", "Dark",
               "Fairy"],
              ["Normal", "Flying", "Poison", "Ghost", "Steel", "Fire", "Water", "Psychic", "Dragon", "Dark", "Fairy"])

    PSYCHIC = (["Fighting", "Poison"], ["Bug", "Ghost", "Dark"], ["Fighting", "Psychic"], ["Psychic", "Steel"],
               ["Dark"], [],
               ["Normal", "Flying", "Ground", "Rock", "Bug", "Ghost", "Fire", "Water", "Grass", "Electric", "Ice",
                "Dragon", "Fairy"],
               ["Normal", "Flying", "Poison", "Ground", "Rock", "Steel", "Fire", "Water", "Grass", "Electric", "Ice",
                "Dragon", "Fairy"])

    BUG = (["Grass", "Psychic", "Dark"], ["Fire", "Flying", "Rock"], ["Grass", "Fighting", "Ground"],
           ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"], [], [],
           ["Normal", "Ground", "Rock", "Bug", "Water", "Electric", "Ice", "Dragon"],
           ["Normal", "Poison", "Bug", "Ghost", "Steel", "Water", "Electric", "Psychic", "Ice", "Dragon", "Dark",
            "Fairy"])

    ROCK = (["Fire", "Ice", "Flying", "Bug"], ["Water", "Grass", "Fighting", "Ground", "Steel"],
            ["Normal", "Fire", "Poison", "Flying"], ["Fighting", "Ground", "Steel"], [], [],
            ["Normal", "Poison", "Rock", "Ghost", "Water", "Grass", "Electric", "Psychic", "Dragon", "Dark", "Fairy"],
            ["Rock", "Bug", "Ghost", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"])

    GHOST = (["Psychic", "Ghost"], ["Ghost", "Dark"], ["Poison", "Bug"], ["Dark"], [], ["Normal", "Fighting"],
             ["Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Steel", "Fire", "Water", "Grass", "Electric",
              "Ice", "Dragon", "Fairy"],
             ["Flying", "Ground", "Rock", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon",
              "Fairy"])

    DRAGON = (["Dragon"], ["Dragon", "Fairy"], ["Fire", "Grass", "Water", "Electric"], ["Steel"], [], ["Fairy"],
              ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Fire", "Water", "Grass",
               "Electric", "Psychic", "Ice", "Dark"],
              ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Psychic", "Dark"])

    DARK = (["Psychic", "Ghost"], ["Fighting", "Bug", "Fairy"],
            ["Ghost", "Dark"], ["Fighting", "Fairy"], [], ["Psychic"],
            ["Normal", "Flying", "Poison", "Ground", "Rock", "Bug", "Steel", "Fire", "Water", "Grass", "Electric",
             "Ice", "Dragon"],
            ["Normal", "Flying", "Poison", "Ground", "Rock", "Steel", "Fire", "Water", "Grass", "Electric", "Ice",
             "Dragon"])

    STEEL = (["Ice", "Rock", "Fairy"], ["Fire", "Fighting", "Ground"],
             ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"],
             ["Fire", "Water", "Electric", "Steel"], [], [],
             ["Normal", "Fighting", "Flying", "Poison", "Ground", "Bug", "Ghost", "Grass", "Psychic", "Dragon", "Dark"],
             [None])

    FAIRY = (["Dragon", "Fighting", "Dark"], ["Poison", "Steel"], ["Fighting", "Bug", "Dark"],
             ["Fire", "Poison", "Steel"], [], [],
             ["Normal", "Flying", "Ground", "Rock", "Bug", "Ghost", "Water", "Grass", "Electric", "Psychic", "Ice",
              "Fairy"], [None])

    def to_dict(self) -> dict[str, list[str]]:
        return {
            "offensively_strong": self.offensively_strong,
            "defensively_weak": self.defensively_weak,
            "offensively_weak": self.offensively_weak,
            "defensively_strong": self.defensively_strong,
            "no_effect_to": self.no_effect_to,
            "no_effect_from": self.no_effect_from,
        }
