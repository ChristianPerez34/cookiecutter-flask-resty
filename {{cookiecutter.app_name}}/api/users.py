from flask import request, Response
from flask_resty import GenericModelView, ApiError
from flask_resty import (
    NoOpAuthorization,
)
from flask_resty.authentication import NoOpAuthentication

from auth.auth import PyJwtAuthentication, StandardAuthorization
from database.models import User
from database.schemas import AuthUserSchema, UserSchema


class UserViewBase(GenericModelView):
    id_fields = ("user_id",)
    model = User
    schema = UserSchema()


class AuthUserViewBase(UserViewBase):
    schema = AuthUserSchema()
    authentication = NoOpAuthentication()
    authorization = NoOpAuthorization()


class LoginUserView(AuthUserViewBase):
    def post(self) -> Response:
        """
        Endpoint returning authenticated user's basic info and access token
        User credentials must be sent via request Basic Auth header to log in and receive access token.
        ---
        tags:
          - auth
        definitions:
          User:
            type: object
            properties:
              user_id:
                type: integer
                description: The id of the user entry
              username:
                type: string
                description: The user name of the user entry
              email:
                type: string
                description: The email of the user entry
              password:
                type: string
                description: The password of the user entry
        security:
          - basicAuth: []
        responses:
          200:
            description: Basic info of authenticated user with access token
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    data:
                      allOf:
                        - $ref: '#/definitions/User'
                        - type: object
                          properties:
                            token:
                              type: string
                              description: JWT token
                          example:
                            user_id: 1
                            username: "test_user"
                            email: "test_user@test.com"
                            token: "JWT-TOKEN"
        """
        auth = request.authorization

        if not auth:
            raise ApiError(401, {"code": "invalid_credentials.missing_auth_header"})

        username = auth.username
        password = auth.password
        user = User.query.filter(User.username == username).first()

        if not user.valid_credentials(password):
            raise ApiError(401, {"code": "invalid_credentials"})

        data = self.schema.dump(user)
        return self.make_response(data)


class RegisterUserView(AuthUserViewBase):
    def get_location(self, item) -> None:
        return None

    def post(self) -> Response:
        """
        Endpoint for registering a new user
        User passwords are hashed before stored in the database
        ---
        tags:
          - auth
        requestBody:
          description: User info to register
          required: true
          content:
            application/json:
              schema:
                $ref: '#/definitions/User'
              examples:
                test_user:
                  summary: Registering a user
                  value:
                    username: "test_user"
                    email: "test_user@test.com"
                    password: "TestPassword123-"
        responses:
          200:
            description: Basic info of authenticated user with access token
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    data:
                      allOf:
                        - $ref: '#/definitions/User'
                        - type: object
                          properties:
                            token:
                              type: string
                              description: JWT token
                          example:
                            user_id: 1
                            username: "test_user"
                            email: "test_user@test.com"
                            token: "JWT-TOKEN"
        """
        return self.create()


class UserListView(UserViewBase):
    authentication = PyJwtAuthentication()
    authorization = StandardAuthorization()

    def get(self) -> Response:
        """
        Endpoint returning list of users
        JWT token must be sent via request Bearer Auth header to be authenticated and authorized to receive data.
        ---
        tags:
          - user
        security:
          - bearerAuth: []
        responses:
          200:
            description: List of users
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    data:
                      type: array
                      items:
                        $ref: '#/definitions/User'
        """
        return self.list()
