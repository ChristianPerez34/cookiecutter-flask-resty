import os

print(os.getcwd())
if "{{cookiecutter.deployment}}" == "heroku":
    file_path = 'Procfile'
    if not os.path.exists(file_path):
        with open(file_path, "w") as procfile:
            procfile.write('web: gunicorn "app:create_app()"')