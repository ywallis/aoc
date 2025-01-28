from icecream import ic
import operator
from itertools import product
from multiprocessing import Pool

ic.disable()

def line_valid(input_list: list[int], operators: list[tuple]) -> bool:
    
    target = input_list[0]
    all_combinations = []
    all_operator_permutations = ''
    
    perms = product([op for op in operators], repeat=len(input_list) - 2)
    result = [perm for perm in perms]
    
    for number in input_list[1:]:

        for combination in result:

            combined = [input_list[1]]
        
            for index, operator in enumerate(combination):
                
                combined.append(operator)
                combined.append(input_list[index + 2])
        
            ic(combined)
            all_combinations.append(combined)
    
    for x in all_combinations:
        
        while len(x) > 1:
            ic('Start', x)
            
            operation = x[:3]
            
            
            if operation[1] == '+':
                result = operation[0] + operation[2]

            elif operation[1] == '|':
                result = int(str(operation[0]) + str(operation[2]))
            
            else:
                result = operation[0] * operation[2]
            
            del x[:2]
            
            x[0] = result
            ic('End', x)

            if x[0] == target:
                return True

    return False

def process_item(args):
    index, item, list_of_operators = args
    print(f'Processing item {index}')
    if line_valid(item, list_of_operators):
        return item[0]
    return 0

def main(list_of_all, list_of_operators):
    total = 0

    # Prepare arguments for each task
    tasks = [(index, item, list_of_operators) for index, item in enumerate(list_of_all)]

    with Pool() as pool:

        # Use map to process items in parallel
        results = pool.map(process_item, tasks)

    # Calculate total from the results
    total = sum(results)

    print(f"Final total: {total}")
    return total

list_of_operators = ['+', '*', '|']

list_of_all = []

with open('input.txt', 'r') as file:
    
    lines = file.readlines()
    for line in lines:
        line_clean = [int(x.strip(':')) for x in line.strip().split()]
        list_of_all.append(line_clean)

ic(list_of_all)

# total = 0

#for index, item in enumerate(list_of_all):
#    print(f'Iterating through {index} of {len(list_of_all)}')
#    if line_valid(item, list_of_operators):
#        total += item[0]

#print('Total is:', total)

main(list_of_all, list_of_operators)
