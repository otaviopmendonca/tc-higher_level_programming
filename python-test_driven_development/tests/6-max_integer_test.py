#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative), -1)

    def test_mixed_numbers(self):
        """Test a list of mixed positive and negative numbers."""
        mixed = [-1, 2, -3, 4]
        self.assertEqual(max_integer(mixed), 4)

    def test_float_numbers(self):
        """Test a list of floating point numbers."""
        floats = [1.5, 2.7, 3.3, 4.9]
        self.assertEqual(max_integer(floats), 4.9)

    def test_duplicate_max(self):
        """Test a list with duplicate max values."""
        duplicates = [1, 4, 2, 4, 3]
        self.assertEqual(max_integer(duplicates), 4)

    def test_string_in_list(self):
        """Test a list containing a string."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])

    def test_none_as_argument(self):
        """Test passing None as argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_arguments(self):
        """Test calling function with no arguments."""
        self.assertEqual(max_integer(), None)
