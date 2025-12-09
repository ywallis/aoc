moves = [(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if dr != 0 or dc != 0]


def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        cleaned = []
        lines = file.readlines()

        for line in lines:
            cleaned.append(list(line.strip()))

        return cleaned


def traverse_matrix(map: list[list[str]]) -> int:
    valid_spots = 0
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "@":
                neighbors = count_neighbors(map, (x, y))
                if neighbors < 4:
                    valid_spots += 1
    return valid_spots


def traverse_matrix_2(map: list[list[str]]) -> int:
    valid_spots = 0
    future_removal = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "@":
                neighbors = count_neighbors(map, (x, y))
                if neighbors < 4:
                    valid_spots += 1
                    future_removal.append((x, y))
    for spot in future_removal:
        map[spot[1]][spot[0]] = "."
    return valid_spots


def count_neighbors(map: list[list[str]], position: tuple[int, int]) -> int:
    neighbor_count = 0
    for move in moves:
        relative_pos = (position[0] + move[0], position[1] + move[1])
        x, y = relative_pos[0], relative_pos[1]
        if x < 0 or y < 0:
            continue
        if y >= len(map) or x >= len(map[0]):
            continue
        if map[y][x] == "@":
            neighbor_count += 1

    return neighbor_count


def main():
    map = load_example("04", False)

    total = 0
    removed = float("inf")
    while removed != 0:
        removed = traverse_matrix_2(map)
        total += removed

    print(total)


if __name__ == "__main__":
    main()
