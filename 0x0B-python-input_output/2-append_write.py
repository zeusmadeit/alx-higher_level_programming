#!/usr/bin/python3
"""Module level documentation for append_write"""

def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8) 
    and returns the number of characters added

    Args:
    filename (string): name of file to be appended
    text (string): text to be appended to file

    Returns: number of characters written to file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)