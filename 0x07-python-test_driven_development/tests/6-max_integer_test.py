#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])"""

    def test_assending_list(self):
        """Test assending ordered integer list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_dessending_list(self):
        """Test dessending ordered integer list"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_in_mid(self):
        """Test max in the middle of integer list"""
        self.assertEqual(max_integer([3, 1, 5, 2, 4]), 5)
        
    def test_max_1neg(self):
        """Test max when 1 -ve integer in list"""
        self.assertEqual(max_integer([5, 6, 5, -6, 1]), 6)
    def test_max_in_all_neg(self):
        """Test max when all are -ve integer list"""
        self.assertEqual(max_integer([-5, -6, -5, -6, -1]), -1)
    
    def test_max_single(self):
        """Test max when 1 element exists in a list"""
        self.assertEqual(max_integer([-1]), -1)

    def test_max_empty(self):
        """Test max when no element in the list"""
        self.assertEqual(max_integer([]), None)
