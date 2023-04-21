#!/usr/bin/python3
""" Unit tests for model rectangle """

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """ unit testing rectangle model """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(5, 1), Base)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, 6, 7, 9)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 2, 0, 0, 1).__y)
