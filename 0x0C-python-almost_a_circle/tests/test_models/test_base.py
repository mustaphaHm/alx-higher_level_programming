#!/usr/bin/python3
""" unit test for base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """definition of classe TestBase"""

    def test_base_continuous(self):
        """Test id is continuous with Args"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
