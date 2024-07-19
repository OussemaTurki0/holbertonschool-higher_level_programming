#!/usr/bin/python3
"""Basic flask application that renders a HTML template"""
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Read and and load items from json file to python dict
    with open('items.json') as f:
        data = json.load(f)
    # retrieve values of "items" key
    # assign empty list if 'items' not present
    items = data.get('items', [])

    # Put items into html template
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
