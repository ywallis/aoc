import math
from itertools import combinations


def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        cleaned = []
        lines = file.readlines()

        for line in lines:
            cleaned.append(tuple(line.strip().split(",")))

        return cleaned


def euclidian_distance(x: tuple[str, ...], y: tuple[str, ...]) -> float:
    return math.sqrt(sum([(int(x[i]) - int(y[i])) ** 2 for i in range(len(x))]))


def part_1(boxes: list[tuple[str, ...]], limit: int) -> int:
    collections: list[set[tuple[str, ...]]] = []
    combos = combinations(boxes, 2)
    distances = [(euclidian_distance(x, y), x, y) for x, y in combos]
    distances.sort(key=lambda x: x[0])

    for i in range(limit + 1):
        box_x = distances[i][1]
        box_y = distances[i][2]

        added = False
        for collection in collections:
            if box_x in collection or box_y in collection:
                collection.add(box_x)
                collection.add(box_y)
                added = True
                break
        if not added:
            collections.append(set([box_x, box_y]))

    collections.sort(key=lambda x: len(x), reverse=True)
    top3l = [len(x) for x in collections[:3]]

    return math.prod(top3l)


def main():
    input = load_example("08", False)

    LIMIT = 1000
    print(part_1(input, LIMIT))


if __name__ == "__main__":
    main()
