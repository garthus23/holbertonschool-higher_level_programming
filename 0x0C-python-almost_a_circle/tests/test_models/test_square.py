import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestsRectangle(unittest.TestCase):

    def test_int(self):
        s1 = Square(10, 2)
        self.assertEqual(s1.id, 8)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)




    def test_all_args(self):
        s3 = Square(10, 2, 4, 5)
        self.assertEqual(s3.id, 5)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 4)

    def test_all_0(self):
        self.assertRaises(ValueError, Square, 0, 0, 0, 0)
        self.assertRaises(TypeError, Square)

    def test_one_arg(self):
        s3 = Square(9)
        self.assertEqual(s3.size, 9)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)
        self.assertEqual(s3.id, 9)
"""
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

    def test_str(self):
        r4 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r4.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        r4.update(3)
        self.assertEqual(r4.__str__(), "[Rectangle] (3) 1/1 - 1/1")

"""
