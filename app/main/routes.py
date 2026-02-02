"""Main blueprint routes."""
from flask import render_template
from app.main import main_bp


@main_bp.route("/")
def index():
    """Home page."""
    return render_template("index.html")


@main_bp.route("/bot")
def bot():
    """Home page."""
    return render_template("pages/bot.html")
