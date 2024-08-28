#!/usr/bin/env python3
"""Welcome to Holberton"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """config class for languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def hello() -> str:
    """root route"""
    return render_template('5-index.html')


def get_user():
    """A function to get user"""
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        return user
    return None


@app.before_request
def before_request() -> None:
    """A function to be called before the rest."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """determine the locale of the user"""
    # Locale from URL parameters
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    # Local from user settings
    locale = g.user.locale
    if locale in app.config["LANGUAGES"]:
        return locale

    # Locale from request headers

    return request.accept_languages.best_match(
            app.config["LANGUAGES"]
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
