#!/usr/bin/python3
""" Test base """

import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    """Test of Base() for assigning automatically an ID """
    def testbase(self):
        b1 = Base(2)
        self.assertAlmostEqual(b1.id, 2)

    def testbaseNone(self):
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)