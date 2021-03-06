# cookiecutter-flask-resty
[![pyup](https://pyup.io/repos/github/pyupio/pyup/shield.svg)](https://pyup.io/account/repos/github/ChristianPerez34/cookiecutter-flask-resty/)
[![python3](https://pyup.io/repos/github/ChristianPerez34/cookiecutter-flask-resty/python-3-shield.svg)](https://pyup.io/account/repos/github/ChristianPerez34/cookiecutter-flask-resty/)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A Flask REST API template for [cookiecutter](https://github.com/audreyr/cookiecutter).


## Highlights
- Modern Python development with Python 3.8+
- PostgreSQL 12.4+
- [Flask-Resty Framework](https://github.com/4Catalyzer/flask-resty) integration
- Dependencies and security updates enforced by [pyup.io](https://pyup.io/).
- Flask-SQLAlchemy with basic User model
- JWT authentication scheme
- Flask-Bcrypt for password hashing
- Flask-Migrate for SQLAlchemy database migrations
- Flasgger swagger-UI API documentation
- Configuration using environment variables

## Quick Start

Install Cookiecutter globally:

```sh
$ pip install cookiecutter
```

Generate the boilerplate:

```sh
$ cookiecutter https://github.com/ChristianPerez34/cookiecutter-flask-resty.git
```
