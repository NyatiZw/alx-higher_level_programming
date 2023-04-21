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
        _b1 = Base()
        _b2 = Base()
        self.assertEqual(_b1.id, _b2.id - 1)

    def test_none_id(self):
        _b1 = Base(None)
        _b2 = Base(None)
        self.assertEqual(_b1.id, _b2.id - 1)

    def test_public_id(self):
        _b1 = Base(7)
        _b1.id = 1
        self.assertEqual(1, _b1.id)

    def test_string_id(self):
        self.assertEqual("World", Base("World").id)

    def test_range(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_NaN(self):
        _b1 = Base()
        _b1.id = "#"
        self.assertEqual("#", _b1.id)
