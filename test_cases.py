#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
    # Valid test cases
    def test_valid_case(self):
        self.assertEqual(6, calc(2, 3))

    def test_valid_boundary_lower(self):
        self.assertEqual(2, calc(1, 2))

    def test_valid_boundary_upper(self):
        self.assertEqual(9990, calc(10, 999))

    def test_valid_string_input(self):
        self.assertEqual(150, calc('10', '15'))

    def test_invalid_string_input(self):
        self.assertEqual(-1, calc('10b', '15'))

    def test_invalid_non_numeric_A(self):
        self.assertEqual(-1, calc('a', 5))

    def test_invalid_non_numeric_B(self):
        self.assertEqual(-1, calc(5, 'b'))

    def test_invalid_non_numeric_both(self):
        self.assertEqual(-1, calc('hello', 'b'))

    def test_invalid_zero_A(self):
        self.assertEqual(-1, calc(0, 10))

    def test_invalid_negative_A(self):
        self.assertEqual(-1, calc(-1, 5))

    def test_invalid_A_equal_to_B(self):
        self.assertEqual(-1, calc(5, 5))

    def test_invalid_A_greater_than_B(self):
        self.assertEqual(-1, calc(8, 5))

    def test_invalid_B_greater_than_999(self):
        self.assertEqual(-1, calc(10, 1000))

    def test_invalid_floating_point(self):
        self.assertEqual(-1, calc(1.5, 2.5))
