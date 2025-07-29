from flask import Flask

from Application.Routes.Weakness import weaknesses_bp
from Application.extensions import db
from Application.Routes.Pokedex import pokedex_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokerouge.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(pokedex_bp)
    app.register_blueprint(weaknesses_bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
