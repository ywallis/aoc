def find_matches_diagonal(matrix: list[list[str]], x: int, y: int) -> set[tuple[int, int]]:

    """This function takes in a matrix and a coordinate, and returns all diagonal neighbors from that coordinate."""

    neighbors: set[tuple[int, int]] = set()
    x_limit: int = len(matrix[0]) - 1
    y_limit: int = len(matrix) - 1
    for i in [x - 1, x + 1]:
        for j in [y - 1, y + 1]:
            if (i, j) != (x, y) and 0 <= i <= x_limit and 0 <= j <= y_limit:
                neighbors.add((i, j))

    return neighbors


def find_matches(matrix: list[list[str]], x: int, y: int, word: str) -> set[tuple[int, int]]:

    """This function takes in a matrix and a coordinate and returns all neighbors from that coordinate."""

    neighbors: set[tuple[int, int]] = set()
    x_limit: int = len(matrix[0]) - 1
    y_limit: int = len(matrix) - 1
    word_limit = len(word) - 1
    for i in [x - word_limit, x, x + word_limit]:
        for j in [y - word_limit, y, y + word_limit]:
            if (i, j) != (x, y) and 0 <= i <= x_limit and 0 <= j <= y_limit:
                neighbors.add((i, j))

    return neighbors


with open("../inputs/4_input.txt", "r") as file:

    lines = file.readlines()

    matrix: list[list[str]] = []

    for line in lines:
        line_list: list[str] = []
        line_clean = line.strip()
        for char in line_clean:
            line_list.append(char)

        matrix.append(line_list)

word = "XMAS"
matches = 0

for index, row in enumerate(matrix):
    for j, cell in enumerate(row):

        if cell == "X":
            m_set = find_matches(matrix, j, index, word)
            start_tuple = (j, index)
            for point in m_set:
                x_step = int((point[0] - start_tuple[0]) / (len(word) - 1))
                y_step = int((point[1] - start_tuple[1]) / (len(word) - 1))
                counter = 1
                for letter in word[1:]:
                    matrix[start_tuple[1] + (y_step * counter)][
                        start_tuple[0] + (x_step * counter)
                    ]
                    if (
                        matrix[start_tuple[1] + (y_step * counter)][
                            start_tuple[0] + (x_step * counter)
                        ]
                        == letter
                    ):

                        counter += 1
                    else:
                        break

                    if letter == word[-1]:
                        matches += 1
print(f'There are {matches} "XMAS" matches')

# Part 2

word = "MAS"
matches: int = 0
for index, row in enumerate(matrix):
    for j, cell in enumerate(row):

        if cell == word[1]:

            m_set = find_matches_diagonal(matrix, j, index)
            s_list = sorted(list(m_set))
            n_m = 0
            n_s = 0
            for point in m_set:
                if matrix[point[1]][point[0]] == word[0]:
                    n_m += 1

                if matrix[point[1]][point[0]] == word[2]:
                    n_s += 1

            if n_m == 2 and n_s == 2:
                lowest = s_list[0]
                highest = s_list[-1]
                if matrix[lowest[1]][lowest[0]] != matrix[highest[1]][highest[0]]:
                    matches += 1

print(f'There are {matches} cross MAS')
