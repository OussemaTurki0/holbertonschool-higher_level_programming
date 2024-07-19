#!/usr/bin/python3

from flask import Flask, render_template, request
from pathlib import Path
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    items_list = []

    with open("items.json", 'r') as f:
        rows = json.load(f)
    for key,value in rows.items():
        items_list = value

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    data = []
    if source == "json":
        data = load_json_data("products.json", id)
    elif source == "csv":
        data = load_csv_data("products.csv", id)

    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, wanted_id = None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)

        for row in rows:
            # Typecast!!!!!!!
            key = str(row['id'])

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                product = {}
                for k,v in row.items():
                    product[k] = v
                data.append(product)

    except ValueError as exc:
        raise ValueError("Unable to load data from file '{}'".format(filename)) from exc

    return data

def load_csv_data(filename, wanted_id = None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r') as csvfile:
            # using DictReader method to convert each row to a dictionary
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except ValueError as exc:
        raise ValueError("Unable to load data from file '{}'".format(filename)) from exc

    return data

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)