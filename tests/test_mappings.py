"""
Unit tests for the CharacterMap class.
"""

import unittest
from siri_bhoovalaya.mappings import CharacterMap

class TestCharacterMap(unittest.TestCase):
    def setUp(self):
        self.char_map = CharacterMap()

    def test_devanagari_mapping(self):
        """Test Devanagari script mapping."""
        # Test valid mappings
        self.assertEqual(self.char_map.get_char(1, 'devanagari'), 'अ')
        self.assertEqual(self.char_map.get_char(2, 'devanagari'), 'आ')
        
        # Test invalid number
        self.assertIsNone(self.char_map.get_char(0, 'devanagari'))
        self.assertIsNone(self.char_map.get_char(65, 'devanagari'))

    def test_kannada_mapping(self):
        """Test Kannada script mapping."""
        # Test valid mappings
        self.assertEqual(self.char_map.get_char(1, 'kannada'), 'ಅ')
        self.assertEqual(self.char_map.get_char(2, 'kannada'), 'ಆ')
        
        # Test invalid number
        self.assertIsNone(self.char_map.get_char(0, 'kannada'))
        self.assertIsNone(self.char_map.get_char(65, 'kannada'))

    def test_sanskrit_mapping(self):
        """Test Sanskrit script mapping."""
        # Test valid mappings
        self.assertEqual(self.char_map.get_char(1, 'sanskrit'), 'अ')
        self.assertEqual(self.char_map.get_char(2, 'sanskrit'), 'आ')
        
        # Test invalid number
        self.assertIsNone(self.char_map.get_char(0, 'sanskrit'))
        self.assertIsNone(self.char_map.get_char(65, 'sanskrit'))

    def test_invalid_script(self):
        """Test handling of invalid script."""
        with self.assertRaises(ValueError):
            self.char_map.get_char(1, 'invalid_script')

    def test_reverse_mapping(self):
        """Test character to number mapping."""
        # Test valid characters
        self.assertEqual(self.char_map.get_number('अ', 'devanagari'), 1)
        self.assertEqual(self.char_map.get_number('ಅ', 'kannada'), 1)
        
        # Test invalid characters
        self.assertIsNone(self.char_map.get_number('invalid', 'devanagari'))

if __name__ == '__main__':
    unittest.main()
