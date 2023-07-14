#!/usr/bin/python3
"""Definition of class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """classe Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        # Calling the class base contructor
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters
    @property
    def width(self):
        """Get the width"""
        return self.__width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @property
    def y(self):
        """Get y"""
        return self.__y

    # Setters
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Public methods
    def area(self):
        """ return the area value of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout rectangle instance with char #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Overrinding str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            )

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribut by order"""
        if args:
            lenghtARgs = len(args)
            self.id = args[0] if lenghtARgs >= 1 else self.id
            self.__width = args[1] if lenghtARgs >= 2 else self.__width
            self.__height = args[2] if lenghtARgs >= 3 else self.__height
            self.__x = args[3] if lenghtARgs >= 4 else self.__x
            self.__y = args[4] if lenghtARgs >= 5 else self.__y
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value

    def to_dictionary(self):
        """return the dictionary representation of a rectangle"""
        i = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return {"x": x, "y": y, 'id': i, 'height': h, 'width': w}
