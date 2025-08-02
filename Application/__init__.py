from flask import Flask
from Application.Routes.Weakness import weaknesses_bp
from Application.Routes.Pokedex import pokedex_bp
from Application.Frontend.Views import views_bp
from Application.extensions import db


def create_app(test_config: dict = None) -> Flask:
    app = Flask(__name__, template_folder="./Frontend/templates", static_folder="./Frontend/static")

    if test_config:
        app.config.update(test_config)

    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokerouge.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(pokedex_bp)
    app.register_blueprint(weaknesses_bp)
    app.register_blueprint(views_bp)

    with app.app_context():
        db.create_all()

    return app
