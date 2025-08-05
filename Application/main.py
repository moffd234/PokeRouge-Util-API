from Application import create_app
from Application.Utils.LoggingController import setup_logging

app = create_app()

setup_logging()

if __name__ == '__main__':
    app.run(debug=True)
