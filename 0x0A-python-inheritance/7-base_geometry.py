#!/usr/bin/python3
"""
    Class BaseGeometry
"""


class BaseGeometry():
    """
        Class BaseGeometry
    """
    def area(self):
        """
            public instance
            Raise:
                Exception: Area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validators that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
