import datetime

import jwt
from flask import current_app as app
from marshmallow import Schema, fields, validate, ValidationError, post_dump, validates

from utils import contains_upper_case, contains_digit, contains_special_char


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.String(validate=validate.Length(max=30), required=True)
    email = fields.Email(validate=validate.Length(max=50), required=True)


class AuthUserSchema(UserSchema):
    password = fields.String(load_only=True, required=True)

    @validates
    def validate_password(self, password):
        if (
            not 8 <= len(password) <= 16
            or not contains_upper_case(password)
            or not contains_digit(password)
            or not contains_special_char(password)
        ):
            raise ValidationError(
                "Passwords must have 8-16 characters and at least 1 upper case, 1 digit, and 1 special character ("
                "~!@#$%^&*()_-) "
            )

    @post_dump
    def generate_token(self, data, **kwargs):
        payload = {
            "id": data["user_id"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            "iss": app.config["RESTY_JWT_DECODE_KEY_ISSUER"],
        }
        key = app.config["RESTY_JWT_DECODE_KEY"]
        algorithm = app.config["RESTY_JWT_DECODE_KEY_ALGORITHMS"]
        token = jwt.encode(payload=payload, key=key, algorithm=algorithm)
        data["token"] = token.decode("utf-8")
        return data
