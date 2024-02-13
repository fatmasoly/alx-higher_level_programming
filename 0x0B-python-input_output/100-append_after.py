#!/usr/bin/python3
"""
This module for function that inserts a line of text to
a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Parameters:
    - filename (str): The name of the file to be modified.
    - search_string (str): The specific string to
    search for in each line.
    - new_string (str): The line of text to be inserted
    after lines containing the search string.

    Returns:
    None
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
