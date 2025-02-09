"""
Matrix operations module for Siri Bhoovalaya decryption system.
Handles the 27x27 Chakra matrix operations.
"""

import numpy as np
from typing import List, Tuple

class ChakraMatrix:
    def __init__(self):
        """Initialize a 27x27 Chakra matrix."""
        self.size = 27
        self.matrix = np.zeros((self.size, self.size), dtype=int)
        self._initialize_matrix()
        print("Matrix initialized with dimensions:", self.matrix.shape)

    def _initialize_matrix(self) -> None:
        """Initialize the matrix with numbers 1-64 in the traditional pattern."""
        # Calculate quadrant size (13x13)
        quad_size = 13

        # Initialize first quadrant (1-16)
        current_number = 1
        for i in range(6):  # Using 6x6 area in top-left quadrant
            for j in range(6):
                if current_number <= 16:
                    self.matrix[i][j] = current_number
                    current_number += 1
                    print(f"Set position ({i},{j}) to {current_number-1}")

        # Initialize second quadrant (17-32)
        current_number = 17
        for i in range(6):
            for j in range(14, 20):  # Start after middle column
                if current_number <= 32:
                    self.matrix[i][j] = current_number
                    current_number += 1
                    print(f"Set position ({i},{j}) to {current_number-1}")

        # Initialize third quadrant (33-48)
        current_number = 33
        for i in range(14, 20):  # Start after middle row
            for j in range(6):
                if current_number <= 48:
                    self.matrix[i][j] = current_number
                    current_number += 1
                    print(f"Set position ({i},{j}) to {current_number-1}")

        # Initialize fourth quadrant (49-64)
        current_number = 49
        for i in range(14, 20):
            for j in range(14, 20):
                if current_number <= 64:
                    self.matrix[i][j] = current_number
                    current_number += 1
                    print(f"Set position ({i},{j}) to {current_number-1}")

    def get_value(self, row: int, col: int) -> int:
        """Get value at specific position."""
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.matrix[row][col]
        raise ValueError("Invalid matrix position")

    def set_value(self, row: int, col: int, value: int) -> None:
        """Set value at specific position."""
        if 0 <= row < self.size and 0 <= col < self.size:
            if 0 <= value <= 64:
                self.matrix[row][col] = value
            else:
                raise ValueError("Value must be between 0 and 64")
        else:
            raise ValueError("Invalid matrix position")

    def get_quadrant(self, quadrant: int) -> np.ndarray:
        """Get a specific quadrant of the matrix."""
        if quadrant not in [1, 2, 3, 4]:
            raise ValueError("Invalid quadrant number")

        mid = self.size // 2
        if quadrant == 1:
            return self.matrix[:mid, :mid]
        elif quadrant == 2:
            return self.matrix[:mid, mid:]
        elif quadrant == 3:
            return self.matrix[mid:, :mid]
        else:  # quadrant == 4
            return self.matrix[mid:, mid:]

    def rotate_quadrant(self, quadrant: int, clockwise: bool = True) -> None:
        """Rotate a specific quadrant of the matrix."""
        quad = self.get_quadrant(quadrant)
        rotated = np.rot90(quad, k=-1 if clockwise else 1)

        mid = self.size // 2
        if quadrant == 1:
            self.matrix[:mid, :mid] = rotated
        elif quadrant == 2:
            self.matrix[:mid, mid:] = rotated
        elif quadrant == 3:
            self.matrix[mid:, :mid] = rotated
        else:  # quadrant == 4
            self.matrix[mid:, mid:] = rotated

    def get_diagonal(self, primary: bool = True) -> List[int]:
        """Get diagonal elements."""
        if primary:
            return self.matrix.diagonal().tolist()
        return np.fliplr(self.matrix).diagonal().tolist()

    def __str__(self) -> str:
        """String representation of the matrix."""
        rows = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                val = self.matrix[i][j]
                row.append(f"{val:2d}" if val > 0 else "  ")
            rows.append(" ".join(row))
        return "\n".join(rows)