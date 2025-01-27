from icecream import ic
from copy import copy

ic.disable()

def find_holes(input: list):

    start_pointer = 0
    end_pointer = len(input) - 1

    while start_pointer < len(input) -1 and end_pointer > 0:

        # Move start_pointer to the next dot
        while input[start_pointer] != '.':
            start_pointer += 1
            ic(start_pointer)
            
        secondary = copy(start_pointer)
        while input[secondary] == '.' and secondary < end_pointer:
            secondary += 1
            ic(secondary)
        memory_gap = secondary - start_pointer
        ic(memory_gap)

        # Move end_pointer to the last non-dot character
        while input[end_pointer] == '.':
            end_pointer -= 1
            ic(end_pointer)
        
        tertiary = copy(end_pointer) 

        while input[tertiary] == input[end_pointer] and tertiary > 0:
            tertiary -= 1
            ic(tertiary)

        data_size = end_pointer - tertiary
        
        ic(data_size)
        # If start_pointer crosses end_pointer, we are done
        if start_pointer > len(input) -1 or end_pointer <= 0:
            break

        #ic('swapping', input[start_pointer:start_pointer + data_size], input[tertiary + 1:end_pointer + 1])
        #ic('with', input[tertiary + 1:end_pointer + 1], input[start_pointer:start_pointer + data_size])
        ic(end_pointer, tertiary)
        # Swap characters
        if memory_gap >= data_size and data_size != 0:
            ic('swapping', input[start_pointer:start_pointer + data_size], input[tertiary + 1:end_pointer + 1])
            ic('with', input[tertiary + 1:end_pointer + 1], input[start_pointer:start_pointer + data_size])
            input[start_pointer:start_pointer + data_size], input[tertiary + 1:end_pointer + 1] = input[tertiary + 1:end_pointer + 1], input[start_pointer:start_pointer + data_size] 
            start_pointer = 0
        else:
            start_pointer += 1

        if secondary >= tertiary:
            end_pointer = tertiary
            start_pointer = 0
            


        ic(input)


    return input

def check_sum(input: list) -> int:
    
    checksum = 0

    for index, char in enumerate(input):
        if char != '.':
            checksum += int(char) * index

    return checksum

def find_edges_it(input: list, start=0, end=None) -> list:
    

    start_pointer = start
    if end is None:
        end_pointer = len(input) - 1
    else:
        end_pointer = end

    while True:
        # Move start_pointer to the next dot
        while input[start_pointer] != '.':
            start_pointer += 1

        # Move end_pointer to the last non-dot character
        while input[end_pointer] == '.':
            end_pointer -= 1

        # If start_pointer crosses end_pointer, we are done
        if start_pointer >= end_pointer:
            break

        # Swap characters
        input[start_pointer], input[end_pointer] = input[end_pointer], '.'

    return input


def find_edges(input: list, start=0, end=None) -> str:
    input = list(input)

    start_pointer = start
    if end is None:
        end_pointer = len(input) - 1
    else:
        end_pointer = end
    
    while input[start_pointer] != '.':
        start_pointer += 1

    while input[end_pointer] == '.':
        end_pointer -= 1
    
    ic(''.join(input))
    ic(start_pointer, end_pointer) 
    ic(input[start_pointer], input[end_pointer])
    
    if start_pointer < end_pointer:
        input[start_pointer] = input[end_pointer]
        input[end_pointer] = '.'
    ic(''.join(input))
    buffer = copy(input)
    while start_pointer < end_pointer:
        return find_edges(''.join(buffer), start_pointer, end_pointer)
    else:
        return ''.join(input)



def show_empty(input: str) -> str:
    
    output = []
    file_index = 0

    for index, char in enumerate(input):
    
        if index % 2 == 0:
            
            for _ in range(int(char)):
            
                output.append(str(file_index))
            file_index += 1

        else:
            
            for _ in range(int(char)):
            
                output.append('.')

    return output

with open('input.txt', 'r') as file:
    data = file.readline().strip()
    ic(data)
    with_empty = show_empty(data)
    print(with_empty)
    defragmented = find_holes(with_empty)
    print(defragmented)
    #ordered = find_edges_it(with_empty)
    #print(ordered)
    print(check_sum(defragmented))


