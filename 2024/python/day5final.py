from icecream import ic 

# Disabling icecream to clean up feed if needed

ic.disable()

# Defining functions


def list_passes(input_list: list[int], rules: list[tuple[int, int]]) -> bool:
    """The goal of this function is simply to check if a input list passes the order rules.
    It returns True if that is the case, and False otherwise. It does so by going through the input list iteratively, and checking if a rule exists
    for any combination."""
    
    for i, x in enumerate(input_list):
        
        ic(f'Currently at index {i} value {x}')
        
        for j, y in enumerate(input_list):
            
            ic(f'Currently at index {j} value {y}')
            
            # Skip self-compare
            
            if i == j:
                ic('Skipping self-compare {i} == {j}')
                continue
            
            # Check for rule violation
            
            if (x, y) in rules and i > j:

                ic(f'Wrong order, {x} should come before {y}.')
                
                return False
    
            if (y, x) in rules and j > i:
                
                ic(f'Wrong order, {y} should come before {x}.')

                return False
    
    ic('List passes!')
    
    return True



def shuffle_list(input_list, rules):
    
    for i, x in enumerate(input_list):
        
        ic(f'Currently at index {i} value {x}')
        
        for j, y in enumerate(input_list):
            
            ic(f'Currently at index {j} value {y}')
            
            # Skip self-compare
            
            if i == j:
                ic('Skipping self-compare {i} == {j}')
                continue
            
            # Check for rule violation
            
            if (x, y) in rules and i > j:

                ic(f'Wrong order, {x} should come before {y}.')
                
                # Swapping offending values
                
                input_list[j], input_list[i] = input_list[i], input_list[j]

                return input_list
    
            if (y, x) in rules and j > i:
                
                ic(f'Wrong order, {y} should come before {x}.')
                
                # Swapping offending values

                input_list[j], input_list[i] = input_list[i], input_list[j]

                return input_list
    
    ic('List passes!')
    
    return input_list


# Initialize lists to import from file

rules = []
numbers = []

# Import values from files

with open('input.txt', 'r') as file:
    
    lines = file.readlines()
    ic(lines[0])
    for line in lines:
        if '|' in line:
            x = int(line.split('|')[0])
            y = int(line.split('|')[1])
            rules.append((x, y))
        elif line != '\n':
            line_n = line.strip().split(',')
            numbers.append(list(map(int, line_n)))

# Display full value lists

ic(rules)
ic(numbers)

valid_lists = []
invalid_lists = []


for _ in numbers:
    if list_passes(_, rules):
        valid_lists.append(_)
    else:
        invalid_lists.append(_)

ic(invalid_lists)
corrected_lists = []

bf_index = 1

for _ in invalid_lists:
    while not list_passes(_, rules):
        _ = shuffle_list(_, rules)
    corrected_lists.append(_)
    print(f'Found {bf_index} solutions of {len(invalid_lists)}')
    bf_index += 1


middles = []
sum_of_middles = 0

for _ in corrected_lists:
    middle_index = len(_) // 2
    middles.append(_[middle_index])
    sum_of_middles += _[middle_index]

ic.enable()

ic(middles)
ic(sum_of_middles)
