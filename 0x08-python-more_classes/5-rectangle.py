#!/usr/bin/python3
"""Implementation of a rectangle class."""


class Rectangle:
    """A class that represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle object."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be non-negative.")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be non-negative.")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns a string representation of
        the rectangle that can be used to recreate the object."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when the rectangle object is deleted."""
        print("Bye rectangle...")
