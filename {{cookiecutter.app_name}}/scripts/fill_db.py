import flask
from flask import Flask

from app import create_app
from database.models import User
from database.schemas import AuthUserSchema


def fill_db_initial_data(app_: Flask):
    with app_.app_context():
        session = flask.current_app.extensions["sqlalchemy"].db.session
        user_data = {
            "email": "test2@test.com",
            "username": "test_user2",
            "password": "Tester1!",
        }
        user_schema = AuthUserSchema().load(user_data)
        user = User(**user_schema)

        session.add(user)
        session.commit()


if __name__ == "__main__":
    app = create_app()
    fill_db_initial_data(app)
