import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to a JSON file.
    
    Parameters:
    csv_filename (str): The name of the input CSV file.
    
    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Sample Test
if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
