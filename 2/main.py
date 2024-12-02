from copy import copy

def line_safe(list:list) -> bool:

    if list == sorted(list) or list == sorted(list, reverse=True):
        print('Direction is valid! Continuing')

        for item in range(len(list)):
            if item == 0:
                continue
            else:
                current = int(list[item])
                preceding = int(list[item-1])
            
            
            if not 1 <= abs(current - preceding) <= 3:
                #print('Difference too high')
                #print(current, preceding)
                return False
        
        return True


    else:
        print('Not sorted')
        return False

def dampener(list:list):

    for index in range(len(list)):
        list_c = copy(list)
        del(list_c[index])
        print(list_c)
        if line_safe(list_c):
            return True
    
    return False


with open('input.txt', 'r') as file:
    
    lines = file.readlines()
    
    safe_lines: int = 0
    
    for line in lines:
        
        line_str: list = list(line.strip().split())
        line_clean = list(map(int, line_str))
        if line_safe(line_clean):
            print('passed', line_clean)
            safe_lines += 1
                    
        else: 
            print('failed, trying dampener', line_clean)

            if dampener(line_clean):
                print('passed', line_clean)
                safe_lines += 1
            else:
                print('failed again')
    
    print(safe_lines)


