from flask import Flask

def create_app() -> Flask:
    application: Flask = Flask(__name__)

    # Blueprints will go here

    return application


if __name__ == '__main__':
    app: Flask = create_app()
    app.run(debug=True)

