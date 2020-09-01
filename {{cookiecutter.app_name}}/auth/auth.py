from flask_resty import (
    JwtAuthentication,
    HasCredentialsAuthorizationBase,
    AuthorizeModifyMixin,
)


class PyJwtAuthentication(JwtAuthentication):
    credentials_arg = "token"


class StandardAuthorization(HasCredentialsAuthorizationBase, AuthorizeModifyMixin):
    def filter_query(self, query, view):
        return query
