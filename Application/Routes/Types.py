import abc


class Types(abc.ABC):
    def __init__(self, super_effective_to: list[str], super_effective_from: list[str], weak_to: list[str],
                 weak_from: list[str], no_effect_to: list[str], no_effect_from: list[str]):
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
