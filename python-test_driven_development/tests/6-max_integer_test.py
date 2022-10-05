#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):


    """ All unittest passed """

    """ Test for “max at the end” exists """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    """ Test for “max at the beginning” exists """
    def test_max_beginning(self):
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    """ Test for “max in the middle” exists """
    def test_max_middle(self):
        self.assertEqual(max_integer([2, 5, 3, 4]), 5)

    """ Test for “one negative number in the list” exists """
    def test_max_negative(self):
        self.assertEqual(max_integer([-2, 5, 3, 4]), 5)

    """ Test for “only negative numbers in the list” exists """
    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    """ Test for “list of one element” exists """
    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    """ Test for “list is empty” exists """
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
