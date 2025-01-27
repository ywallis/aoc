import re


with open('input.txt', 'r') as file:
    string = file.read()
    print(string)
    occurences = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", str(string))
    print(occurences)
    
    counter = 0
    active = True
    
    for match in occurences:
        if match.startswith('mul') and active:
            digits = re.findall(r'\d{1,3}', match)
            print(digits)
            counter += (int(digits[0]) * int(digits[1]))
        if match == 'do()':
            active = True
        if match == "don't()":
            active = False
    print(counter)

