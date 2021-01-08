#!/usr/bin/python3


"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        define classe unittest
    """
    def test_max(self):
        """
            test the max
        """
        actual = max_integer([1, 3, 6, 12])
        expected = 12
        self.assertEqual(actual, expected)
