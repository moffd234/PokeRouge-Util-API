import json
from Application import create_app, db
from Application.Models.Pokemon import Pokemon


def build_pokemon(entry: dict) -> Pokemon:
    def parse_type(value):
        return None if value == "NONE" else value

    def parse_value(value):
        return value

    def parse_float(value) -> float | None:
        try:
            if value == "" or value is None:
                return None
            return float(value)
        except (ValueError, TypeError):
            return None

    return Pokemon(
        name=entry["id"],
        generation=entry["generation"],
        sub_legendary=entry["subLegendary"],
        legendary=entry["legendary"],
        mythical=entry["mythical"],
        category=entry["category"],
        type_1=parse_type(entry.get("type1")),
        type_2=parse_type(entry.get("type2")),
        ability_1=parse_value(entry.get("ability1")),
        ability_2=parse_type(entry.get("ability2")),
        hidden_ability=parse_value(entry.get("abilityHidden")),
        height=parse_float(entry.get("height")),
        weight=parse_float(entry.get("weight")),
        base_total=entry["baseTotal"],
        base_hp=entry["baseHp"],
        base_attack=entry["baseAtk"],
        base_defense=entry["baseDef"],
        base_sp_attack=entry["baseSpatk"],
        base_sp_defense=entry["baseSpdef"],
        base_speed=entry["baseSpd"],
        catch_rate=entry["catchRate"],
        base_friendship=entry["baseFriendship"],
        base_exp=entry["baseExp"],
        growth_rate=entry["growthRate"],
        male_percent=parse_float(entry.get("malePercent")),
        gender_diffs=entry["genderDiffs"],
    )


def seed_pokemon_species():
    app = create_app()

    with app.app_context():
        with open("../Data/pokemon_species.json", "r") as file:
            data: dict = json.load(file)

        added: int = 0
        for entry in data:
            try:
                if db.session.get(Pokemon, entry["id"]):
                    print(f"⚠️  Skipped: {entry['id']}")
                    continue

                pokemon = build_pokemon(entry)
                db.session.add(pokemon)
                db.session.flush()

                added += 1
                print(f"✅ Added: {entry['id']}")

            except Exception as e:
                db.session.rollback()
                print(f"Failed to add Pokémon {entry.get('id', 'UNKNOWN')}: {e}")

        try:
            db.session.commit()
            print(f"\nSeed complete. {added} Pokémon added.")
        except Exception as e:
            db.session.rollback()
            print(f"Final db commit failed: {e}")


if __name__ == "__main__":
    seed_pokemon_species()
