#!/usr/bin/python3
"""Doc string for module level documentation"""

def write_file(filename="", text=""):
    """
    Function that writes a string to a text file in (UTF8) 
    and returns the number of characters written.

    Args:
    filename (string): name of file to write to
    text (string): text to be written into file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)