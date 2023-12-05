#!/usr/bin/python3
"""Defines file-reading function."""


def write_file(filename="", text=""):
    """ reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
