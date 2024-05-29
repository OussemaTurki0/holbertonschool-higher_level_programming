#!/usr/bin/python3
"""
This script defines a function to convert JSON strings to Python objects.

The function `from_json_string` takes a JSON string as input and returns
the corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
    Returns:
        Any: The Python object corresponding to the JSON string.
    """
    return json.loads(my_str)
