import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestsRectangle(unittest.TestCase):

    def test_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)

    def test_str(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")

    def test_below_0(self):
        self.assertRaises(ValueError, Rectangle, 10, -10)
