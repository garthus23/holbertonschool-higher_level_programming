import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestsRectangle(unittest.TestCase):

    def test_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)

