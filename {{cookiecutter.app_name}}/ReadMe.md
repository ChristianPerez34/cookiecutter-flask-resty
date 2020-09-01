# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description}}

## Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```

> **Note**: each time the database models change repeat the migrate and upgrade commands.