#!/usr/bin/python3
"""Unittest for the max_integer module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer function."""

    def test_regular(self):
        """Test the normal case"""
        my_list = [1, 2, 3, 4, 5]
        result = max_integer(my_list)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test if the list is non-ints and ints:
        if it's non-int than TypeError exception appears"""
        my_list = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, my_list)

    def test_empty(self):
        """Test the empty list: should return None"""
        my_list = []
        result = max_integer(my_list)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test if the list contains negative values:
            should return the max"""
        my_list = [-2, -6, -1]
        result = max_integer(my_list)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test if the list contains mixed ints and floats:
            should return the max"""
        my_list = [3, 4.5, 2]
        result = max_integer(my_list)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test if the parameter isn't a list:
            a TypeError must appear"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test if the list contains one int:
            should return the value of this int"""
        my_list = [45]
        result = max_integer(my_list)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test if the list contains identical values:
            should return the value"""
        my_list = [8, 8, 8, 8, 8]
        result = max_integer(my_list)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test if the list contains strings:
            should return the first string"""
        my_list = ["hi", "hello"]
        result = max_integer(my_list)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test None as parameter:
            TypeError must appear"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':

    unittest.main()
