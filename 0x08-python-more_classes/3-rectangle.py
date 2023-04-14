#!/usr/bin/python3
"""Module 2-rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join("#" * self.__width for i in range(self.__height))

    def print(self):
        """Prints the rectangle"""

        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            print("\n".join("#" * self.__width for i in range(self.__height)))
