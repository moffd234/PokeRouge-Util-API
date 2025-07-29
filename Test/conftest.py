import pytest
from flask import Flask
from Application import create_app, db
from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import TypeUtils


@pytest.fixture
def app():
    app: Flask = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def example_pokemon(app):
    """Creates an example Pokémon and add it to the database then removes it once test has run"""
    bulbasaur: Pokemon = Pokemon(name="BULBASAUR", generation=1, sub_legendary=False, legendary=False, mythical=False,
                                 category="Seed Pokemon", type_1="GRASS", type_2="POISON", ability_1="OVERGROW",
                                 ability_2=None, hidden_ability="CHLOROPHYLL", height=0.7, weight=6.9, base_total=318,
                                 base_hp=45, base_attack=49, base_defense=49, base_sp_attack=65, base_sp_defense=65,
                                 base_speed=45, catch_rate=45, base_friendship=50, base_exp=64,
                                 growth_rate="MEDIUM_SLOW", male_percent=87.5, gender_diffs=False)

    # Lunala is used due to its typing being useful for edge case testing
    lunala: Pokemon = Pokemon(name="LUNALA", generation=7, sub_legendary=False, legendary=True, mythical=False,
                              category="Moone Pokémon", type_1="PSYCHIC", type_2="GHOST", height=4, weight=120,
                              ability_1="SHADOW_SHIELD", ability_2="NONE", hidden_ability="NONE", base_total=680,
                              base_hp=137, base_attack=113, base_defense=89, base_sp_attack=137, base_sp_defense=107,
                              base_speed=97, catch_rate=3, base_friendship=0, base_exp=340, growth_rate="SLOW",
                              male_percent=None, gender_diffs=False)

    fake: Pokemon = Pokemon(name="FAKE_POKEMON", generation=7, sub_legendary=False, legendary=True, mythical=False,
                            category="Moone Pokémon", type_1="Sound", type_2="Sound", height=4, weight=120,
                            ability_1="SHADOW_SHIELD", ability_2="NONE", hidden_ability="NONE", base_total=680,
                            base_hp=137, base_attack=113, base_defense=89, base_sp_attack=137, base_sp_defense=107,
                            base_speed=97, catch_rate=3, base_friendship=0, base_exp=340, growth_rate="SLOW",
                            male_percent=None, gender_diffs=False)

    pokemon: dict[str, Pokemon] = {"bulbasaur": bulbasaur, "lunala": lunala, "fake": fake}

    db.session.add(bulbasaur)
    db.session.add(lunala)
    db.session.add(fake)
    db.session.commit()

    yield pokemon

    db.session.delete(bulbasaur)
    db.session.delete(lunala)
    db.session.delete(fake)
    db.session.commit()


@pytest.fixture
def type_utils():
    return TypeUtils()
