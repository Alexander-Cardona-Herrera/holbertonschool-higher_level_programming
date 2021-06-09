#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def test_id(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)
if __name__ == '__main__':
    unittest.main()
