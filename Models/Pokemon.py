from Application import db


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), unique=True, nullable=False)
    generation = db.Column(db.Integer, nullable=False)

    sub_legendary = db.Column(db.Boolean, nullable=False)
    legendary = db.Column(db.Boolean, nullable=False)
    mythical = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(50))

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
    male_percent = db.Column(db.Float, nullable=False)
    gender_diffs = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Pokemon {self.name} (Gen {self.generation}, Type: {self.type_1} {self.type_2})>"