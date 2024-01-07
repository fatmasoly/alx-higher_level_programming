#!/usr/bin/python3
"""
This module defines a function to print a given text
with specific indentation rules.
"""


def text_indentation(text):
    """
    This function prints a given text with specific indentation rules.

    Args:
        text (str): The text to be printed.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    space = False
    pr_sp = ""
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            if space:
                print(pr_sp, end="")
            pr_sp = ""
            print(text[i], end="")
            print()
            print()
            space = False
        elif text[i] != " ":
            if text[i] == "\n":
                space = False
            if space:
                print(pr_sp, end="")
            pr_sp = ""
            print(text[i], end="")
            space = True
        else:
            pr_sp += " "


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
