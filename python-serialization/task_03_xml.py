import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    
    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the output XML file.
    
    Returns:
    None
    """
 
def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.
    
    Parameters:
    filename (str): The name of the input XML file.
    
    Returns:
    dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        data = {}
        for item in root:
            data[item.tag] = item.text
        
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Sample Test
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    if deserialized_data:
        print("\nDeserialized Data:")
        print(deserialized_data)
