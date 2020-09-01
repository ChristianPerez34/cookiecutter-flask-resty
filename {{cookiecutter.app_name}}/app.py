import os
from pathlib import Path

from flasgger import Swagger
from flask import Flask
from flask.cli import load_dotenv
from flask_migrate import Migrate
from flask_resty import Api

from database.models import db, bcrypt_
from routes import initialize_routes


def create_app() -> Flask:
    app = Flask(__name__)

    # Load application settings from environment variable.
    # If environment variable is not set will load development settings by default.
    app_settings = os.getenv("APP_SETTINGS", "settings.DevelopmentConfig")
    env_path = Path(".env.development").absolute()

    if not app_settings:
        raise ValueError('"APP_SETTINGS" environment variable not set')

    if app_settings == "settings.TestingConfig":
        env_path = Path(".env.testing")
    elif app_settings == "settings.ProductionConfig":
        env_path = Path(".env.production")

    # Load environment variables depending on application settings (Dev/Test/Prod)
    load_dotenv(path=env_path)
    app.config.from_object(app_settings)

    # Initialize Flask-SQLAlchemy ORM
    db.init_app(app)
    db.app = app

    # Initialize Flask-Migrate
    Migrate(app, db)

    # Initialize flask_resty api
    api = Api(app, prefix="/api")
    initialize_routes(api)

    # Initialize Flask-Bcrypt
    bcrypt_.init_app(app)

    # Initialize swagger
    template = {
        "components": {
            "securitySchemes": {
                "basicAuth": {"type": "http", "scheme": "basic"},
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                },
            }
        }
    }
    Swagger(app, template=template)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
