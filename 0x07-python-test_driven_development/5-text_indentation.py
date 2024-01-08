#!/usr/bin/python3
"""
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']

    current_line = ""
    for char in text:
        current_line += char

        if char in punctuations:
            print(current_line.strip())
            print()
            current_line = ""

    # Print the remaining text, if any
    if current_line:
        print(current_line.strip())

        if __name__ == "__main__":
            import doctest
            doctest.testfile("tests/5-text_indentation.txt")
