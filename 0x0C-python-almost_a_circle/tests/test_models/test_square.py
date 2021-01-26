import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestsRectangle(unittest.TestCase):

    def test_int(self):
        s1 = Square(10, 2)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)




    def test_all_args(self):
        s3 = Square(10, 2, 4, "a")
        self.assertEqual(s3.id, "a")
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
        self.assertEqual(s3.id, 13)

    def test_str(self):
        self.assertRaises(TypeError, Square, "10")
        self.assertRaises(TypeError, Square, 10, "2")
        self.assertRaises(TypeError, Square, 10, 3, "4")


    def test_below_0(self):
        self.assertRaises(ValueError, Square, -10)
        self.assertRaises(ValueError, Square, 10, -10)
        self.assertRaises(ValueError, Square, 10, 10, -10)
        self.assertRaises(TypeError, Square, 10, 10, 10, -10, 10, 10)
        self.assertRaises(TypeError, Square, 10, 10, 10, 10, 10 , -10)


    def test_area(self):
        s2 = Square(10, 2)
        self.assertEqual(s2.area(), 100)
        s2 = Square(8, 7, 0, 12)
        self.assertEqual(s2.area(), 64)

    def test_str(self):
        s4 = Square(1, 1, 1, 1)
        self.assertEqual(s4.__str__(), "[Square] (1) 1/1 - 1")
        s4.update(5)
        self.assertEqual(s4.__str__(), "[Square] (5) 1/1 - 1")


