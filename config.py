from flask import Flask

from src.apps.bookstore.blueprints.authors_blueprint import authors_blueprint
from src.apps.bookstore.blueprints.health_check_blueprint import health_check_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(authors_blueprint)
    app.register_blueprint(health_check_blueprint)

    return app
