#!/usr/bin/python3
"""Starts a Flask Web App"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """

    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """

    """
    return 'HBNB'


@app.route('/c/<text>')
def c_with_params(text):
    """

    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_with_text(text):
    """

    """
    text_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_no_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
