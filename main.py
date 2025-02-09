#!/usr/bin/env python3
"""
Siri Bhoovalaya Decryption System
Command-line interface for the ancient Indian cryptographic method
"""

import sys
import argparse
from typing import List, Optional
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout
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
        console = Console()
        console.print(f"[red]Error parsing sequence: {str(e)}[/red]")
        return None

def parse_start_pos(pos_str: str) -> tuple:
    """Parse start position string into tuple."""
    try:
        row, col = map(int, pos_str.split(','))
        if 0 <= row < 27 and 0 <= col < 27:
            return (row, col)
        raise ValueError("Position must be within matrix bounds (0-26)")
    except ValueError as e:
        console = Console()
        console.print(f"[red]Error parsing start position: {str(e)}[/red]")
        return (0, 0)

def interactive_mode():
    """Run the decoder in interactive mode."""
    console = Console()
    decoder = SiriBhoovalayaDecoder()

    console.print(Panel.fit(
        "[bold blue]Siri Bhoovalaya Decryption System[/bold blue]\n"
        "Interactive Mode",
        title="Welcome"
    ))

    while True:
        try:
            console.print("\n[bold green]Available Commands:[/bold green]")
            console.print("1. Decrypt sequence")
            console.print("2. Display matrix")
            console.print("3. Analyze pattern")
            console.print("4. Exit")

            choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4"])

            if choice == "3":
                pattern = Prompt.ask(
                    "Select pattern type",
                    choices=["chakra", "navamaank", "diagonal"],
                    default="chakra"
                )
                start_pos_str = Prompt.ask(
                    "Enter start position (row,col)",
                    default="0,0"
                )
                start_pos = parse_start_pos(start_pos_str)
                decoder.analyze_pattern(pattern, start_pos)
                continue

            if choice == "1":
                sequence_str = Prompt.ask("Enter sequence (comma-separated numbers)")
                sequence = parse_sequence(sequence_str)
                if sequence:
                    pattern = Prompt.ask(
                        "Select pattern",
                        choices=["chakra", "navamaank", "diagonal"],
                        default="chakra"
                    )
                    script = Prompt.ask(
                        "Select script",
                        choices=["devanagari", "kannada", "sanskrit"],
                        default="devanagari"
                    )
                    start_pos_str = Prompt.ask(
                        "Enter start position (row,col)",
                        default="0,0"
                    )
                    start_pos = parse_start_pos(start_pos_str)

                    result = decoder.decrypt_sequence(
                        sequence,
                        pattern=pattern,
                        script=script,
                        start_pos=start_pos
                    )

                    console.print("\n[bold]Decryption Result:[/bold]")
                    console.print(Panel(Text(result, justify="center")))

            elif choice == "2":
                decoder.display_matrix()

            else:  # choice == "4"
                console.print("[yellow]Exiting...[/yellow]")
                break

        except EOFError:
            console.print("\n[yellow]Exiting due to EOF...[/yellow]")
            break
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting due to user interrupt...[/yellow]")
            break
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
            continue

def main():
    """Main entry point of the application."""
    parser = create_parser()
    args = parser.parse_args()
    console = Console()

    if args.interactive:
        interactive_mode()
        return

    if not args.sequence:
        console.print("[red]Error: Sequence is required in non-interactive mode[/red]")
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

    console.print("\n[bold]Decryption Result:[/bold]")
    console.print(Panel(Text(result, justify="center")))

if __name__ == "__main__":
    main()