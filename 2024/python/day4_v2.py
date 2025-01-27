import pandas as pd

def find_matches(matrix, x, y, word):
    neighbors = set()
    x_limit = df.shape[0] -1
    y_limit = df.shape[1] -1
    word_limit = len(word) - 1
    for i in [x-word_limit, x, x+word_limit]:
        for j in [y-word_limit, y, y+word_limit]:
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

word = 'XMAS'
matches = 0
df = pd.DataFrame(matrix)

for index, row in df.iterrows():
    for col in df.columns:

        if row[col] == 'X':
            m_set = find_matches(df, col, index, word)
            start_tuple = (col, index)
            print('this is', start_tuple)
            print(m_set)
            for point in m_set:
                print(point)
                x_step = int((point[0] - start_tuple[0]) / (len(word) - 1))
                y_step = int((point[1] - start_tuple[1]) / (len(word) - 1))
                counter = 1
                for letter in word[1:]:
                    print(letter)
                    df.iloc[start_tuple[1] + (y_step * counter), start_tuple[0] + (x_step * counter)]
                    if df.iloc[start_tuple[1] + (y_step * counter), start_tuple[0] + (x_step * counter)] == letter:

                        
                        print('continue')
                        counter += 1
                    else:
                        print('fail')
                        break
                    
                    if letter == word[-1]:
                        matches += 1
print(matches)
