import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the CustomObject instance to a file using pickle.
        
        Parameters:
        filename (str): The name of the file where the object will be saved.
        
        Returns:
        None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject instance from a file using pickle.
        
        Parameters:
        filename (str): The name of the file containing the serialized object.
        
        Returns:
        CustomObject: The deserialized object instance.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"An error occurred during deserialization: {e}")
            return None

# Sample Test
if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    obj.serialize("object.pkl")

    new_obj = CustomObject.deserialize("object.pkl")
    if new_obj:
        print("\nDeserialized Object:")
        new_obj.display()
