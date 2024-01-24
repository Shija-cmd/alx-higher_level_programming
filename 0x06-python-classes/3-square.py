#!/usr/bin/python3
class Square:
    """Describes the Square"""
    def __init__(self, size=0):
        """Starting the data"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns square area"""
        return self.__size**2
