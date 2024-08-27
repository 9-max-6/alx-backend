#!/usr/bin/env python3
"""Welcome to Holberton"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route("/")
def hello():
    return render_template('1-index.html')

@babel.localeselector
def get_locale():
    """determine the locale of the user"""
    return request.accept_languages.best_match(
        Config.LANGUAGES
    )


if __name__ == "__main__":
    app.run()
