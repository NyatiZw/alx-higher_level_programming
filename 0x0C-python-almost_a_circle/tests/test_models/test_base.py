#!/usr/bin/python3
""" Defines unittests for base class
Unittest classes:
    TestBase_instantiation - line 15 
"""


import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """ Unittesting for base class """
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_public_id(self):
        b1 = Base(7)
        b1.id = 1
        self.assertEqual(1, b1.id)

    def test_string_id(self):
        self.assertEqual("World", Base("World").id)

    def test_range(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_NaN(self):
        b1 = Base(?)
        b1.id = #
        self.assertEqual(#, b1).id)
