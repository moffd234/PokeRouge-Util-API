from Application.Models.Pokemon import Pokemon


class TypeUtils:

    def __init__(self):
        self.types: dict[str, dict[str, float]] = {
            "normal": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1,
                       "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 0.5, "ghost": 0,
                       "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 1},
            "fire": {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 1, "grass": 2, "ice": 2, "fighting": 1,
                     "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 2, "rock": 0.5, "ghost": 1,
                     "dragon": 0.5, "dark": 1, "steel": 2, "fairy": 1},
            "water": {"normal": 1, "fire": 2, "water": 0.5, "electric": 1, "grass": 0.5, "ice": 1, "fighting": 1,
                      "poison": 1, "ground": 2, "flying": 1, "psychic": 1, "bug": 1, "rock": 2, "ghost": 1,
                      "dragon": 0.5, "dark": 1, "steel": 1, "fairy": 1},
            "electric": {"normal": 1, "fire": 1, "water": 2, "electric": 0.5, "grass": 0.5, "ice": 1, "fighting": 1,
                         "poison": 1, "ground": 0, "flying": 2, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1,
                         "dragon": 0.5, "dark": 1, "steel": 1, "fairy": 1},
            "grass": {"normal": 1, "fire": 0.5, "water": 2, "electric": 1, "grass": 0.5, "ice": 1, "fighting": 1,
                      "poison": 0.5, "ground": 2, "flying": 0.5, "psychic": 1, "bug": 0.5, "rock": 2, "ghost": 1,
                      "dragon": 0.5, "dark": 1, "steel": 0.5, "fairy": 1},
            "ice": {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 1, "grass": 2, "ice": 0.5, "fighting": 1,
                    "poison": 1, "ground": 2, "flying": 2, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 2,
                    "dark": 1, "steel": 0.5, "fairy": 1},
            "fighting": {"normal": 2, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 2, "fighting": 1,
                         "poison": 0.5, "ground": 1, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2, "ghost": 0,
                         "dragon": 1, "dark": 2, "steel": 2, "fairy": 0.5},
            "poison": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 2, "ice": 1, "fighting": 1,
                       "poison": 0.5, "ground": 0.5, "flying": 1, "psychic": 1, "bug": 1, "rock": 0.5, "ghost": 0.5,
                       "dragon": 1, "dark": 1, "steel": 0, "fairy": 2},
            "ground": {"normal": 1, "fire": 2, "water": 1, "electric": 2, "grass": 0.5, "ice": 1, "fighting": 1,
                       "poison": 2, "ground": 1, "flying": 0, "psychic": 1, "bug": 0.5, "rock": 2, "ghost": 1,
                       "dragon": 1, "dark": 1, "steel": 2, "fairy": 1},
            "flying": {"normal": 1, "fire": 1, "water": 1, "electric": 0.5, "grass": 2, "ice": 1, "fighting": 2,
                       "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 2, "rock": 0.5, "ghost": 1,
                       "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 1},
            "psychic": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 2,
                        "poison": 2, "ground": 1, "flying": 1, "psychic": 0.5, "bug": 1, "rock": 1, "ghost": 1,
                        "dragon": 1, "dark": 0, "steel": 0.5, "fairy": 1},
            "bug": {"normal": 1, "fire": 0.5, "water": 1, "electric": 1, "grass": 2, "ice": 1, "fighting": 0.5,
                    "poison": 0.5, "ground": 1, "flying": 0.5, "psychic": 2, "bug": 1, "rock": 1, "ghost": 0.5,
                    "dragon": 1, "dark": 2, "steel": 0.5, "fairy": 0.5},
            "rock": {"normal": 1, "fire": 2, "water": 1, "electric": 1, "grass": 1, "ice": 2, "fighting": 0.5,
                     "poison": 1, "ground": 0.5, "flying": 2, "psychic": 1, "bug": 2, "rock": 1, "ghost": 1,
                     "dragon": 1, "dark": 1, "steel": 0.5, "fairy": 1},
            "ghost": {"normal": 0, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1,
                      "poison": 1, "ground": 1, "flying": 1, "psychic": 2, "bug": 1, "rock": 1, "ghost": 2, "dragon": 1,
                      "dark": 0.5, "steel": 1, "fairy": 1},
            "dragon": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1,
                       "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1,
                       "dragon": 2, "dark": 1, "steel": 0.5, "fairy": 0},
            "dark": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 0.5,
                     "poison": 1, "ground": 1, "flying": 1, "psychic": 2, "bug": 1, "rock": 1, "ghost": 2, "dragon": 1,
                     "dark": 0.5, "steel": 1, "fairy": 0.5},
            "steel": {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 0.5, "grass": 1, "ice": 2, "fighting": 1,
                      "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 2, "ghost": 1, "dragon": 1,
                      "dark": 1, "steel": 0.5, "fairy": 2},
            "fairy": {"normal": 1, "fire": 0.5, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 2,
                      "poison": 0.5, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1,
                      "dragon": 2, "dark": 2, "steel": 0.5, "fairy": 1},
        }

    def get_offensive_weaknesses(self, atk_type: str) -> list:
        """
        Returns a list of defending types that take half damage (0.5x) from the given attacking type.

        This method will raise a ValueError if the given attacking type is not recognized.

        :param atk_type: The attacking Pokémon type.
        :return: List of defending types that resist the given attacking type.
        """
        atk_type = atk_type.lower()

        if atk_type not in self.types:
            raise ValueError(f"'{atk_type.title()}' is not a valid type")

        matchups: dict[str, float] = self.types[atk_type]

        return sorted([defender for defender, multiplier in matchups.items() if multiplier == 0.5])

    def get_defensive_weaknesses(self, type_1: str, type_2: str | None) -> list:
        """
        Returns a list of attacking types that deal super-effective damage (>1x)
        to the given combination of defending types.

        This method will raise a ValueError if either `type_1` or `type_2` is not recognized.

        :param type_1: The primary defending type.
        :param type_2: The secondary defending type, or None.
        :return: A list of attacking types that are strong against the given type combination.
        """
        type_1 = type_1.lower()

        if type_1 not in self.types:
            raise ValueError(f"'{type_1.title()}' is not a valid type")

        if type_2 is not None:
            type_2 = type_2.lower()
            if type_2 not in self.types:
                raise ValueError(f"'{type_2.title()}' is not a valid type")

        output: list[str] = []

        for attacker in self.types:
            multiplier = self.types[attacker][type_1]

            if type_2:
                multiplier *= self.types[attacker][type_2]

            if multiplier > 1.0:
                output.append(attacker)

        return sorted(output)

    def get_immunities(self, type_1: str, type_2) -> list[str]:
        """
        Returns a list of attacking types that deal no damage (0x) to the given defending type(s).

        This method will raise a ValueError if either `type_1` or `type_2` is not recognized.

        :param type_1: The primary defending type.
        :param type_2: The secondary defending type, or None.
        :return: A list of attacking types the Pokémon is immune to.
        """
        type_1 = type_1.lower()

        if type_1 not in self.types:
            raise ValueError(f"'{type_1.title()}' is not a valid type")

        if type_2 is not None:
            type_2 = type_2.lower()
            if type_2 not in self.types:
                raise ValueError(f"'{type_2.title()}' is not a valid type")

        output: list[str] = []

        for attacker in self.types:
            multiplier = self.types[attacker][type_1]

            if type_2:
                multiplier *= self.types[attacker][type_2]

            if multiplier == 0:
                output.append(attacker)

        return sorted(output)

    def get_immune_defenders(self, attacker: str) -> list[str]:
        """
        Returns a list of defending types that are completely immune (0x damage)
        to the given attacking type.

        This method will raise a ValueError if the attacker type is not recognized.

        :param attacker: The attacking Pokémon type.
        :return: A list of defending types immune to the given attacker.
        """
        attacker = attacker.lower()

        if attacker not in self.types:
            raise ValueError(f"'{attacker.title()}' is not a valid type")

        attacker_matchups = self.types[attacker]

        return sorted([defender for defender, multiplier in attacker_matchups.items() if multiplier == 0])

    def get_weakness_summary(self, pokemon_species: Pokemon):
        """
        Returns a summary of type-based interactions for the given Pokémon species.

        This method will raise a ValueError if any of the Pokémon's types are not valid or unrecognized.

        :param pokemon_species: The Pokémon whose type weaknesses and immunities are being analyzed.
        :return: A dictionary summarizing offensive weaknesses, defensive weaknesses, immunities, and immune defenders.
        """
        try:
            type_1 = pokemon_species.type_1.lower()
            type_2 = pokemon_species.type_2.lower()

            offensive_weaknesses = {type_1: self.get_offensive_weaknesses(type_1)}
            immune_defenders = {type_1: self.get_immune_defenders(type_1)}

            if type_2:
                offensive_weaknesses[type_2] = self.get_offensive_weaknesses(type_2)
                immune_defenders[type_2] = self.get_immune_defenders(type_2)

            return {
                "offensive_weaknesses": offensive_weaknesses,
                "defensive_weaknesses": self.get_defensive_weaknesses(type_1, type_2),
                "immunities": self.get_immunities(type_1, type_2),
                "immune_defenders": immune_defenders
            }

        except ValueError as error:
            return {"error": str(error)}
