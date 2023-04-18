#!/usr/bin/python3
""" Defines unittests for base class """
import os
import unittest
from models.base import Base


class TestBase_instantiation(unitttest.TestCase):
    """ Unittesting for base class """

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id -1)

    def test_public_id(self):
        b1 = Base(7)
        b1.id = 1
        self.assertEqual(15, b.id)
