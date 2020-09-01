import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "{{cookiecutter.app_name}}-secret")

    RESTY_JWT_DECODE_KEY = os.getenv(
        "JWT_SECRET_KEY", "{{cookiecutter.app_name}}-jwt-secret"
    )
    RESTY_JWT_DECODE_KEY_ALGORITHMS = os.getenv("JWT_ALGORITHM", "HS256")
    RESTY_JWT_DECODE_KEY_ISSUER = os.getenv(
        "JWT_ISSUER", "{{cookiecutter.app_name}}-jwt-issuer"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BCRYPT_LOG_ROUNDS = 12

    SWAGGER = {
        "title": "{{cookiecutter.app_name}}",
        "description": "API endpoints documentation",
        "uiversion": 3,
        "openapi": "3.0.2",
    }

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError('"DATABASE_URI" environment variable not set')


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_ECHO = False
