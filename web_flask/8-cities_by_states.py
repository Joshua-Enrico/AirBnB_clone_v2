#!/usr/bin/python3
"""Simple Flask app, with additional route"""
from flask import Flask, abort, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ returns a message"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """new path"""
    return ("HBNB")


@app.route('/c/<text>')
def c(text):
    """ display C with value in variable text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """ display python with value of text variable"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def numb(n):
    """ display value of n var if it is int"""
    return '{:d} is number'.format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """ display template n var if it is int """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """ return template if n is int and check odd|even"""
    if (n % 2 == 0):
        var = 'even'
    else:
        var = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, var=var)


@app.route('/states_list')
def run_all_states():
    """Run all states"""
    l_list = storage.all('State')
    return render_template('7-states_list.html', l_list=l_list)


@app.route('/cities_by_states')
def run_all_states_and_cities():
    """All states and cities"""
    l_list = storage.all('State')
    return render_template('8-cities_by_states.html', l_list=l_list)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
