# old_python_flask_mongodb_boilerplate

An older Python 3 + Flask + MongoDB boilerplate — JWT auth with token blocklisting, MongoEngine models and a Waitress production server, already wired up.

> Superseded by [python_flask_blueprint_mongoenginemate_boilerplate](https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate), which adds a NestJS-style module structure, Pydantic validation and a CRUD generator. This one is flatter and simpler if that's what you want.

## What's included

- **Flask** with controllers split out from services
- **MongoEngine + mongoengine-mate** models (`User`, `BlockedToken`)
- **JWT auth** with logout that actually invalidates — blocked tokens are persisted, not just dropped client-side
- **A consistent response helper** (`utils/responder.py`) so endpoints don't each invent their own JSON shape
- **Waitress** as the production server, not the Flask dev server
- **Docker + docker-compose**, and a `.env.example` to copy

## Project layout

```
waitress_server.py          production entrypoint
controllers/                route handlers
services/user_service.py    business logic
db_models/                  User and BlockedToken
utils/responder.py          uniform JSON responses
utils/logger.py             logging setup
constants.py                config constants
```

## Getting started

```bash
git clone https://github.com/p32929/old_python_flask_mongodb_boilerplate.git
cd old_python_flask_mongodb_boilerplate

# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env     # then fill it in
python waitress_server.py
```

Or with Docker:

```bash
docker-compose up
```

## Configuration

`.env` keys, all required:

| Key | What it's for |
|---|---|
| `PORT` | Port to serve on |
| `DATABASE_URL` | MongoDB connection string |
| `PROD` | Production flag |
| `JWT_SECRET` | Signing secret for tokens |
| `TOKEN_VALIDITY` | Token lifetime |
| `APP_NAME` | Used in logs and responses |

## Contributing

Contributions are warmly welcomed and greatly appreciated! Whether it's a bug fix, new feature, or improvement, your input helps make this project better for everyone.

Before submitting a pull request, please:

1. Create an issue describing the feature or bug fix you'd like to work on
2. Wait for discussion and approval to ensure alignment with project goals
3. Fork the repository and create your feature branch
4. Submit your pull request with a clear description of changes

This approach helps avoid duplicate efforts and ensures smooth collaboration. Thank you for considering contributing!

## Share

Sharing this repository with your friends is just one click away from here

[![facebook](https://user-images.githubusercontent.com/6418354/179013321-ac1d1452-0689-493f-9066-940cf2302b6e.png)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![twitter](https://user-images.githubusercontent.com/6418354/179013351-7d8d6d1c-4ce2-46ab-bef8-4c4765a1b888.png)](https://twitter.com/intent/tweet?url=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![tumblr](https://user-images.githubusercontent.com/6418354/179013343-3111f55a-3b90-40c7-8487-9777348672b0.png)](https://www.tumblr.com/share?v=3&u=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![pocket](https://user-images.githubusercontent.com/6418354/179013334-b095c45f-becf-49f4-9ee1-5a731a9b1f85.png)](https://getpocket.com/save?url=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![pinterest](https://user-images.githubusercontent.com/6418354/179013331-44cd9206-11b1-4b65-becb-5863b61c828f.png)](https://pinterest.com/pin/create/button/?url=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![reddit](https://user-images.githubusercontent.com/6418354/179013338-7416ae3f-73ba-4522-86e1-1374d7082d22.png)](https://www.reddit.com/submit?url=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![linkedin](https://user-images.githubusercontent.com/6418354/179013327-ca7b7102-1da8-4b1c-858f-1a6e5f21bd70.png)](https://www.linkedin.com/shareArticle?mini=true&url=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
[![whatsapp](https://user-images.githubusercontent.com/6418354/179013353-f477fa0b-3e6f-4138-a357-c9991b23ff88.png)](https://api.whatsapp.com/send?text=https://github.com/p32929/old_python_flask_mongodb_boilerplate/)
