#!/usr/bin/python3
""" Unit testing for model square """

import unittest
from models.square import Square
from models.base import Base


class TestSquare_instantiation(unittest.TestCase):
    """ Unit testing the instantiation of the class square """

    def test_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_rect(self):
        self.assertIsInstance(Square(5), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_four_args(self):
        self.assertEqual(7, Square(5, 3, 5, 7).id)

if __name__ == "__main__":
    unittest.main()
