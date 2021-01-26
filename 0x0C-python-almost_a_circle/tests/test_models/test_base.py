import unittest
from models.base import Base


class TestClass(unittest.TestCase):

    def test_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
