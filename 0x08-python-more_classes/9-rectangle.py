#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """A class used to represent a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a rectangle object"""
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """Creates a square"""
        return cls(size, size)

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self._width

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self._height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self._height * self._width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._height == 0 or self._width == 0:
            return 0
        return (self._height * 2) + (self._width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the bigger one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Modifies string representation of the object"""
        if not self.perimeter:
            return ""
        return('\n'.join("{}".format(
            self.print_symbol) * self._width for x in range(self._height)))

    def __repr__(self):
        """Modifies the representation of the object"""
        return("Rectangle({}, {})".format(self._width, self._height))

    def __del__(self):
        """Modifies deletion of the object"""
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
