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

## You might also like

<p><a href="https://openstore.pfay.workers.dev/cards/p32929/0?n=4&amp;repo=old_python_flask_mongodb_boilerplate"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/cards/p32929/0.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=dark"><img src="https://openstore.pfay.workers.dev/cards/p32929/0.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=light" width="50%" align="top" alt="More apps by p32929 on OpenStore (1)"></picture></a><a href="https://openstore.pfay.workers.dev/cards/p32929/1?n=4&amp;repo=old_python_flask_mongodb_boilerplate"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/cards/p32929/1.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=dark"><img src="https://openstore.pfay.workers.dev/cards/p32929/1.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=light" width="50%" align="top" alt="More apps by p32929 on OpenStore (2)"></picture></a><br><a href="https://openstore.pfay.workers.dev/cards/p32929/2?n=4&amp;repo=old_python_flask_mongodb_boilerplate"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/cards/p32929/2.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=dark"><img src="https://openstore.pfay.workers.dev/cards/p32929/2.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=light" width="50%" align="top" alt="More apps by p32929 on OpenStore (3)"></picture></a><a href="https://openstore.pfay.workers.dev/cards/p32929/3?n=4&amp;repo=old_python_flask_mongodb_boilerplate"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/cards/p32929/3.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=dark"><img src="https://openstore.pfay.workers.dev/cards/p32929/3.svg?n=4&amp;repo=old_python_flask_mongodb_boilerplate&amp;theme=light" width="50%" align="top" alt="More apps by p32929 on OpenStore (4)"></picture></a></p>

<p><a href="https://p32929.github.io/share/?repo=old_python_flask_mongodb_boilerplate"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-share-dark.svg"><img src="https://p32929.github.io/readme/footer-share-light.svg" width="50%" align="top" alt="Share this project with your friends in one click"></picture></a><a href="https://p32929.github.io/support/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-support-dark.svg"><img src="https://p32929.github.io/readme/footer-support-light.svg" width="50%" align="top" alt="If you like my work and want to support me, feel free to support"></picture></a><br><a href="https://openstore.pfay.workers.dev/add"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-join-dark.svg"><img src="https://p32929.github.io/readme/footer-join-light.svg" width="100%" align="top" alt="Put your own apps on OpenStore: free, your listing lives in your own repo"></picture></a></p>
