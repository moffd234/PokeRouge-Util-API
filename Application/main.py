import os

from Application import create_app
from Application.Utils.LoggingController import setup_logging

app = create_app()

setup_logging()

if __name__ == '__main__':
    debug_mode: bool = os.getenv('FLASK_DEBUG', 'false').strip().lower() == 'true'
    app.run(debug=debug_mode)
