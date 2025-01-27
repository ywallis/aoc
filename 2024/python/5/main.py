from icecream import ic 

rules = []
numbers = []

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

ic(rules)
ic(numbers)

valid_lists = []

def list_passes(input_list, rules):
    
    x_index = 0

    correct_order = True

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
        ic('List fails!')

for _ in numbers:
    if list_passes(_, rules):
        valid_lists.append(_)

ic(valid_lists)

middles = []
sum_of_middles = 0

for _ in valid_lists:
    middle_index = len(_) // 2
    middles.append(_[middle_index])
    sum_of_middles += _[middle_index]

ic(middles)
ic(sum_of_middles)
