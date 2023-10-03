#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle

    Attribute
    ---------
    width: int
    height: int
    """

    @property
    def width(self):
        """
        Getter

        Return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value: sets to the width if it is an int and is
            greater or equal to 0

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value: sets to the height if it is an int and is
            greater or equal to 0

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """
        Initializer
        """

        self.width = width
        self.height = height

    def area(self):
        """
        Method
        Returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method
        Returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string += "#"
                if i != self.height - 1:
                    string += "\n"
            return string
