import unittest
from models.base import Base


class TestClass(unittest.TestCase):

    def test_one_instance_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_two_instances_none(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_third_instance_int(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_fourth_instance_str(self):
        b4 = Base("a")
        self.assertEqual(b4.id, "a")
