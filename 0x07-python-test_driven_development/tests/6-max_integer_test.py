#!/usr/bin/python3
"""Unittest for the moule max_integer 
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for max_integer function."""

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        i = [1, 2, 3, 4, 5]
        result = max_integer(i)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with a list of non-integers and integers:
        should raise a TypeError exception"""
        i = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, i)

    def test_empty(self):
        """Test with an empty list: should return None"""
        i = []
        result = max_integer(i)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        i = [-4, -8, -2]
        result = max_integer(i)
        self.assertEqual(result, -2)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        i = [4, 4.5, 3]
        result = max_integer(i)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with a parameter that is not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        i = [54]
        result = max_integer(i)
        self.assertEqual(result, 54)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        i = [9, 9, 9, 9, 9]
        result = max_integer(i)
        self.assertEqual(result, 9)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        i = ["hello", "hi"]
        result = max_integer(i)
        self.assertEqual(result, "hello")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
