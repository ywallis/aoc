def find_neighbours(point: tuple[int, int], map: list[list[int]]):

    rows: int = len(map)
    cols: int = len(map[0])

    neighbours: list[tuple[int, int]] = []

    directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx: int = point[0] + dx
        ny: int = point[1] + dy

        if 0 <= nx <= cols - 1 and 0 <= ny <= rows - 1:
            neighbours.append((nx, ny))

    return neighbours


def find_peak(head: tuple[int, int], map: list[list[int]]):

    peak: set[tuple[int, int]] = set()
    all_trails: list[tuple[int, int]] = []

    cur_val: int = map[head[0]][head[1]]

    def rec_help(head: tuple[int, int], map: list[list[int]], val: int):

        neighbours: list[tuple[int, int]] = find_neighbours(head, map)

        for neighbour in neighbours:
            if val == 8 and map[neighbour[0]][neighbour[1]] == 9:
                peak.add(neighbour)
                all_trails.append(neighbour)

            if map[neighbour[0]][neighbour[1]] == val + 1:

                rec_help(neighbour, map, val + 1)

    rec_help(head, map, cur_val)
    return len(peak), len(all_trails)


with open("../inputs/10_input.txt", "r") as file:

    lines = file.readlines()

    safe_lines: int = 0
    safe_with_dampener: int = 0
    matrix: list[list[int]] = []

    for line in lines:

        line_str: list[str] = list(line.strip())
        line_clean: list[int] = list(map(int, line_str))
        matrix.append(line_clean)


score: int = 0
trail_score: int = 0

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):

        if cell == 0:
            peaks, trails = find_peak((i, j), matrix)
            score += peaks
            trail_score += trails

print(f"Total score is {score}, amount of trails is {trail_score}.")
