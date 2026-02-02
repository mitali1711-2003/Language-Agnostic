"""Application factory for Flask app."""
from pathlib import Path

from flask import Flask
from app.config import config


def create_app(config_name: str = "development") -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # Load .env from project root when present
    try:
        from dotenv import load_dotenv
        load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    except ImportError:
        pass

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Register blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app
