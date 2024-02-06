#!/usr/bin/python3
"""This module defines a text file reading function"""

def read_file(filename=""):
    """
    Function that reads a text file in (UTF8) and prints it to stdout

    Agrs:
        filename (string): name of the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")