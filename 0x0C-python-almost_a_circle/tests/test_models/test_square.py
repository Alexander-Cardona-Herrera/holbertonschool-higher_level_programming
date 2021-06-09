#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    
    def test_id(self):
        r1 = Square(10, 2, 0, 12)
        self.assertEqual(r1.id, 12)

        r1 = Square(10)
        self.assertEqual(r1.id, 3)


if __name__ == '__main__':
    unittest.main()