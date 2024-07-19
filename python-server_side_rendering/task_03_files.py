#!/usr/bin/python3

from flask import Flask, render_template, request, abort
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

    try:
        with open("items.json", 'r') as f:
            rows = json.load(f)
        for key, value in rows.items():
            items_list.extend(value)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        abort(500, description=f"Error loading items: {e}")

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    if not source:
        abort(400, description="Missing 'source' parameter")
    
    id = request.args.get('id')

    data = []
    try:
        if source == "json":
            data = load_json_data("products.json", id)
        elif source == "csv":
            data = load_csv_data("products.csv", id)
        else:
            abort(400, description="Invalid 'source' parameter")
    except (FileNotFoundError, ValueError) as e:
        abort(500, description=f"Error loading products: {e}")

    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, wanted_id=None):
    """ Load JSON data from file and returns as a list of dictionaries """

    if not Path(filename).is_file():
        raise FileNotFoundError(f"Data file '{filename}' missing")

    data = []
    try:
        with open(filename, 'r') as f:
            rows = json.load(f)

        for row in rows:
            key = str(row['id'])
            if wanted_id is None or key == wanted_id:
                data.append(row)

    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise ValueError(f"Unable to load data from file '{filename}'") from exc

    return data

def load_csv_data(filename, wanted_id=None):
    """ Load CSV data from file and returns as a list of dictionaries """

    if not Path(filename).is_file():
        raise FileNotFoundError(f"Data file '{filename}' missing")

    data = []
    try:
        with open(filename, 'r') as csvfile:
            for row in csv.DictReader(csvfile):
                if wanted_id is None or row['id'] == wanted_id:
                    data.append(row)
    except csv.Error as exc:
        raise ValueError(f"Unable to load data from file '{filename}'") from exc

    return data

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
