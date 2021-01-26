import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestsRectangle(unittest.TestCase):

    def test_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_all_args(self):
        r3 = Rectangle(10, 2, 4, 5, 6)
        self.assertEqual(r3.id, 6)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)

    def test_all_0(self):
        self.assertRaises(ValueError, Rectangle, 0, 0, 0, 0, 0)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)

    def test_str(self):

        self.assertRaises(TypeError, Rectangle, "10")
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, 10, 3, "4")
        self.assertRaises(TypeError, Rectangle, 10, 2, 3, "6")


    def test_below_0(self):
        self.assertRaises(TypeError, Rectangle, -10)
        self.assertRaises(ValueError, Rectangle, 10, -10)
        self.assertRaises(ValueError, Rectangle, 10, 10, -10)
        self.assertRaises(TypeError, Rectangle, 10, 10, 10, -10, 10, 10)
        self.assertRaises(TypeError, Rectangle, 10, 10, 10, 10, 10 , -10)


    def test_area(self):
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.area(), 20)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)
