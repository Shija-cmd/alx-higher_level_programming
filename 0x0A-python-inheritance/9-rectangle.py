#!/usr/bin/python3
"""
   a rectangle class inheriting other clases
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
   a class  that inheriting from BaseGeometry
    """
    def __init__(self, width, height):
        """
            Initialising rectangle from BaseGeometry
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        defines the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
            Rectangle with __str__
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
