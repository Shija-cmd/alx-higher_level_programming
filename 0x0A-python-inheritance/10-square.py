#!/usr/bin/python3
"""
   a square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
      a Square Class inheriting other class
    """
    def __init__(self, size):
        """
            Initializing the square
        """
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """
        defines area
        """
        return self.__size ** 2

    def __str__(self):
        """
            Usage of __str__
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
