#!/usr/bin/python3
"""definition of a rectangle class"""


class Rectangle:
    """Rectangle class based on first task"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes height and width """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """func to retrieve the width

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """func to modify the width

        Args:
            value (int): new width to set

        Raises:
            TypeError: when value is not int
            ValueError: when value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """func to retrieve the height

        Returns:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """func to modify the height

        Args:
            value (int): new height to set

        Raises:
            TypeError: when value is not int
            ValueError: when value is  0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func to returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """func to returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints rectangle with #"""
        newStr = ""
        if self.__width == 0 or self.__height == 0:
            return newStr
        for i in range(self.height):
            newStr += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                newStr += "\n"
        return newStr

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle(" + str(self.__width) + ", "\
                            + str(self.__height) + ")"

    def __del__(self):
        """ deletion of instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() <= rect_2.area():
            return rect_2
        else:
            return rect_1
