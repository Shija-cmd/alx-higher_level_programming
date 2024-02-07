#!/usr/bin/python3
"""
    a quare class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
      a  square Class inheriting other class
    """
    def __init__(self, size):
        """
            Initialising the square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        defines area
        """
        return self.__size ** 2

    def __str__(self):
        """
            Use of __str__
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
