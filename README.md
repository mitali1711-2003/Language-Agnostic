# Language Chatbot Application

A minimal Flask boilerplate with app factory, blueprints, and config profiles.

## Structure

```
language_chatbot/
├── app/
│   ├── __init__.py      # App factory (create_app)
│   ├── config.py        # Development / Testing / Production config
│   ├── main/            # Main blueprint
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       ├── base.html
│       └── index.html
├── .env.example
├── requirements.txt
├── run.py               # Dev server
├── wsgi.py              # Production (gunicorn etc.)
└── README.md
```

## Setup

1. Create a virtual environment and install dependencies:

   ```bash
   cd language_chatbot
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Copy environment template and set your values:

   ```bash
   cp .env.example .env
   ```

3. Run the development server:

   ```bash
   python run.py
   ```

   Or with the Flask CLI:

   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   flask run
   ```

Open http://localhost:5000. The `/health` endpoint returns `{"status": "ok"}` for checks.

## Adding blueprints

1. Create a package under `app/`, e.g. `app/auth/`.
2. Define a blueprint and routes in `app/auth/__init__.py` and `app/auth/routes.py`.
3. Register it in `app/__init__.py`:

   ```python
   from app.auth import auth_bp
   app.register_blueprint(auth_bp, url_prefix="/auth")
   ```

## Production

Set `FLASK_ENV=production` and use a WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

Set `SECRET_KEY` and `DATABASE_URL` (or other config) in the environment; do not commit `.env`.
