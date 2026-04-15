import os
import secrets

from flask import Flask

from Application.Frontend.Views import views_bp
from Application.Routes.Pokedex import pokedex_bp
from Application.Routes.Weakness import weaknesses_bp
from Application.extensions import db


def create_app(test_config: dict = None) -> Flask:
    app = Flask(__name__, template_folder="./Frontend/templates", static_folder="./Frontend/static")

    default_config = {
        'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL', 'sqlite:///pokerouge.db'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': os.getenv('SECRET_KEY', secrets.token_hex(32)),
        'SESSION_COOKIE_HTTPONLY': True,
        'SESSION_COOKIE_SAMESITE': 'Lax',
    }

    app.config.update(default_config)

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    app.register_blueprint(pokedex_bp)
    app.register_blueprint(weaknesses_bp)
    app.register_blueprint(views_bp)

    with app.app_context():
        db.create_all()

    return app
