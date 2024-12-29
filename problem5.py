from utils.file_operations import read_lines_from_file, read_all_text_from_file
from collections import defaultdict, deque

import re

def parse_input(input_text):
    """
    Parses the input into ordering rules and updates.
    """
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    return rules, updates

def is_update_valid2(update, rules):
    """
    Checks if an update is valid given the ordering rules.
    """
    pages_in_update = set(update)
    filtered_rules = [(x, y) for x, y in rules if x in pages_in_update and y in pages_in_update]
    page_index = {page: i for i, page in enumerate(update)}

    for x, y in filtered_rules:
        if page_index[x] >= page_index[y]:
            return False
    return True


def topological_sort(update, rules):
    """
    Reorders an update using topological sorting based on the rules.
    """
    # Filter rules to only include pages in the update
    pages_in_update = set(update)
    filtered_rules = [(x, y) for x, y in rules if x in pages_in_update and y in pages_in_update]

    # Build a graph (adjacency list) and compute in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in filtered_rules:
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0

    # Perform topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def is_update_valid(update, rules):
    """
    Checks if an update is valid given the ordering rules.
    """
    # Create a set of the pages in the update
    pages_in_update = set(update)

    # Filter rules to only those that involve pages in the update
    filtered_rules = [(x, y) for x, y in rules if x in pages_in_update and y in pages_in_update]

    # Create a mapping of page indices for the current update
    page_index = {page: i for i, page in enumerate(update)}

    # Check if each rule is satisfied
    for x, y in filtered_rules:
        if page_index[x] >= page_index[y]:
            return False
    return True


def find_middle_page(update):
    """
    Finds the middle page of an update.
    """
    return update[len(update) // 2]


def process_updates(input_text):
    """
    Processes the input, validates updates, and calculates the sum of middle pages.
    """
    # Parse the input
    rules, updates = parse_input(input_text)

    # Validate updates and sum middle pages
    total_middle_sum = 0
    for update in updates:
        if is_update_valid(update, rules):
            total_middle_sum += find_middle_page(update)

    return total_middle_sum


def process_incorrect_updates(input_text):
    """
    Processes the input, fixes incorrect updates, and calculates the sum of middle pages.
    """
    # Parse the input
    rules, updates = parse_input(input_text)

    # Identify and correct incorrect updates
    total_middle_sum = 0
    for update in updates:
        if not is_update_valid(update, rules):
            corrected_update = topological_sort(update, rules)
            total_middle_sum += find_middle_page(corrected_update)

    return total_middle_sum

# Example Input
input_text = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def problem_one():
    file_path = 'inputs/input5.txt'
    text = read_all_text_from_file(file_path)
    
    result = process_updates(text)
    print(f"Sum of middle pages: {result}")
                    

def problem_two():
    file_path = 'inputs/input5.txt'
    text = read_all_text_from_file(file_path)

    result = process_incorrect_updates(text)
    print(f"Sum of middle pages of corrected updates: {result}")
    