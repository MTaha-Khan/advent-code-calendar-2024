from utils.file_operations import read_lines_from_file

def problem_one():
    file_path = 'inputs/input1.txt'
    lines = read_lines_from_file(file_path)
    
    numbers1 = []
    numbers2 = []

    if lines:
        for line in lines:
            nums = line.strip().split()
            numbers1.append(int(nums[0]))
            numbers2.append(int(nums[1]))
    
    numbers1.sort()
    numbers2.sort()
    distance = 0

    for i in range(0, len(numbers1)): 
        distance = distance + abs(numbers1[i] - numbers2[i])

    print(distance)

def problem_two():
    file_path = 'inputs/input1.txt'
    lines = read_lines_from_file(file_path)
    
    numbers1 = []
    numbers2 = []

    if lines:
        for line in lines:
            nums = line.strip().split()
            numbers1.append(int(nums[0]))
            numbers2.append(int(nums[1]))
    
    numbers1.sort()
    numbers2.sort()
    similarity = 0

    for i in range(0, len(numbers1)): 
        count = 0
        for j in range(0, len(numbers2)):
            if numbers1[i] == numbers2[j]:
                count +=1
        similarity += count * numbers1[i]
        
    print(similarity)
