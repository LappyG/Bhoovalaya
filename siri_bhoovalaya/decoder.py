"""
Main decoder module for Siri Bhoovalaya decryption system.
Coordinates matrix operations, pattern traversal, and character mapping.
"""

from typing import List, Optional
from rich.console import Console
from rich.table import Table
from .matrix import ChakraMatrix
from .patterns import BandhaPatterns
from .mappings import CharacterMap

class SiriBhoovalayaDecoder:
    def __init__(self):
        """Initialize the decoder with required components."""
        self.matrix = ChakraMatrix()
        self.patterns = BandhaPatterns(self.matrix)
        self.char_map = CharacterMap()
        self.console = Console()

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
        table = Table(title="Siri Bhoovalaya Matrix")
        
        # Add columns
        for i in range(self.matrix.size):
            table.add_column(str(i))

        # Add rows
        for i in range(self.matrix.size):
            row = [str(self.matrix.get_value(i, j)) for j in range(self.matrix.size)]
            table.add_row(*row)

        self.console.print(table)

    def analyze_pattern(self, pattern: str, start_pos: tuple = (0, 0)) -> None:
        """Analyze and display a pattern traversal."""
        try:
            if pattern == 'chakra':
                pattern_gen = self.patterns.chakra_bandha(start_pos)
            elif pattern == 'navamaank':
                pattern_gen = self.patterns.navamaank_bandha(start_pos)
            elif pattern == 'diagonal':
                pattern_gen = self.patterns.diagonal_bandha()
            else:
                raise ValueError(f"Unsupported pattern: {pattern}")

            self.console.print(f"\n[bold]Pattern Analysis: {pattern}[/bold]")
            self.console.print("Traversal sequence:")
            
            sequence = list(pattern_gen)
            for i, value in enumerate(sequence):
                self.console.print(f"Step {i+1}: {value}")

        except Exception as e:
            self.console.print(f"[red]Error during pattern analysis: {str(e)}[/red]")
