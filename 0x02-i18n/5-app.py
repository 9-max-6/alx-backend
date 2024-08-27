#!/usr/bin/env python3
"""Welcome to Holberton"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """config class for languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def hello() -> str:
    return render_template('1-index.html')


@babel.localeselector
def get_locale() -> str:
    """determine the locale of the user"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(
            app.config["LANGUAGES"]
        )


if __name__ == "__main__":
    app.run()
