#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """an empty class BaseGeometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a paramete as an integer.

        Args:
            name :
            value :
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
