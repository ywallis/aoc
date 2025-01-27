import pandas as pd

def find_neighbors(matrix, x, y):
    neighbors = set()
    x_limit = df.shape[0] -1
    y_limit = df.shape[1] -1
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if (i, j) != (x, y) and 0 <= i <= x_limit and 0 <= j <= y_limit:
                neighbors.add((i, j))
    
    return neighbors

def check_neighbors(matrix, x, y, target_char):
    
    neighbors = find_neighbors(matrix, x, y)
    has_nice_neighbors = set()
    for location in neighbors:
        if matrix.iloc[location[1], location[0]] == target_char:
            has_nice_neighbors.add(location)

    return has_nice_neighbors
    

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


for index, row in df.iterrows():
    for col in df.columns:
        a_set = set()
        s_set = set()

        if row[col] == 'X':
            m_set = check_neighbors(df, col, index, 'M')
            for _ in m_set:
                a_set.add(check_neighbors(df, col, index, 'A'))
            for _ in a_set:
                s_set.add(check_neighbors(df, col, index, 'S'))
            print(s_set)

            #x_neighbors = find_neighbors(df, col, index) 
            #for location in x_neighbors:
                #if df.iloc[location[0], location[1]] == 'M':
                    #print('found one M')

            # print('Only X', x_neighbors)

