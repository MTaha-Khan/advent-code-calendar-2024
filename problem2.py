from utils.file_operations import read_lines_from_file


def safe_report(levels):
    n = levels[0]
    
    if (levels[0] == levels[1]):
        return False
    
    d = (levels[0] - levels[1]) < 0
    for num in levels[1:]:
        
        if num == n:
            return False
        elif abs(num - n) < 1 or abs(num - n) > 3:
            return False
        elif d == True and num < n:
            return False
        elif d == False and num > n:
            return False
        else:
            n = num

    return True


def is_safe_with_dampener(levels):
    """Check if a report is safe, either directly or with the Problem Dampener."""
    # Check if the report is already strictly decreasing
    if safe_report(levels):
        return True

    # Check if removing any single level makes it strictly decreasing
    for i in range(len(levels)):
        # Create a new list without the i-th level
        modified_levels = levels[:i] + levels[i + 1:]
        if safe_report(modified_levels):
            return True

    # If neither condition is met, the report is unsafe
    return False


def problem_one():
    file_path = 'inputs/input2.txt'
    lines = read_lines_from_file(file_path)
    
    safe_reports = 0

    if lines:
        for line in lines:
            safe = safe_report(list(map(int, line.split())))
            if safe:
                safe_reports += 1
            
    print(safe_reports)
                    

def problem_two():
    file_path = 'inputs/input2.txt'
    lines = read_lines_from_file(file_path)

    safe_reports = 0

    if lines:
        for line in lines:
            safe = is_safe_with_dampener(list(map(int, line.split())))
            if safe:
                safe_reports += 1
            
    print(safe_reports)
