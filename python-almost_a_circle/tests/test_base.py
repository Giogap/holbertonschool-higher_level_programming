#!/usr/bin/python3
""" Test base """

import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    """Test of Base() for assigning automatically an ID """
    def testBase(self):
        b1 = Base(2)
        self.assertAlmostEqual(b1.id, 2)

    def testBaseNone(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testBaseJsonStr(self):
        self.assertIsNotNone(Base.to_json_string)

    def testBaseJsonStrNone(self):
        test = Base.to_json_string(None)
        self.assertEqual(test, "[]")