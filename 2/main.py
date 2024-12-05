with open('example.txt', 'r') as file:
    
    lines = file.readlines()
    
    safe_lines: int = 0
    
    for line in lines:
        
        line_clean: list = list(line.strip().split())
        print(line_clean)
        
        if line_clean == sorted(line_clean) or line_clean == sorted(line_clean, reverse=True):
            print('Direction is valid! Continuing')

            for item in range(len(line_clean)):
                if item == 0:
                    continue
                else:
                    current = int(line_clean[item])
                    preceding = int(line_clean[item-1])
                
                if current == preceding:
                    print('Repeating value')
                    break
    
                elif abs(current - preceding) > 3:
                    print('Difference too high')
                    break
        safe_lines += 1
    
    print(safe_lines)


