from copy import copy

def line_safe(list:list[int]) -> bool:

    if list == sorted(list) or list == sorted(list, reverse=True):

        for item in range(len(list)):

            # Item 0 has no preceding
            
            if item == 0:
                continue
            else:
                current = int(list[item])
                preceding = int(list[item-1])
            
            # Checking if difference from current to preceding is within allowed range.
            
            if not 1 <= abs(current - preceding) <= 3:
                return False
        
        return True


    else:
        return False

def dampener(list:list[int]):

    for index in range(len(list)):
        list_c = copy(list)
        del(list_c[index])
        if line_safe(list_c):
            return True
    
    return False


with open('../inputs/2_input.txt', 'r') as file:
    
    lines = file.readlines()
    
    safe_lines: int = 0
    safe_with_dampener: int = 0
    
    for line in lines:
        
        line_str: list[str] = list(line.strip().split())
        line_clean: list[int] = list(map(int, line_str))
        if line_safe(line_clean):
            safe_lines += 1
                    
        else: 

            if dampener(line_clean):
                safe_with_dampener += 1
    
    print(f'There are {safe_lines} without the dampener, {safe_lines + safe_with_dampener} with it.')
