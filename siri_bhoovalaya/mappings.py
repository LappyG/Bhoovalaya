"""
Character mapping module for Siri Bhoovalaya decryption.
Handles character substitution for Indian languages.
"""

from typing import Dict, Optional

class CharacterMap:
    def __init__(self):
        """Initialize character mappings for different scripts."""
        self.devanagari_map = self._init_devanagari_map()
        self.kannada_map = self._init_kannada_map()
        self.sanskrit_map = self._init_sanskrit_map()

    def _init_devanagari_map(self) -> Dict[int, str]:
        """Initialize Devanagari script mapping."""
        return {
            1: 'अ', 2: 'आ', 3: 'इ', 4: 'ई', 5: 'उ', 6: 'ऊ',
            7: 'ऋ', 8: 'ए', 9: 'ऐ', 10: 'ओ', 11: 'औ', 12: 'अं',
            13: 'क', 14: 'ख', 15: 'ग', 16: 'घ', 17: 'ङ',
            18: 'च', 19: 'छ', 20: 'ज', 21: 'झ', 22: 'ञ',
            23: 'ट', 24: 'ठ', 25: 'ड', 26: 'ढ', 27: 'ण',
            28: 'त', 29: 'थ', 30: 'द', 31: 'ध', 32: 'न',
            33: 'प', 34: 'फ', 35: 'ब', 36: 'भ', 37: 'म',
            38: 'य', 39: 'र', 40: 'ल', 41: 'व', 42: 'श',
            43: 'ष', 44: 'स', 45: 'ह', 46: 'क्ष', 47: 'त्र',
            48: 'ज्ञ', 49: '०', 50: '१', 51: '२', 52: '३',
            53: '४', 54: '५', 55: '६', 56: '७', 57: '८',
            58: '९', 59: '॰', 60: '।', 61: '॥', 62: '्',
            63: 'ं', 64: 'ः'
        }

    def _init_kannada_map(self) -> Dict[int, str]:
        """Initialize Kannada script mapping."""
        return {
            1: 'ಅ', 2: 'ಆ', 3: 'ಇ', 4: 'ಈ', 5: 'ಉ', 6: 'ಊ',
            7: 'ಋ', 8: 'ಎ', 9: 'ಏ', 10: 'ಐ', 11: 'ಒ', 12: 'ಓ',
            13: 'ಔ', 14: 'ಕ', 15: 'ಖ', 16: 'ಗ', 17: 'ಘ',
            18: 'ಙ', 19: 'ಚ', 20: 'ಛ', 21: 'ಜ', 22: 'ಝ',
            23: 'ಞ', 24: 'ಟ', 25: 'ಠ', 26: 'ಡ', 27: 'ಢ',
            28: 'ಣ', 29: 'ತ', 30: 'ಥ', 31: 'ದ', 32: 'ಧ',
            33: 'ನ', 34: 'ಪ', 35: 'ಫ', 36: 'ಬ', 37: 'ಭ',
            38: 'ಮ', 39: 'ಯ', 40: 'ರ', 41: 'ಲ', 42: 'ವ',
            43: 'ಶ', 44: 'ಷ', 45: 'ಸ', 46: 'ಹ', 47: 'ಳ',
            48: '೦', 49: '೧', 50: '೨', 51: '೩', 52: '೪',
            53: '೫', 54: '೬', 55: '೭', 56: '೮', 57: '೯',
            58: '॰', 59: '।', 60: '॥', 61: '್', 62: 'ಂ',
            63: 'ಃ', 64: 'ೱ'
        }

    def _init_sanskrit_map(self) -> Dict[int, str]:
        """Initialize Sanskrit script mapping."""
        return {
            1: 'अ', 2: 'आ', 3: 'इ', 4: 'ई', 5: 'उ', 6: 'ऊ',
            7: 'ऋ', 8: 'ॠ', 9: 'ऌ', 10: 'ॡ', 11: 'ए', 12: 'ऐ',
            13: 'ओ', 14: 'औ', 15: 'क', 16: 'ख', 17: 'ग',
            18: 'घ', 19: 'ङ', 20: 'च', 21: 'छ', 22: 'ज',
            23: 'झ', 24: 'ञ', 25: 'ट', 26: 'ठ', 27: 'ड',
            28: 'ढ', 29: 'ण', 30: 'त', 31: 'थ', 32: 'द',
            33: 'ध', 34: 'न', 35: 'प', 36: 'फ', 37: 'ब',
            38: 'भ', 39: 'म', 40: 'य', 41: 'र', 42: 'ल',
            43: 'व', 44: 'श', 45: 'ष', 46: 'स', 47: 'ह',
            48: 'ळ', 49: 'क्ष', 50: 'ज्ञ', 51: '०', 52: '१',
            53: '२', 54: '३', 55: '४', 56: '५', 57: '६',
            58: '७', 59: '८', 60: '९', 61: '॰', 62: '।',
            63: '॥', 64: 'ऽ'
        }

    def get_char(self, number: int, script: str = 'devanagari') -> Optional[str]:
        """Get character for given number in specified script."""
        if not 1 <= number <= 64:
            return None
            
        if script == 'devanagari':
            return self.devanagari_map.get(number)
        elif script == 'kannada':
            return self.kannada_map.get(number)
        elif script == 'sanskrit':
            return self.sanskrit_map.get(number)
        else:
            raise ValueError(f"Unsupported script: {script}")

    def get_number(self, char: str, script: str = 'devanagari') -> Optional[int]:
        """Get number for given character in specified script."""
        if script == 'devanagari':
            mapping = self.devanagari_map
        elif script == 'kannada':
            mapping = self.kannada_map
        elif script == 'sanskrit':
            mapping = self.sanskrit_map
        else:
            raise ValueError(f"Unsupported script: {script}")

        for num, ch in mapping.items():
            if ch == char:
                return num
        return None
