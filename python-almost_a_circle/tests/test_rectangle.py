#!/usr/bin/python3
""" Test base """

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test of Rectangle()"""
    def testRectangle(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def TestRecStrW(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def TestRecStrH(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
