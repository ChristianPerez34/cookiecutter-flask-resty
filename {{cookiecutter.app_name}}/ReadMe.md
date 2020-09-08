# {{ cookiecutter.app_name }}

{{ cookiecutter.app_short_description}}

## Getting Started

### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```

> **Note**: each time the database models change repeat the migrate and upgrade commands.

### Running the app

Must populate the .env.* file with the environment variables you need and set the app settings the application will run on. By default the application will run using development settings.

```bash
export APP_SETTINGS=settings.DevelopmentConfig
```

> **Note**: Use **settings.TestingConfig** when running tests and **settings.ProductionConfig** when deploying the application.

