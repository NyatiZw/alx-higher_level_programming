#!/usr/bin/python3
""" Unit tests for model rectangle """

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """ unit testing rectangle model """

    def test_rect_base(self):
        self.assertIsInstance(Rectangle(5, 1), Base)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, 6, 7, 9)

    def test_w_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__width)

    def test_h_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__y)

    def test_w_getter(self):
        r = Rectangle(3, 8, 5, 9, 1)
        self.assertEqual(3, r.width)

    def test_h_getter(self):
        r = Rectangle(6, 2, 1, 8, 5)
        self.assertEqual(2, r.height)

    def test_x_setter(self):
        r = Rectangle(9, 1, 5, 9, 2)
        r.x = 15
        self.assertEqual(15, r.x)

    def test_y_setter(self):
        r = Rectangle(4, 2, 6, 8, 1)
        r.y = 5
        self.assertEqual(5, r.y)

if __name__ == "__main__":
    unittest.main()
