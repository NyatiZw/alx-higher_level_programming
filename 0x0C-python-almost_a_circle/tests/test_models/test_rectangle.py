#!/usr/bin/python3
""" Defines unittests for base class """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """ Unittesting for base class """

    def rect_is_base(self):
        self.assertIsInstance(Rectangle(20, 5), Base)

    def test_no_args(self):
        _r1 = Ractangle()
        _r2 = Ractangle()
        self.assertEqual(_r1.id, _r2.id - 1)

    def test_none(self):
        _r1 = Rectangle(None)
        _r2 = Rectangle(None)
        self.assertEqual(_r1.id, _r2.id - 1)

    def test_public_id(self):
        _r1 = Rectangle(7)
        _r1.id = 1
        self.assertEqual(1, r1.id)

    def test_string_id(self):
        self.assertEqual("World", Rectangle("World").id)

    def test_range(self):
        self.assertEqual(range(5), Rectangle(range(5)).id)

if __name__ == "__main__":
    unittest.main()
