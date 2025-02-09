"""
Pattern implementation module for Siri Bhoovalaya decryption.
Implements various Bandha patterns for matrix traversal.
"""

from typing import List, Generator, Tuple
import numpy as np
from .matrix import ChakraMatrix

class BandhaPatterns:
    def __init__(self, matrix: ChakraMatrix):
        """Initialize with a ChakraMatrix instance."""
        self.matrix = matrix

    def chakra_bandha(self, start_pos: Tuple[int, int]) -> Generator[int, None, None]:
        """
        Implement Chakra-Bandh pattern traversal.
        Moves in a spiral pattern from the given starting position.
        """
        rows, cols = self.matrix.size, self.matrix.size
        visited = np.zeros((rows, cols), dtype=bool)
        
        def is_valid(x: int, y: int) -> bool:
            return (0 <= x < rows and 0 <= y < cols and not visited[x][y])

        # Direction vectors for right, down, left, up
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x, y = start_pos
        dir_idx = 0
        
        for _ in range(rows * cols):
            if is_valid(x, y):
                visited[x][y] = True
                yield self.matrix.get_value(x, y)
                
                # Try to move in current direction
                next_x = x + dx[dir_idx]
                next_y = y + dy[dir_idx]
                
                if not is_valid(next_x, next_y):
                    # Change direction
                    dir_idx = (dir_idx + 1) % 4
                    x = x + dx[dir_idx]
                    y = y + dy[dir_idx]
                else:
                    x, y = next_x, next_y
            else:
                break

    def navamaank_bandha(self, start_pos: Tuple[int, int]) -> Generator[int, None, None]:
        """
        Implement Navamaank-Bandh pattern traversal.
        Moves in a 9-step pattern from the given starting position.
        """
        rows, cols = self.matrix.size, self.matrix.size
        visited = np.zeros((rows, cols), dtype=bool)
        
        # Nine-step movement pattern
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        
        x, y = start_pos
        
        while True:
            if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
                visited[x][y] = True
                yield self.matrix.get_value(x, y)
                
                # Try all possible moves
                valid_moves = []
                for i in range(8):
                    next_x = x + dx[i]
                    next_y = y + dy[i]
                    if (0 <= next_x < rows and 0 <= next_y < cols and 
                        not visited[next_x][next_y]):
                        valid_moves.append((next_x, next_y))
                
                if not valid_moves:
                    break
                    
                # Choose the next position
                x, y = valid_moves[0]
            else:
                break

    def diagonal_bandha(self) -> Generator[int, None, None]:
        """
        Implement Diagonal-Bandh pattern traversal.
        Traverses the matrix diagonally.
        """
        size = self.matrix.size
        
        # Traverse upper triangular matrix
        for k in range(size):
            for i in range(k + 1):
                j = k - i
                if j < size:
                    yield self.matrix.get_value(i, j)
        
        # Traverse lower triangular matrix
        for k in range(1, size):
            for i in range(k, size):
                j = size - 1 - (i - k)
                if j >= 0:
                    yield self.matrix.get_value(i, j)
