import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestsRectangle(unittest.TestCase):

    def test_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 7)

    def test_all_args(self):
        r3 = Rectangle(10, 2, 4, 5)
        self.assertEqual(r3.id, 4)

    def test_str(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")

    def test_below_0_width(self):
        self.assertRaises(ValueError, Rectangle, 10, -10)

    def test_below_0_height(self):
        self.assertRaises(ValueError, Rectangle, 10, 9, -2) 
