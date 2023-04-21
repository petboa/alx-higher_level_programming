#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Creates a rectangle object
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with a given width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Returns the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle to a given value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle to a given value
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """Returns a string representation of the rectangle
        """
        if not self.perimeter:
            return ""
        return('\n'.join('#' * self.width for x in range(self.height)))

    def __repr__(self):
        """Returns a string representation of the
        rectangle that can be used to recreate it
        """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Deletes the rectangle object
        """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
