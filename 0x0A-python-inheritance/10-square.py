#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
class BaseGeometry in module
===================================
"""


class Square(Rectangle):
    """Square class that inherited from Rectangle that inherited BaseGeometry"""

    def __init__(self, size):
        """Method for initialising the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
