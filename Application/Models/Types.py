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

    NORMAL = ([], ["FIGHTING"], ["ROCK", "STEEL"], [], ["GHOST"],
              ["NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "BUG", "FIRE", "WATER", "GRASS", "ELECTRIC",
               "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"],
              ["NORMAL", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC",
               "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"],
              ["NORMAL", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC",
               "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"])

    FIRE = (["GRASS", "BUG", "ICE", "STEEL"], ["WATER", "GROUND", "ROCK"],
            ["FIRE", "GRASS", "ICE", "STEEL", "FAIRY", "BUG"],
            ["FIRE", "WATER", "ROCK", "DRAGON"], [], [],
            ["NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "GHOST", "ELECTRIC", "PSYCHIC", "DARK", "FAIRY"],
            ["NORMAL", "FIGHTING", "FLYING", "POISON", "GHOST", "ELECTRIC", "PSYCHIC", "DRAGON", "DARK"])

    WATER = (['FIRE', "GROUND", "ROCK"], ["GRASS", "ELECTRIC"], ["STEEL", "WATER", "FIRE", "ICE"],
             ["WATER", "GRASS", "DRAGON"], [], [],
             ["NORMAL", "FIGHTING", "FLYING", "POISON", "BUG", "GHOST", "STEEL", "ELECTRIC", "PSYCHIC", "ICE", "DARK",
              "FAIRY"],
             ["NORMAL", "FIGHTING," "FLYING", "POISON", "GROUND", "ROCK", "BUG", "GHOST", "PSYCHIC", "DRAGON", "DARK",
              "FAIRY"])
    GRASS = (["WATER", "GROUND", "ROCK"], ["FIRE", "FLYING", "BUG", "POISON", "ICE"],
             ["FIRE", "GRASS", "POISON", "FLYING", "BUG", "DRAGON", "STEEL"], ["WATER", "ELECTRIC", "GRASS"], [], [],
             ["NORMAL", "FIGHTING", "GHOST", "ELECTRIC", "PSYCHIC", "ICE", "DARK", "FAIRY"],
             ["NORMAL", "FIGHTING", "ROCK", "GHOST", "STEEL", "PSYCHIC", "DRAGON", "DARK", "FAIRY"])

    ELECTRIC = (["WATER", "FLYING"], ["GROUND"], ["ELECTRIC", "FLYING", "STEEL"], ["GRASS", "ELECTRIC", "DRAGON"],
                ["GROUND"], [],
                ["NORMAL", "FIGHTING", "POISON", "ROCK", "BUG", "GHOST", "STEEL", "FIRE", "PSYCHIC", "ICE", "DARK",
                 "FAIRY"],
                ["NORMAL", "FIGHTING", "POISON", "ROCK", "BUG", "GHOST", "FIRE", "WATER", "GRASS", "PSYCHIC", "ICE",
                 "DRAGON", "DARK", "FAIRY"])

    ICE = (["GRASS", "GROUND", "FLYING", "DRAGON"], ["FIRE", "FIGHTING", "ROCK", "STEEL"], ["ICE"],
           ["FIRE", "WATER", "STEEL"], [], [],
           ["NORMAL", "FIGHTING", "POISON", "ROCK", "BUG", "GHOST", "ELECTRIC", "PSYCHIC", "DARK", "FAIRY"],
           ["NORMAL", "FLYING", "POISON", "GROUND", "BUG", "GHOST", "WATER", "GRASS", "ELECTRIC", "PSYCHIC", "DRAGON",
            "DARK", "FAIRY"])

    FIGHTING = (["NORMAL", "STEEL", "ICE", "ROCK", "DARK"], ["PSYCHIC", "FAIRY", "FLYING"], ["BUG", "ROCK", "DARK"],
                ["POISON", "FLYING", "PSYCHIC", "BUG", "FAIRY"], [], [],
                ["FIGHTING", "GROUND", "FIRE", "WATER", "GRASS", "ELECTRIC", "DRAGON"],
                ["NORMAL", "fighting", "POISON", "GROUND", "GHOST", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC",
                 "ICE", "DRAGON"])

    POISON = (["GRASS", "FAIRY"], ["GROUND", "PSYCHIC"], ["GRASS", "FIGHTING", "POISON", "BUG", "FAIRY"],
              ["POISON", "GROUND", "ROCK", "GHOST"], ["STEEL"], [],
              ["NORMAL", "FIGHTING", "FLYING", "BUG", "FIRE", "WATER", "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK"],
              ["NORMAL", "FLYING", "ROCK", "GHOST", "STEEL", "FIRE", "WATER", "ELECTRIC", "ICE", "DRAGON", "DARK"])

    GROUND = (["ELECTRIC", "FIRE", "POISON", "ROCK", "STEEL"], ["WATER", "GRASS", "ICE"], ["POISON", "ROCK"],
              ["GRASS", "BUG"], ["FLYING"], ["ELECTRIC"],
              ["NORMAL", "FIGHTING", "GROUND", "GHOST", "WATER", "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"],
              ["NORMAL", "FIGHTING", "FLYING", "GROUND", "BUG", "GHOST", "STEEL", "FIRE", "PSYCHIC", "DRAGON", "DARK",
               "FAIRY"])

    FLYING = (["FIGHTING", "GRASS", "BUG"], ["ELECTRIC", "ICE", "ROCK"], ["FIGHTING", "GRASS", "BUG"],
              ["ELECTRIC", "ROCK", "STEEL"], ["GROUND"], [],
              ["NORMAL", "FLYING", "POISON", "GROUND", "GHOST", "FIRE", "WATER", "PSYCHIC", "ICE", "DRAGON", "DARK",
               "FAIRY"],
              ["NORMAL", "FLYING", "POISON", "GHOST", "STEEL", "FIRE", "WATER", "PSYCHIC", "DRAGON", "DARK", "FAIRY"])

    PSYCHIC = (["FIGHTING", "POISON"], ["BUG", "GHOST", "DARK"], ["FIGHTING", "PSYCHIC"], ["PSYCHIC", "STEEL"],
               ["DARK"], [],
               ["NORMAL", "FLYING", "GROUND", "ROCK", "BUG", "GHOST", "FIRE", "WATER", "GRASS", "ELECTRIC", "ICE",
                "DRAGON", "FAIRY"],
               ["NORMAL", "FLYING", "POISON", "GROUND", "ROCK", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC", "ICE",
                "DRAGON", "FAIRY"])

    BUG = (["GRASS", "PSYCHIC", "DARK"], ["FIRE", "FLYING", "ROCK"], ["GRASS", "FIGHTING", "GROUND"],
           ["FIRE", "FIGHTING", "POISON", "FLYING", "GHOST", "STEEL", "FAIRY"], [], [],
           ["NORMAL", "GROUND", "ROCK", "BUG", "WATER", "ELECTRIC", "ICE", "DRAGON"],
           ["NORMAL", "POISON", "BUG", "GHOST", "STEEL", "WATER", "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK",
            "FAIRY"])

    ROCK = (["FIRE", "ICE", "FLYING", "BUG"], ["WATER", "GRASS", "FIGHTING", "GROUND", "STEEL"],
            ["NORMAL", "FIRE", "POISON", "FLYING"], ["FIGHTING", "GROUND", "STEEL"], [], [],
            ["NORMAL", "POISON", "ROCK", "GHOST", "WATER", "GRASS", "ELECTRIC", "PSYCHIC", "DRAGON", "DARK", "FAIRY"],
            ["ROCK", "BUG", "GHOST", "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY"])

    GHOST = (["PSYCHIC", "GHOST"], ["GHOST", "DARK"], ["POISON", "BUG"], ["DARK"], [], ["NORMAL", "FIGHTING"],
             ["FIGHTING", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC",
              "ICE", "DRAGON", "FAIRY"],
             ["FLYING", "GROUND", "ROCK", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC", "PSYCHIC", "ICE", "DRAGON",
              "FAIRY"])

    DRAGON = (["DRAGON"], ["DRAGON", "FAIRY"], ["FIRE", "GRASS", "WATER", "ELECTRIC"], ["STEEL"], [], ["FAIRY"],
              ["NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "GHOST", "FIRE", "WATER", "GRASS",
               "ELECTRIC", "PSYCHIC", "ICE", "DARK"],
              ["NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "GHOST", "STEEL", "PSYCHIC", "DARK"])

    DARK = (["PSYCHIC", "GHOST"], ["FIGHTING", "BUG", "FAIRY"],
            ["GHOST", "DARK"], ["FIGHTING", "FAIRY"], [], ["PSYCHIC"],
            ["NORMAL", "FLYING", "POISON", "GROUND", "ROCK", "BUG", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC",
             "ICE", "DRAGON"],
            ["NORMAL", "FLYING", "POISON", "GROUND", "ROCK", "STEEL", "FIRE", "WATER", "GRASS", "ELECTRIC", "ICE",
             "DRAGON"])

    STEEL = (["ICE", "ROCK", "FAIRY"], ["FIRE", "FIGHTING", "GROUND"],
             ["NORMAL", "GRASS", "ICE", "FLYING", "PSYCHIC", "BUG", "ROCK", "DRAGON", "STEEL", "FAIRY"],
             ["FIRE", "WATER", "ELECTRIC", "STEEL"], [], [],
             ["NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "BUG", "GHOST", "GRASS", "PSYCHIC", "DRAGON", "DARK"],
             ["GHOST", "WATER", "ELECTRIC", "DARK"])

    FAIRY = (["DRAGON", "FIGHTING", "DARK"], ["POISON", "STEEL"], ["FIGHTING", "BUG", "DARK"],
             ["FIRE", "POISON", "STEEL"], [], [],
             ["NORMAL", "FLYING", "GROUND", "ROCK", "BUG", "GHOST", "WATER", "GRASS", "ELECTRIC", "PSYCHIC", "ICE",
              "FAIRY"],
             ["NORMAL", "FLYING", "GROUND", "ROCK", "GHOST", "FIRE", "WATER", "GRASS", "ELECTRIC", "PSYCHIC", "ICE",
              "FAIRY"])

    def to_dict(self) -> dict[str, list[str]]:
        return {
            "offensively_strong": self.offensively_strong,
            "defensively_weak": self.defensively_weak,
            "offensively_weak": self.offensively_weak,
            "defensively_strong": self.defensively_strong,
            "no_effect_to": self.no_effect_to,
            "no_effect_from": self.no_effect_from,
        }
