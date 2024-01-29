#!/usr/bin/python3
class Square:
    """Describes a square"""
    def __init__(self, size=0):
        """Initialise data"""
        self.size = size

    def area(self):
        """Returns square area"""
        return self.__size**2

    @property
    def size(self):
        """Getters method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setters method"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
