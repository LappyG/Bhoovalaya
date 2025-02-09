"""
Unit tests for the BandhaPatterns class.
"""

import unittest
from siri_bhoovalaya.matrix import ChakraMatrix
from siri_bhoovalaya.patterns import BandhaPatterns

class TestBandhaPatterns(unittest.TestCase):
    def setUp(self):
        self.matrix = ChakraMatrix()
        self.patterns = BandhaPatterns(self.matrix)

    def test_chakra_bandha(self):
        """Test Chakra-Bandh pattern traversal."""
        start_pos = (0, 0)
        pattern = list(self.patterns.chakra_bandha(start_pos))
        
        # Test pattern properties
        self.assertGreater(len(pattern), 0)
        self.assertEqual(pattern[0], 1)  # Should start at position 1
        self.assertEqual(len(set(pattern)), len(pattern))  # No duplicates

    def test_navamaank_bandha(self):
        """Test Navamaank-Bandh pattern traversal."""
        start_pos = (0, 0)
        pattern = list(self.patterns.navamaank_bandha(start_pos))
        
        # Test pattern properties
        self.assertGreater(len(pattern), 0)
        self.assertEqual(pattern[0], 1)  # Should start at position 1
        self.assertEqual(len(set(pattern)), len(pattern))  # No duplicates

    def test_diagonal_bandha(self):
        """Test Diagonal-Bandh pattern traversal."""
        pattern = list(self.patterns.diagonal_bandha())
        
        # Test pattern properties
        self.assertGreater(len(pattern), 0)
        self.assertEqual(len(set(pattern)), len(pattern))  # No duplicates

    def test_invalid_start_positions(self):
        """Test handling of invalid start positions."""
        invalid_pos = (27, 27)
        pattern = list(self.patterns.chakra_bandha(invalid_pos))
        self.assertEqual(len(pattern), 0)

if __name__ == '__main__':
    unittest.main()
