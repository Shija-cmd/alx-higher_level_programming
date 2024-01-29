#!/usr/bin/python3
"""Describes a class Rectangle"""


class Rectangle:
    """
    Class that describes properties of rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Make new instances of Rectangle.

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Properties setter for width of rectangle.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Properties setter for height of recyangle.

        Args:
            value (int): Height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
