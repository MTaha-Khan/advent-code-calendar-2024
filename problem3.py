from utils.file_operations import read_lines_from_file

import re

def parse_and_multiply(memory):
    """
    Parses a corrupted memory string for valid `mul(X,Y)` instructions,
    calculates the result of each multiplication, and returns their sum.
    """
    # Regular expression to match valid `mul(X,Y)` instructions
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the memory
    matches = re.findall(pattern, memory)
    
    # Compute the sum of all valid multiplications
    total = sum(int(x) * int(y) for x, y in matches)
    return total


def parse_and_multiply_do_donts(memory):
    """
    Parses the corrupted memory string and calculates the sum of all valid
    multiplications, considering the effects of do() and don't() instructions.
    """
    # Regular expression to match valid instructions
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    
     # Find all matches in the memory
    matches = re.finditer(pattern, memory)
    
    # Initialize state
    enabled = True
    total = 0
    
    # Process each match
    for match in matches:

        if match.group(1) and match.group(2):  # Check if it's a `mul(X,Y)` instruction
            if enabled:  # Only process if enabled
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y
        elif match.group(0) == "do()":  # Enable future `mul`
            enabled = True
        elif match.group(0) == "don't()":  # Disable future `mul`
            enabled = False
    
    return total


def problem_one():
    file_path = 'inputs/input3.txt'
    lines = read_lines_from_file(file_path)
    
    completeline = ""

    if lines:
        for line in lines:
            completeline += line 

    print(parse_and_multiply(completeline))
                    

def problem_two():
    file_path = 'inputs/input3.txt'
    lines = read_lines_from_file(file_path)

    completeline = ""

    if lines:
        for line in lines:
            completeline += line 

    print(parse_and_multiply_do_donts(completeline))
   