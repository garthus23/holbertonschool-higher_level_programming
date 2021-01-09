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

        expected = 12

        actual = max_integer([1, 3, 6, 12])
        self.assertEqual(actual, expected)

        actual = max_integer([12, 3, 6, 10])
        self.assertEqual(actual, expected)

        actual = max_integer([-1, 12, 3, 5])
        self.assertEqual(actual, expected)

        actual = max_integer([-1, -12, -3, -5])
        self.assertEqual(actual, -1)

        actual = max_integer([12])
        self.assertEqual(actual, expected)
