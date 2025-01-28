import pandas as pd
from icecream import ic
from itertools import cycle
from copy import deepcopy, copy

class Guard:
    
    directions = {'^': (-1, 0, '>'),
                  '>': (0, 1, 'v'),
                  'v': (1, 0, '<'),
                  '<': (0, -1, '^'),
                  }
    
    def __init__(self, y, x):
        self.coordinates = [y, x]
        self.direction_cycle = cycle(Guard.directions) 
        self.direction = next(self.direction_cycle)
        self.new_blockers = 0
        self.been = set()
        self.been_with_direction = set()

        #self.been.add((self.coordinates[0], self.coordinates[1]))
        #self.been_with_direction.add((self.coordinates[0], self.coordinates[1], self.direction))

    def add_direction(self, position, direction):

        f_position = copy(position)
        
        f_position[0] = f_position[0] + Guard.directions[direction][0] 
        f_position[1] = f_position[1] + Guard.directions[direction][1] 
        
        return f_position

    def move(self, full_map):
        
        future_position = self.add_direction(self.coordinates, self.direction)
        # Manually referencing the new direction if a blocker were to be there, as to not trigger the iterator
        possible_direction = Guard.directions[self.direction][2]
        path_with_blocker = self.add_direction(self.coordinates, possible_direction)
        ic(path_with_blocker)
        ic(possible_direction)

        try:
        
            while full_map.loc[future_position[0], future_position[1]] == '#':
                ic(self.coordinates)
                ic(future_position)
                self.direction = next(self.direction_cycle)
                ic(self.direction)
            
                future_position = self.add_direction(self.coordinates, self.direction)
                possible_direction = Guard.directions[self.direction][2]
                path_with_blocker = self.add_direction(self.coordinates, possible_direction)
            
            else:

                full_map.loc[self.coordinates[0], self.coordinates[1]] = self.direction
            
                self.coordinates = future_position

                full_map.loc[self.coordinates[0], self.coordinates[1]] = self.direction
                self.been.add((self.coordinates[0], self.coordinates[1]))
                if (self.coordinates[0], self.coordinates[1], self.direction) in self.been_with_direction:
                    print("I've been here before")
                self.been_with_direction.add((self.coordinates[0], self.coordinates[1], self.direction))

        except KeyError:

            print('Next step out of range, guard should get deleted next turn')
        
            full_map.loc[self.coordinates[0], self.coordinates[1]] = self.direction 

            self.coordinates = future_position

with open('example.txt', 'r') as file:
    
    lines = file.readlines()
    
    matrix = []

    for line in lines:
        line_list = []
        line_clean = line.strip()
        for char in line_clean:
            line_list.append(char)

        matrix.append(line_list)


df = pd.DataFrame(matrix)
df_og = deepcopy(df)
for index, row in df.iterrows():
    for col, value in row.items():

        if value == '^':
            guard = Guard(index, col)

y_limit = df.shape[0] - 1
x_limit = df.shape[1] - 1
looping = True

while looping:
#for _ in range(0,30):
    # print(df)
    
        
    if guard.coordinates[0] > y_limit or guard.coordinates[1] > x_limit:
        looping = False
        
    else:
        guard.move(df)

total_values = 0
brute_force = 0

for index, row in df.iterrows():
    for col, value in row.items():
        if value in ['^', '>', 'v', '<'] :
            total_values += 1

print(total_values)
print(guard.new_blockers)
print(len(guard.been))

for position in guard.been:
    map_copy = deepcopy(df_og)
    ic(f'adding # to {map_copy.loc[position[0], position[1]]}')
    map_copy.loc[position[0], position[1]] = '#'
    ic(position)
    for index, row in map_copy.iterrows():
        for col, value in row.items():

            if value == '^':
                new_guard = Guard(index, col)
    
    looping = True
    new_guard_been = set() 

    while looping:
    #for _ in range(0,30):
        # print(df)
        ic(new_guard_been)
            
        if (new_guard.coordinates[0], new_guard.coordinates[1], new_guard.direction) in new_guard_been:
            # looping = False
            ic('sanity')
            ic(new_guard_been)
            ic((new_guard.coordinates[0], new_guard.coordinates[1], new_guard.direction))
            brute_force += 1
            del(new_guard)
            del(new_guard_been)
            looping = False

        elif new_guard.coordinates[0] > y_limit or new_guard.coordinates[1] > x_limit:
            looping = False
            #del(new_guard)
            
        else:
            new_guard.move(map_copy)
            new_guard_been.add((new_guard.coordinates[0], new_guard.coordinates[1], new_guard.direction))
ic(brute_force)    
