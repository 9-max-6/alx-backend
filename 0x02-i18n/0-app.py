#!/usr/bin/env python3
"""Welcome to Holberton"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """A function to render template"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
