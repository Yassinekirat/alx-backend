#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config():
    """Basic Babel setup"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """locale from request: best language match"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Basic Babel setup"""
    locale = get_locale()
    return render_template('3-index.html', locale=locale)


if __name__ == '__main__':
    app.run(debug=True)
