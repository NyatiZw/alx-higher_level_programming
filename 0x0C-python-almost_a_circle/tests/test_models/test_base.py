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

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as fp:
            self.assertEqual("[]", fp.read())

    def test_save_many_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

class TestBase_from_json_string(unittest.TestCase):
    """ testing from_json_string method"""

    def test_from_json_string(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_none(self):
        self.assertEqual('[]', Base.from_json_string(None))

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

class TestBase_create(unittest.TestCase):
    """ Testing create method """

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (5) 1/3 - 3/5", str(r1))

    def test_create_rectangle_(self):
        r1 =  Rectangle(4, 7, 8, 4, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
