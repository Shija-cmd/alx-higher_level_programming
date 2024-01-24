#!/usr/bin/python3
""" class Square that defines a square by: (based on 2-square.py) """
Square = __import__('3-square').Square

""" Describe instance my_square_1 """
my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

""" Private instance attribute: size """
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

""" Describe instance my_square_2 """ 
my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
