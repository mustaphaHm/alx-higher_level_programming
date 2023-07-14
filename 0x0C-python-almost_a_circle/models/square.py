#!/usr/bin/python3
"""Definition of class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructur"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )

    @property
    def size(self):
        """Get the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribut by order"""
        if args:
            lenghtARgs = len(args)
            self.id = args[0] if lenghtARgs >= 1 else self.id
            self.width = args[1] if lenghtARgs >= 2 else self.width
            self.height = args[1] if lenghtARgs >= 2 else self.height
            self.x = args[2] if lenghtARgs >= 3 else self.x
            self.y = args[3] if lenghtARgs >= 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dictionary representation of a square"""
        i = self.id
        w = self.width
        x = self.x
        y = self.y
        return {'id': i, 'x': x, 'size': w, 'y': y}
