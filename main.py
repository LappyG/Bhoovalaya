#!/usr/bin/env python3
"""
Siri Bhoovalaya Decryption System
Command-line interface for the ancient Indian cryptographic method
"""

import sys
import argparse
from typing import List, Optional
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from siri_bhoovalaya.decoder import SiriBhoovalayaDecoder
from siri_bhoovalaya.matrix import ChakraMatrix
from siri_bhoovalaya.patterns import BandhaPatterns

def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="Siri Bhoovalaya Decryption System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--sequence',
        type=str,
        help='Comma-separated sequence of numbers to decrypt'
    )
    parser.add_argument(
        '--pattern',
        choices=['chakra', 'navamaank', 'diagonal'],
        default='chakra',
        help='Pattern to use for decryption'
    )
    parser.add_argument(
        '--script',
        choices=['devanagari', 'kannada', 'sanskrit'],
        default='devanagari',
        help='Script to use for character mapping'
    )
    parser.add_argument(
        '--start-pos',
        type=str,
        default='0,0',
        help='Starting position for pattern traversal (row,col)'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run in interactive mode'
    )
    return parser

def parse_sequence(sequence_str: str) -> Optional[List[int]]:
    """Parse comma-separated sequence string into list of integers."""
    try:
        sequence = [int(x.strip()) for x in sequence_str.split(',')]
        if all(1 <= x <= 64 for x in sequence):
            return sequence
        raise ValueError("Numbers must be between 1 and 64")
    except ValueError as e:
        print(f"Error parsing sequence: {str(e)}")
        return None

def parse_start_pos(pos_str: str) -> tuple:
    """Parse start position string into tuple."""
    try:
        row, col = map(int, pos_str.split(','))
        if 0 <= row < 27 and 0 <= col < 27:
            return (row, col)
        raise ValueError("Position must be within matrix bounds (0-26)")
    except ValueError as e:
        print(f"Error parsing start position: {str(e)}")
        return (0, 0)

def interactive_mode():
    """Run the decoder in interactive mode."""
    decoder = SiriBhoovalayaDecoder()
    print("\nSiri Bhoovalaya Decryption System")
    print("Interactive Mode")
    print("-" * 40)

    while True:
        try:
            print("\nAvailable Commands:")
            print("1. Decrypt sequence")
            print("2. Display matrix")
            print("3. Analyze pattern")
            print("4. Exit")

            choice = input("\nSelect an option [1/2/3/4]: ").strip()
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid option. Please try again.")
                continue

            if choice == "3":
                print("\nAvailable patterns: chakra, navamaank, diagonal")
                pattern = input("Select pattern type [chakra]: ").strip().lower() or "chakra"
                if pattern not in ["chakra", "navamaank", "diagonal"]:
                    print("Invalid pattern. Using chakra.")
                    pattern = "chakra"

                start_pos_str = input("Enter start position (row,col) [0,0]: ").strip() or "0,0"
                start_pos = parse_start_pos(start_pos_str)
                decoder.analyze_pattern(pattern, start_pos)
                continue

            if choice == "1":
                sequence_str = input("Enter sequence (comma-separated numbers): ").strip()
                sequence = parse_sequence(sequence_str)
                if sequence:
                    print("\nAvailable patterns: chakra, navamaank, diagonal")
                    pattern = input("Select pattern [chakra]: ").strip().lower() or "chakra"
                    if pattern not in ["chakra", "navamaank", "diagonal"]:
                        pattern = "chakra"

                    print("\nAvailable scripts: devanagari, kannada, sanskrit")
                    script = input("Select script [devanagari]: ").strip().lower() or "devanagari"
                    if script not in ["devanagari", "kannada", "sanskrit"]:
                        script = "devanagari"

                    start_pos_str = input("Enter start position (row,col) [0,0]: ").strip() or "0,0"
                    start_pos = parse_start_pos(start_pos_str)

                    result = decoder.decrypt_sequence(
                        sequence,
                        pattern=pattern,
                        script=script,
                        start_pos=start_pos
                    )

                    if result:
                        print("\nDecryption Result:")
                        print("-" * 40)
                        print(result)
                        print("-" * 40)

            elif choice == "2":
                decoder.display_matrix()

            elif choice == "4":
                print("\nExiting...")
                break

        except KeyboardInterrupt:
            print("\nExiting due to user interrupt...")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            continue

def main():
    """Main entry point of the application."""
    parser = create_parser()
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not args.sequence:
        print("Error: Sequence is required in non-interactive mode")
        parser.print_help()
        sys.exit(1)

    sequence = parse_sequence(args.sequence)
    if not sequence:
        sys.exit(1)

    start_pos = parse_start_pos(args.start_pos)
    decoder = SiriBhoovalayaDecoder()

    result = decoder.decrypt_sequence(
        sequence,
        pattern=args.pattern,
        script=args.script,
        start_pos=start_pos
    )

    if result:
        print("\nDecryption Result:")
        print("-" * 40)
        print(result)
        print("-" * 40)

if __name__ == "__main__":
    main()