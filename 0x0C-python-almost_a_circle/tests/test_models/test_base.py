#!/usr/bin/python3
""" Defines unittests for base class """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase_instantiation(unittest.TestCase):
    """ Unittesting for base class """

    def test_no_args(self):
        _b1 = Base()
        _b2 = Base()
        self.assertEqual(_b1.id, _b2.id - 1)

    def test_none(self):
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


if __name__ == "__main__":
    unittest.main()
