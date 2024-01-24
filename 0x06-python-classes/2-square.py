#!/usr/bin/python3
"""Describes the class square"""


class Square:
    """
    Class that describes the properties of the square
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
