import math
from itertools import combinations


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.size = [1] * size
        self.sets = size

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def unite(self, i: int, j: int):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
            self.size[irep] = 0
            self.sets -= 1


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
    combos = combinations(range(len(boxes)), 2)
    distances = [(euclidian_distance(boxes[x], boxes[y]), x, y) for x, y in combos]
    distances.sort(key=lambda x: x[0])

    uf = UnionFind(len(boxes))
    for i in range(limit):
        uf.unite(distances[i][1], distances[i][2])
    t3 = sorted(uf.size, reverse=True)[:3]

    return math.prod(t3)


def part_2(boxes: list[tuple[str, ...]]) -> int:
    combos = combinations(range(len(boxes)), 2)
    distances = [(euclidian_distance(boxes[x], boxes[y]), x, y) for x, y in combos]
    distances.sort(key=lambda x: x[0])

    uf = UnionFind(len(boxes))
    i = 0
    while uf.sets > 1:
        uf.unite(distances[i][1], distances[i][2])
        i += 1

    a, b = boxes[distances[i - 1][1]], boxes[distances[i - 1][2]]

    return int(a[0]) * int(b[0])


def main():
    input = load_example(
        "08",
    )

    LIMIT = 1000
    print(part_1(input, LIMIT))
    print(part_2(input))


if __name__ == "__main__":
    main()
