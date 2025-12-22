from itertools import combinations

from utils import load_example


def parse_input(data: list[str]) -> list[tuple[int, int]]:
    data_lines = [line.split(",") for line in data]
    parsed_lines = [(int(x), int(y)) for x, y in data_lines]
    return parsed_lines


def calculate_area(x: tuple[int, int], y: tuple[int, int]) -> int:
    x_vec = (max(x[0], y[0]) - min(x[0], y[0])) + 1
    y_vec = (max(x[1], y[1]) - min(x[1], y[1])) + 1

    return x_vec * y_vec


def part_1(data: list[tuple[int, int]]) -> int:
    all_combinations = combinations(data, 2)

    areas = []
    for x, y in all_combinations:
        areas.append(calculate_area(x, y))

    return max(areas)


def part_2(data: list[tuple[int, int]]):
    pass


def main():
    input = load_example("09", False)
    data = parse_input(input)
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
