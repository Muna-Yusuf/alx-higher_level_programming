#!/usr/bin/python3
"""defines class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ the size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            for counts, arg in enumerate(args):
                if counts == 0:
                    self.id = arg
                elif counts == 1:
                    self.size = arg
                elif counts == 2:
                    self.x = arg
                elif counts == 3:
                    self.y = arg
                else:
                    continue

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "x": self.x,
                "size": self.width, "y": self.y}
