import json
import os

import pytest
from flask import Flask
from Application import create_app, db
from Application.Models.Pokemon import Pokemon
from Application.Utils.TypeUtils import TypeUtils
from Application.Utils.PokemonSeed import build_pokemon


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session", autouse=True)
def seeded_pokemon(app):
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../Application/Data/pokemon_species.json")

    with open(json_path) as f:
        data = json.load(f)

    for entry in data:
        db.session.add(build_pokemon(entry))

    fake: Pokemon = Pokemon(name="FAKE_POKEMON", generation=7, sub_legendary=False, legendary=True, mythical=False,
                            category="Moone Pokémon", type_1="Sound", type_2="Sound", height=4, weight=120,
                            ability_1="SHADOW_SHIELD", ability_2="NONE", hidden_ability="NONE", base_total=680,
                            base_hp=137, base_attack=113, base_defense=89, base_sp_attack=137, base_sp_defense=107,
                            base_speed=97, catch_rate=3, base_friendship=0, base_exp=340, growth_rate="SLOW",
                            male_percent=None, gender_diffs=False)
    db.session.add(fake)
    db.session.commit()

    yield

    db.session.query(Pokemon).delete()
    db.session.commit()


@pytest.fixture
def type_utils():
    return TypeUtils()
