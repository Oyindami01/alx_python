"""
A script that starts a Flask Web application and also has
an additional route/path.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    modified_text = text.replace('_', ' ')
    return "C {}".format(modified_text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    modified_text = text.replace('_', ' ') if text else 'is cool'
    return "Python {}".format(modified_text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('number_template.html', number=n)

if __name__ == '__main':
    app.run(host='0.0.0.0', port=5000)
