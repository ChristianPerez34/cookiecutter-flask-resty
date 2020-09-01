from flask_resty import Api

from api.users import UserListView, RegisterUserView, LoginUserView


def initialize_routes(api: Api):
    api.add_resource("/users/", UserListView)
    api.add_resource("/auth/register/", RegisterUserView)
    api.add_resource("/auth/login/", LoginUserView)
