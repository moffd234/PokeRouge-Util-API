from Application.extensions import db


class Pokemon(db.Model):
    def __init__(self, name: str, generation: int, sub_legendary: bool, legendary: bool, mythical: bool, category: str,
                 type_1: str, type_2: str | None, ability_1: str, ability_2: str | None, hidden_ability: str,
                 height: float, weight: float, base_total: int, base_hp: int, base_attack: int, base_defense: int,
                 base_sp_attack: int, base_sp_defense: int, base_speed: int, catch_rate: int, base_friendship: int,
                 base_exp: int, growth_rate: str, male_percent: float | None, gender_diffs: bool):
        self.name: str = name
        self.generation: int = generation
        self.sub_legendary: bool = sub_legendary
        self.legendary: bool = legendary
        self.mythical: bool = mythical
        self.category: str = category
        self.type_1: str = type_1
        self.type_2: str | None= type_2
        self.ability_1: str = ability_1
        self.ability_2: str | None = ability_2
        self.hidden_ability: str = hidden_ability
        self.height: float = height
        self.weight: float = weight
        self.base_total: int = base_total
        self.base_hp: int = base_hp
        self.base_attack: int = base_attack
        self.base_defense: int = base_defense
        self.base_sp_attack: int = base_sp_attack
        self.base_sp_defense: int = base_sp_defense
        self.base_speed: int = base_speed
        self.catch_rate: int = catch_rate
        self.base_friendship: int = base_friendship
        self.base_exp: int = base_exp
        self.growth_rate: str = growth_rate
        self.male_percent: float | None = male_percent
        self.gender_diffs: bool = gender_diffs


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), unique=True, nullable=False)
    generation = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50))

    sub_legendary = db.Column(db.Boolean, nullable=False)
    legendary = db.Column(db.Boolean, nullable=False)
    mythical = db.Column(db.Boolean, nullable=False)

    type_1 = db.Column(db.String(10), nullable=False)
    type_2 = db.Column(db.String(10))

    ability_1 = db.Column(db.String(30), nullable=False)
    ability_2 = db.Column(db.String(30))
    hidden_ability = db.Column(db.String(30))

    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    base_total = db.Column(db.Integer, nullable=False)
    base_hp = db.Column(db.Integer, nullable=False)
    base_attack = db.Column(db.Integer, nullable=False)
    base_defense = db.Column(db.Integer, nullable=False)
    base_sp_attack = db.Column(db.Integer, nullable=False)
    base_sp_defense = db.Column(db.Integer, nullable=False)
    base_speed = db.Column(db.Integer, nullable=False)

    catch_rate = db.Column(db.Integer, nullable=False)
    base_friendship = db.Column(db.Integer, nullable=False)
    base_exp = db.Column(db.Integer, nullable=False)
    growth_rate = db.Column(db.String(15), nullable=False)
    male_percent = db.Column(db.Float, nullable=True)
    gender_diffs = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Pokemon {self.name} (Gen {self.generation}, Type: {self.type_1} {self.type_2})>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "generation": self.generation,
            "category": self.category,
            "legendary_status": {
                "sub_legendary": self.sub_legendary,
                "legendary": self.legendary,
                "mythical": self.mythical,
            },
            "types": {
                "type_1": self.type_1,
                "type_2": self.type_2,
            },
            "abilities": {
                "ability_1": self.ability_1,
                "ability_2": self.ability_2,
                "hidden_ability": self.hidden_ability,
            },
            "size": {
                "height": self.height,
                "weight": self.weight,
            },
            "stats": {
                "total": self.base_total,
                "hp": self.base_hp,
                "attack": self.base_attack,
                "defense": self.base_defense,
                "sp_attack": self.base_sp_attack,
                "sp_defense": self.base_sp_defense,
                "speed": self.base_speed,
            },
            "catch_rate": self.catch_rate,
            "base_friendship": self.base_friendship,
            "base_exp": self.base_exp,
            "growth_rate": self.growth_rate,
            "male_percent": self.male_percent,
            "gender_diffs": self.gender_diffs,
        }
