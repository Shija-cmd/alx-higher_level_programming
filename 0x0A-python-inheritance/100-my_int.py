#!/usr/bin/python3
"""
class MyInt that inheriting from int
"""


class MyInt(int):
    """
        class MyInt that inheriting from int
    """
    def __eq__(self, x):
        """Defines module eq"""
        return not super().__eq__(x)

    def __ne__(self, x):
        """Defines module not eq"""
        return not super().__ne__(x)
