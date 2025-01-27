from icecream import ic
from collections import defaultdict
from copy import deepcopy

ic.disable()

def antinode_jump(pos1: tuple, pos2: tuple) -> tuple:
    result = tuple(a - b for a, b in zip(pos1, pos2))
    return result

def find_antinodes(list_of_antennas: list, limit_x: int, limit_y:int) -> list[tuple]:

    antinodes = set()

    for antenna_x in list_of_antennas:
        for antenna_y in list_of_antennas:
            if antenna_x == antenna_y:
                continue
            
            jump = antinode_jump(antenna_x, antenna_y)
            all_pos = set()
            antenna_pos = deepcopy([antenna_y[0], antenna_y[1]])
            antenna_neg = deepcopy([antenna_y[0], antenna_y[1]])

            while antenna_pos[0] <= limit_x and antenna_pos[1] <= limit_y and antenna_pos[0] >= 0 and antenna_pos[1] >= 0:
                ic('Pre', antenna_pos)
                antenna_pos[0] = antenna_pos[0] + jump[0]
                antenna_pos[1] = antenna_pos[1] + jump[1]
                ic('Post', antenna_pos)
                ic(jump)
                #if (antenna_pos[0], antenna_pos[1]) != antenna_x:
                all_pos.add((antenna_pos[0], antenna_pos[1]))
                ic(all_pos)

            while antenna_neg[0] <= limit_x and antenna_neg[1] <= limit_y and antenna_neg[0] >= 0 and antenna_neg[1] >= 0:
                antenna_neg[0] = antenna_neg[0] - jump[0]
                antenna_neg[1] = antenna_neg[1] - jump[1]
                ic(antenna_neg)
                #if (antenna_neg[0], antenna_neg[1]) != antenna_x:
                all_pos.add((antenna_neg[0], antenna_neg[1]))

            #pos_x1 = tuple(a + b for a, b in zip(antenna_x, jump))
            #pos_x2 = tuple(a - b for a, b in zip(antenna_x, jump))
            #pos_y1 = tuple(a + b for a, b in zip(antenna_y, jump))
            #pos_y2 = tuple(a - b for a, b in zip(antenna_y, jump))
            
            #all_pos = [pos_x1, pos_x2, pos_y1, pos_y2]

            for pos in all_pos:
                if pos[0] >= 0 and pos[1] >= 0:
                    antinodes.add(pos)

    return antinodes


antennas = defaultdict(list)
all_antinodes = set()
x_limit = 0
y_limit = 0


with open('input.txt', 'r') as file:
    lines = file.readlines()
    for y, line in enumerate(lines):
        ic(line.strip())
        y_limit = y
        for x, char in enumerate(line.strip()):
            if char != '.':
                antennas[char].append((int(x), int(y)))
            x_limit = x

ic(antennas)

for index, key in enumerate(antennas):
    print(f'Starting antenna {key}, {index + 1} of {len(antennas)}')
    all_nodes = find_antinodes(antennas[key], x_limit, y_limit)
    ic(key, all_nodes)
    for node in all_nodes:
        ic(node[0], x_limit, node[1], y_limit)
        if node[0] <= x_limit and node[1] <= y_limit:
            all_antinodes.add(node)

print(all_antinodes)
print('Total antinodes:', len(all_antinodes))
