from utils.file_operations import read_lines_from_file

import re

def count_xmas_occurrences(grid, word="XMAS"):
    """
    Counts all occurrences of the word 'XMAS' in the grid in all directions.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Helper function to check if a match exists in a specific direction
    def matches_at(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols):  # Out of bounds
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    # Check all directions for each cell
    for x in range(rows):
        for y in range(cols):
            # Directions: (dx, dy)
            directions = [
                (0, 1),   # Horizontal right
                (0, -1),  # Horizontal left
                (1, 0),   # Vertical down
                (-1, 0),  # Vertical up
                (1, 1),   # Diagonal down-right
                (-1, -1), # Diagonal up-left
                (1, -1),  # Diagonal down-left
                (-1, 1)   # Diagonal up-right
            ]
            for dx, dy in directions:
                if matches_at(x, y, dx, dy):
                    count += 1

    return count




# Example word search grid
word_search = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]


def problem_one():
    file_path = 'inputs/input4.txt'
    lines = read_lines_from_file(file_path)
    
    # Count all occurrences of 'XMAS'
    result = count_xmas_occurrences(lines)
    print(f"Total occurrences of 'XMAS': {result}")
                    

def problem_two():
    file_path = 'inputs/input4.txt'
    lines = read_lines_from_file(file_path)

    rows = len(lines)
    cols = len(lines[0])
    count = 0

    # Helper function to check if a diagonal matches MAS or SAM
    def matches_diagonal(x, y, dx, dy):
        pattern = ""
        for i in range(3):  # A diagonal for MAS or SAM is 3 characters long
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols):  # Out of bounds
                return False
            pattern += lines[nx][ny]
        return pattern in {"MAS", "SAM"}

    # Check for X-MAS patterns
    for x in range(rows):
        for y in range(cols):
            # Ensure there's space for both diagonals
            if (0 <= x - 1 < rows and 0 <= x + 1 < rows and
                0 <= y - 1 < cols and 0 <= y + 1 < cols):
                # Top-left to bottom-right diagonal
                if matches_diagonal(x - 1, y - 1, 1, 1):
                    # Top-right to bottom-left diagonal
                    if matches_diagonal(x - 1, y + 1, 1, -1):
                        count += 1

    print(f"Total occurrences of 'X-MAS': {count}")

    
   
