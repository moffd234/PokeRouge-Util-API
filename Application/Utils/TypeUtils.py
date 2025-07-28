class TypeUtils:

    def __init__(self):
        self.types: dict[str: dict] = {
            "normal": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1,
                       "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 0.5, "ghost": 0,
                       "dragon": 1, "dark": 1, "steel": 0.5},
            "fire": {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 1, "grass": 2, "ice": 2, "fighting": 1,
                     "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 2, "rock": 0.5, "ghost": 1,
                     "dragon": 0.5, "dark": 1, "steel": 2},
            "water": {"normal": 1, "fire": 2, "water": 0.5, "electric": 1, "grass": 0.5, "ice": 1, "fighting": 1,
                      "poison": 1, "ground": 2, "flying": 1, "psychic": 1, "bug": 1, "rock": 2, "ghost": 1,
                      "dragon": 0.5, "dark": 1, "steel": 1},
            "electric": {"normal": 1, "fire": 1, "water": 2, "electric": 0.5, "grass": 0.5, "ice": 1, "fighting": 1,
                         "poison": 1, "ground": 0, "flying": 2, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1,
                         "dragon": 0.5, "dark": 1, "steel": 1},
            "grass": {"normal": 1, "fire": 0.5, "water": 2, "electric": 1, "grass": 0.5, "ice": 1, "fighting": 1,
                      "poison": 0.5, "ground": 2, "flying": 0.5, "psychic": 1, "bug": 0.5, "rock": 2, "ghost": 1,
                      "dragon": 0.5, "dark": 1, "steel": 0.5},
            "ice": {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 1, "grass": 2, "ice": 0.5, "fighting": 1,
                    "poison": 1, "ground": 2, "flying": 2, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 2,
                    "dark": 1, "steel": 0.5},
            "fighting": {"normal": 2, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 2, "fighting": 1,
                         "poison": 0.5, "ground": 1, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2, "ghost": 0,
                         "dragon": 1, "dark": 2, "steel": 2},
            "poison": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 2, "ice": 1, "fighting": 1,
                       "poison": 0.5, "ground": 0.5, "flying": 1, "psychic": 1, "bug": 1, "rock": 0.5, "ghost": 0.5,
                       "dragon": 1, "dark": 1, "steel": 0},
            "ground": {"normal": 1, "fire": 2, "water": 1, "electric": 2, "grass": 0.5, "ice": 1, "fighting": 1,
                       "poison": 2, "ground": 1, "flying": 0, "psychic": 1, "bug": 0.5, "rock": 2, "ghost": 1,
                       "dragon": 1, "dark": 1, "steel": 2},
            "flying": {"normal": 1, "fire": 1, "water": 1, "electric": 0.5, "grass": 2, "ice": 1, "fighting": 2,
                       "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 2, "rock": 0.5, "ghost": 1,
                       "dragon": 1, "dark": 1, "steel": 0.5},
            "psychic": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 2,
                        "poison": 2, "ground": 1, "flying": 1, "psychic": 0.5, "bug": 1, "rock": 1, "ghost": 1,
                        "dragon": 1, "dark": 0, "steel": 0.5},
            "bug": {"normal": 1, "fire": 0.5, "water": 1, "electric": 1, "grass": 2, "ice": 1, "fighting": 0.5,
                    "poison": 0.5, "ground": 1, "flying": 0.5, "psychic": 2, "bug": 1, "rock": 1, "ghost": 0.5,
                    "dragon": 1, "dark": 2, "steel": 0.5},
            "rock": {"normal": 1, "fire": 2, "water": 1, "electric": 1, "grass": 1, "ice": 2, "fighting": 0.5,
                     "poison": 1, "ground": 0.5, "flying": 2, "psychic": 1, "bug": 2, "rock": 1, "ghost": 1,
                     "dragon": 1, "dark": 1, "steel": 0.5},
            "ghost": {"normal": 0, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1,
                      "poison": 1, "ground": 1, "flying": 1, "psychic": 2, "bug": 1, "rock": 1, "ghost": 2, "dragon": 1,
                      "dark": 0.5, "steel": 0.5},
            "dragon": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 1,
                       "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1,
                       "dragon": 2, "dark": 1, "steel": 0.5},
            "dark": {"normal": 1, "fire": 1, "water": 1, "electric": 1, "grass": 1, "ice": 1, "fighting": 0.5,
                     "poison": 1, "ground": 1, "flying": 1, "psychic": 2, "bug": 1, "rock": 1, "ghost": 2, "dragon": 1,
                     "dark": 0.5, "steel": 0.5},
            "steel": {"normal": 1, "fire": 0.5, "water": 0.5, "electric": 0.5, "grass": 1, "ice": 2, "fighting": 1,
                      "poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 2, "ghost": 1, "dragon": 1,
                      "dark": 1, "steel": 0.5}
        }

    def get_offensive_weaknesses(self, atk_type: str) -> list:
        if atk_type.lower() not in self.types:
            raise ValueError(f"'{atk_type}' is not a valid type")

        matchups: dict[str: str] = self.types[atk_type.lower()]

        return [defender for defender, multiplier in matchups.items() if multiplier == 0.5]

    def get_defensive_weaknesses(self, type_1: str, type_2: str | None) -> list:
        type_1 = type_1.lower()
        if type_1 not in self.types:
            raise ValueError(f"'{type_1}' is not a valid type")

        if type_2 is not None:
            type_2 = type_2.lower()
            if type_2 not in self.types:
                raise ValueError(f"'{type_2}' is not a valid type")

        output: list[str] = []

        for attacker in self.types:
            multiplier = self.types[attacker][type_1]

            if type_2:
                multiplier *= self.types[attacker][type_2]

            if multiplier > 1.0:
                output.append(attacker)

        return output
