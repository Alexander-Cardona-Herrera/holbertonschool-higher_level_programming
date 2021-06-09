#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

if __name__ == '__main__':
    unittest.main()
