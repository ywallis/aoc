from icecream import ic 

# Disabling icecream to clean up feed

ic.disable()

# Defining functions

def list_passes(input_list: list[int], rules: list[tuple[int, int]]) -> bool:
    """The goal of this function is simply to check if a input list passes the order rules.
    It returns True if that is the case, and False otherwise. It does so by going through the input list iteratively, and checking if a rule exists
    for any combination."""
    
    x_index: int = 0

    correct_order: bool = True
    
    for x in input_list:
        ic(x)
        y_index: int = x_index + 1
        for y in input_list[x_index + 1:]:
            if (y, x) in rules:
               ic(f'Rule for {y}, {x}')
               ic(y_index)
               if y_index < x_index:
                    ic('Order is fine')

               else:
                    ic('Order not fine, breaking')
                    correct_order = False
                    break
            if (x, y) in rules:
                ic(f'Rule for {x}, {y}')
                ic(y_index)
                if x_index < y_index:
                    ic('Order is fine')

                else:
                    ic('Order not fine, breaking')
                    correct_order = False
                    break
            y_index += 1
            
        x_index += 1

    if correct_order:
        ic('List passes!')
        return True
    else:
        return False
        ('List fails!')


def shuffle_list(input_list, rules):
    
    x_index = 0

    for x in input_list:
        ic(x)
        
        y_index = x_index + 1
        
        for y in input_list[x_index + 1:]:
            
            if (y, x) in rules:
                ic(f'Rule for {y}, {x}')
                ic(y_index)
                if y_index < x_index:
                    ic('Order is fine')

                else:
                    ic('Order not fine, breaking')
                    input_list[y_index], input_list[x_index] = input_list[x_index], input_list[y_index]
                    return input_list
            if (x, y) in rules:
                ic(f'Rule for {x}, {y}')
                ic(y_index)
                if x_index < y_index:
                    ic('Order is fine')

                else:
                    ic('Order not fine, breaking')
                    input_list[y_index], input_list[x_index] = input_list[x_index], input_list[y_index]
                    return input_list
            y_index += 1
            
        x_index += 1




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
