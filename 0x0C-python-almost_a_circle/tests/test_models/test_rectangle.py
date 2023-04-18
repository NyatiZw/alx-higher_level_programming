#!/usr/bin/python3
""" Defines unittests for base class """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """ Unittesting for base class """

    def test_no_args(self):
        r1 = Ractangle()
        rb2 = Ractangle()
        self.assertEqual(r1.id, r2.id - 1)

    def test_none(self):
        r1 = Rectangle(None)
        r2 = Rectangle(None)
        self.assertEqual(r1.id, r2.id - 1)

    def test_public_id(self):
        r1 = Rectangle(7)
        r1.id = 1
        self.assertEqual(1, r1.id)

    def test_string_id(self):
        self.assertEqual("World", Rectangle("World").id)

    def test_range(self):
        self.assertEqual(range(5), Rectangle(range(5)).id)
