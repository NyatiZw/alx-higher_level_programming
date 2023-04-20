#!/usr/bin/python3
""" Defines unittests for base class
Unittest classes:
    TestRectangle_instantiation - line 16 
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """ Unittesting for base class """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(20, 5), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_two_args(self):
        r1 = Rectangle(20, 5)
        r2 = Rectangle(3, 17)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(7, 5, 3)
        r2 = Rectangle(5, 2, 9)
        self.assertEqual(r1.id, r2.id - 1)

    def test_string_id(self):
        self.assertEqual("World", Rectangle("World").id)

    def test_range(self):
        self.assertEqual(range(5), Rectangle(range(5)).id)

if __name__ == "__main__":
    unittest.main()
