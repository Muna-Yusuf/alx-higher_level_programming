#!/usr/bin/python3
"""Module for text_indentation mothod
function prints a text with 2 new lines after delim.
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines
        after each of these characters: [ ., ? and : ]
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
