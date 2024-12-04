import pandas as pd

def find_matches(matrix, x, y, word):
    neighbors = set()
    x_limit = df.shape[0] -1
    y_limit = df.shape[1] -1
    word_limit = len(word) - 1
    for i in [x-1, x+1]:
        for j in [y-1, y+1]:
            if (i, j) != (x, y) and 0 <= i <= x_limit and 0 <= j <= y_limit:
                neighbors.add((i, j))
    
    return neighbors


# Find X

# Find neighbors

# Check if direction has x cells

# Check if string present


with open('input.txt', 'r') as file:
    
    lines = file.readlines()
    
    matrix = []

    for line in lines:
        line_list = []
        line_clean = line.strip()
        for char in line_clean:
            line_list.append(char)

        matrix.append(line_list)

word = 'MAS'
matches = 0
df = pd.DataFrame(matrix)

for index, row in df.iterrows():
    for col in df.columns:

        if row[col] == word[1]:
            m_set = find_matches(df, col, index, word)
            print(m_set)
            s_list = sorted(list(m_set))
            print(s_list)
            n_m = 0
            n_s = 0
            for point in m_set:
                if df.iloc[point[1], point[0]] == word[0]:
                    n_m += 1

                if df.iloc[point[1], point[0]] == word[2]:
                    n_s += 1
                #print(df.iloc[point[1], point[0]])
                print(n_m, n_s)


            if n_m == 2 and n_s == 2:
                lowest = s_list[-0]
                highest = s_list[-1]
                if df.iloc[lowest[1], lowest[0]] != df.iloc[highest[1], highest[0]]:
                    matches += 1

print(matches)
