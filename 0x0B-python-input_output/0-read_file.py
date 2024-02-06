#!/usr/bin/python3

def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Agrs:
        filename (string): name of the file to read
    """
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line)