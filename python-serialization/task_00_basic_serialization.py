import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    
    Parameters:
    data (dict): The Python dictionary to serialize.
    filename (str): The name of the file where the JSON data will be saved.
    
    Returns:
    None
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.
    
    Parameters:
    filename (str): The name of the file containing JSON data.
    
    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

# Execution Output Example
if __name__ == "__main__":
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    deserialized_data = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized_data)
