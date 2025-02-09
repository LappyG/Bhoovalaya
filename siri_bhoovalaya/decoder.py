"""
Main decoder module for Siri Bhoovalaya decryption system.
Coordinates matrix operations, pattern traversal, and character mapping.
"""

from typing import List, Optional
from rich.console import Console
from rich.table import Table
from rich.box import SQUARE
from rich.style import Style
from .matrix import ChakraMatrix
from .patterns import BandhaPatterns
from .mappings import CharacterMap

class SiriBhoovalayaDecoder:
    def __init__(self):
        """Initialize the decoder with required components."""
        try:
            self.matrix = ChakraMatrix()
            self.patterns = BandhaPatterns(self.matrix)
            self.char_map = CharacterMap()
            self.console = Console()
            print("Decoder initialized successfully")
        except Exception as e:
            print(f"Error during initialization: {str(e)}")
            raise

    def decrypt_sequence(self, 
                        sequence: List[int], 
                        pattern: str = 'chakra',
                        script: str = 'devanagari',
                        start_pos: tuple = (0, 0)) -> str:
        """
        Decrypt a sequence of numbers using specified pattern and script.
        """
        try:
            # Validate inputs
            if not sequence:
                raise ValueError("Empty sequence provided")
            if not all(1 <= x <= 64 for x in sequence):
                raise ValueError("Sequence numbers must be between 1 and 64")

            # Get pattern traversal
            if pattern == 'chakra':
                pattern_gen = self.patterns.chakra_bandha(start_pos)
            elif pattern == 'navamaank':
                pattern_gen = self.patterns.navamaank_bandha(start_pos)
            elif pattern == 'diagonal':
                pattern_gen = self.patterns.diagonal_bandha()
            else:
                raise ValueError(f"Unsupported pattern: {pattern}")

            # Map numbers to positions in pattern
            position_map = {}
            for pos, value in enumerate(pattern_gen):
                position_map[value] = pos

            # Decrypt sequence
            result = [''] * len(sequence)
            for i, num in enumerate(sequence):
                char = self.char_map.get_char(num, script)
                if char:
                    pos = position_map.get(num, i)
                    result[pos] = char

            return ''.join(result)

        except Exception as e:
            self.console.print(f"[red]Error during decryption: {str(e)}[/red]")
            return ""

    def display_matrix(self) -> None:
        """Display the current matrix state in a formatted table."""
        try:
            print("\nSiri Bhoovalaya Matrix:")
            print("=" * 81)  # Header separator

            # Print column headers
            print("   ", end="")  # Space for row numbers
            for i in range(self.matrix.size):
                print(f"{i:2d} ", end="")
            print("\n" + "-" * 81)  # Separator after headers

            # Print matrix rows with row numbers
            for i in range(self.matrix.size):
                print(f"{i:2d}|", end=" ")
                for j in range(self.matrix.size):
                    val = self.matrix.get_value(i, j)
                    if val > 0:
                        print(f"{val:2d}", end=" ")
                    else:
                        print("  ", end=" ")
                print()  # New line after each row

            print("=" * 81)  # Footer separator
            print("\nMatrix display completed successfully")

        except Exception as e:
            print(f"Error in display_matrix: {str(e)}")

    def analyze_pattern(self, pattern: str, start_pos: tuple = (0, 0)) -> None:
        """Analyze and display a pattern traversal."""
        try:
            print(f"\nAnalyzing {pattern} pattern from position {start_pos}:")
            print("=" * 50)

            if pattern == 'chakra':
                pattern_gen = self.patterns.chakra_bandha(start_pos)
                description = "Spiral pattern traversal"
            elif pattern == 'navamaank':
                pattern_gen = self.patterns.navamaank_bandha(start_pos)
                description = "Nine-step pattern traversal"
            elif pattern == 'diagonal':
                pattern_gen = self.patterns.diagonal_bandha()
                description = "Diagonal pattern traversal"
            else:
                raise ValueError(f"Unsupported pattern: {pattern}")

            print(f"\nPattern Type: {pattern}")
            print(f"Description: {description}")
            print(f"Starting Position: {start_pos}")
            print("\nTraversal Sequence:")
            print("-" * 50)

            sequence = list(pattern_gen)
            for i, value in enumerate(sequence, 1):
                if i % 5 == 0:  # Line break every 5 numbers
                    print(f"{value:2d}")
                else:
                    print(f"{value:2d}", end=" -> ")

            print("\nTotal steps:", len(sequence))
            print("=" * 50)

        except Exception as e:
            print(f"Error during pattern analysis: {str(e)}")