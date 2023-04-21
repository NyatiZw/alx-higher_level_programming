#!/usr/bin/python3
""" Defines unittests for base class
Unittest classes:
    TestBase_instantiation - line 15 
"""

from models.rectangle import Rectangle
import unittest
from models.base import Base
import os
from models.square import Square


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
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_bytes_id(self):
        self.assertEqual('Hello', Base('Hello').id)

    def test_tuple_id(self):
        self.assertEqual((4, 6), Base((4, 6)).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(4, 5)

class TestBase_to_json_string(unittest.TestCase):
    """Testing to_json_string"""

    def test_to_json_string_rectangle(self):
        r = Rectangle(10, 6, 3, 5, 8)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_type(self):
        s = Square(10, 6, 3, 5)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]",Base.to_json_string([]))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

class TestBase_save_to_file(unittest.TestCase):
    """ Testing save_to_file method"""

    def test_save_to_file_no_agrs(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
