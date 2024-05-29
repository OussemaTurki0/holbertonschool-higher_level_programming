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
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

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
    