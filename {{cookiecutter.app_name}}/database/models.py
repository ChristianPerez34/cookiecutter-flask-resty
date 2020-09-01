from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt_ = Bcrypt()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    _password = db.Column("password", db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = bcrypt_.generate_password_hash(password=password).decode(
            "utf-8"
        )

    def valid_credentials(self, password: str) -> bool:
        return bcrypt_.check_password_hash(pw_hash=self.password, password=password)
