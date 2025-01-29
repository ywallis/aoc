import re


with open('../inputs/3_input.txt', 'r') as file:
    string = file.read()

occurences: list[str] = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", str(string))

counter_switch: int = 0
counter: int = 0
active: bool = True

digits: list[str] = []

for match in occurences:
    if match.startswith('mul') and active:
        digits  = re.findall(r'\d{1,3}', match)
        counter += (int(digits[0]) * int(digits[1]))


for match in occurences:
    if match.startswith('mul') and active:
        digits = re.findall(r'\d{1,3}', match)
        counter_switch += (int(digits[0]) * int(digits[1]))
    if match == 'do()':
        active = True
    if match == "don't()":
        active = False


print(f'Part 1 is {counter}, part 2 is {counter_switch}.')

