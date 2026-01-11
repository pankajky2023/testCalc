
"""
Test cases for the Calculator module.

This module contains unit tests for all calculator operations
using the unittest framework.
"""

import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(0, 5), 5)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
    
    def test_add_floats(self):
        """Test addition of floating point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.7), 4.2, places=1)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=1)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 15), 5)
        self.assertEqual(self.calc.subtract(5, 5), 0)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(7, 1), 7)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(0, -5), 0)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(-5, 0)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
        self.assertEqual(self.calc.power(1, 100), 1)
    
    def test_power_negative_base(self):
        """Test power operation with negative base."""
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(-1, 2), 1)
    
    def test_power_negative_exponent(self):
        """Test power operation with negative exponent."""
        self.assertEqual(self.calc.power(2, -2), 0.25)
        self.assertEqual(self.calc.power(5, -1), 0.2)
    
    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers."""
        self.assertEqual(self.calc.square_root(4), 2.0)
        self.assertEqual(self.calc.square_root(9), 3.0)
        self.assertEqual(self.calc.square_root(16), 4.0)
        self.assertEqual(self.calc.square_root(0), 0.0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.414213, places=5)
    
    def test_square_root_negative_number(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        result = self.calc.add(999999999, 1)
        self.assertEqual(result, 1000000000)
        
        result = self.calc.multiply(1000000, 1000000)
        self.assertEqual(result, 1000000000000)
    
    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        result = self.calc.add(0.000001, 0.000002)
        self.assertAlmostEqual(result, 0.000003, places=6)
    
    def test_infinity_handling(self):
        """Test behavior with very large results."""
        # This might produce infinity in some cases
        result = self.calc.power(10, 308)  # Close to float limit
        self.assertTrue(isinstance(result, float))


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
