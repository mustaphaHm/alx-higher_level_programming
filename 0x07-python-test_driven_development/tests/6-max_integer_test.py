#!/usr/bin/python3
"""Implementing Unittests"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Function to test the max intger
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([1, -1]), 1)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 4, 9]), 9)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            max_integer(["a", 1])
            max_integer(1, [1, 2])
