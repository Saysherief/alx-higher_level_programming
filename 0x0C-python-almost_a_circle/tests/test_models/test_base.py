#!/usr/bin/python3
"""Unittest for Base"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittests for base([..])"""

    def test_no_of_obj(self):
        """Test no of objects and id"""
        first = Base()
        second = Base()
        self.assertEqual(second.id - first.id, 1)

if __name__ == "__main__":
    unittest.main()
