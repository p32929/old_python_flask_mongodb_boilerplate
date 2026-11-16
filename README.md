# old_python_flask_mongodb_boilerplate

An older, simple starter for a Python 3 API with Flask and MongoDB. JWT login with a real logout, MongoEngine models and a Waitress production server are already set up, so you can start on your own routes right away.

> There is a newer version: [python_flask_blueprint_mongoenginemate_boilerplate](https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate) adds a module structure, Pydantic validation and a CRUD generator. This one is flatter and simpler, if that is what you want.

## What you get

1. **Flask**, with route handlers (controllers) kept apart from the logic (services).
2. **MongoEngine models** for `User` and `BlockedToken`, using mongoengine-mate.
3. **JWT login with a logout that really works:** logged-out tokens are saved as blocked, not just forgotten by the client.
4. **One response helper** (`utils/responder.py`), so every endpoint answers in the same JSON shape.
5. **Waitress** as the production server instead of Flask's development server.
6. **Docker and docker-compose** files.

## Project layout

```
waitress_server.py          starts the app in production
controllers/                route handlers
services/user_service.py    the logic behind them
db_models/                  User and BlockedToken
utils/responder.py          the same JSON response shape everywhere
utils/logger.py             logging setup
constants.py                settings read from the environment
```

## Get started

```bash
git clone https://github.com/p32929/old_python_flask_mongodb_boilerplate.git
cd old_python_flask_mongodb_boilerplate
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then fill it in
python waitress_server.py
```

Or run it with Docker:

```bash
docker-compose up
```

## Settings

Put these in `.env`:

| Key | What it is for | Default |
|---|---|---|
| `PORT` | The port to serve on | 8000 |
| `DATABASE_URL` | Your MongoDB connection string | none, you must set it |
| `PROD` | Set it to run in production mode | off |
| `JWT_SECRET` | The secret used to sign tokens | `SECRET`, change it |
| `TOKEN_VALIDITY` | How long a token lasts | 7 |
| `APP_NAME` | Shown in logs and responses | `APP` |

## Contributing

Contributions are very welcome. Please open an issue first to talk about what you'd like to add or change, so we can agree on it before you spend time on a pull request. Thank you!

## Share

<a href="https://p32929.github.io/share/?repo=old_python_flask_mongodb_boilerplate"><img src="https://p32929.github.io/readme/share.svg" alt="Share this with your friends in just a click" width="420"></a>

## Support

<a href="https://p32929.github.io/support/"><img src="https://p32929.github.io/readme/support.svg" alt="If you like my works and want to support me, feel free to support" width="420"></a>
