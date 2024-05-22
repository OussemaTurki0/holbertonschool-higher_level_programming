#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Function to print text with 2 new lines after ., ? and :.
    
    Args:
    text (str): The text to be printed.

    Raises:
    TypeError: If text is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
