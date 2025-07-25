import pytest
from flask import Flask

from Application import create_app, db
from Application.Models.Pokemon import Pokemon


@pytest.fixture
def app():
    app: Flask = create_app()
    app.config['TESTING'] = True

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

    db.session.add(bulbasaur)
    db.session.commit()

    yield bulbasaur

    db.session.delete(bulbasaur)
    db.session.commit()

