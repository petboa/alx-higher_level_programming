#!/usr/bin/python3
"""Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_docstring(self):  
        # Check if documentation exists
        self.assertIsNotNone(max_integer.__doc__)

    def test_simple(self):
        # Test the function with simple integer inputs
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-5, -3, 0, 3, 5]), 5)
        self.assertEqual(max_integer([69, 6, 9]), 69)
        self.assertEqual(max_integer([69, 99, 9]), 99)
        self.assertEqual(max_integer([69]), 69)

    def test_empty(self):
        # Test the function with an empty input list and None
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        # Test the function with string inputs
        self.assertEqual(max_integer(["a", "z"]), "z")

    def test_neg_float(self):
        # Test the function with negative float inputs
        self.assertEqual(max_integer([-5.55, -66.66, -111.1]), -5.55)

    def test_diff_datatypes(self):
        # Test the function with different data types
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

    def test_list_list(self):
        # Test the function with nested list inputs
        self.assertEqual(max_integer([[1, 2], [2, 1]]), [2, 1])


if __name__ == "__main__":
    unittest.main()
