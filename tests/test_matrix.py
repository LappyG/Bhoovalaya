"""
Unit tests for the ChakraMatrix class.
"""

import unittest
import numpy as np
from siri_bhoovalaya.matrix import ChakraMatrix

class TestChakraMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = ChakraMatrix()

    def test_initialization(self):
        """Test if matrix is initialized correctly."""
        self.assertEqual(self.matrix.size, 27)
        self.assertEqual(self.matrix.get_value(0, 0), 1)
        self.assertEqual(self.matrix.get_value(2, 1), 64)

    def test_invalid_positions(self):
        """Test handling of invalid matrix positions."""
        with self.assertRaises(ValueError):
            self.matrix.get_value(-1, 0)
        with self.assertRaises(ValueError):
            self.matrix.get_value(27, 0)
        with self.assertRaises(ValueError):
            self.matrix.set_value(0, -1, 1)

    def test_quadrant_operations(self):
        """Test quadrant retrieval and rotation."""
        # Test quadrant retrieval
        q1 = self.matrix.get_quadrant(1)
        self.assertEqual(q1.shape, (13, 13))
        
        # Test quadrant rotation
        self.matrix.rotate_quadrant(1, clockwise=True)
        self.matrix.rotate_quadrant(1, clockwise=False)
        
        with self.assertRaises(ValueError):
            self.matrix.get_quadrant(5)

    def test_diagonal_operations(self):
        """Test diagonal operations."""
        primary_diagonal = self.matrix.get_diagonal(primary=True)
        secondary_diagonal = self.matrix.get_diagonal(primary=False)
        
        self.assertEqual(len(primary_diagonal), 27)
        self.assertEqual(len(secondary_diagonal), 27)

if __name__ == '__main__':
    unittest.main()
