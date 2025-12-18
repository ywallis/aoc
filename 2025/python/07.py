def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        cleaned = []
        lines = file.readlines()

        for line in lines:
            cleaned.append(line.strip())

        return cleaned


def part1(matrix: list[str]) -> int:
    total = 0
    start = matrix[0]
    cur = [0] * len(start)
    first_beam = start.find("S")
    cur[first_beam] = 1

    for row in matrix[1:]:
        next = [0] * len(start)
        for i, pos in enumerate(cur):
            if pos == 0:
                continue
            if pos == 1:
                if row[i] == ".":
                    next[i] = 1
                else:
                    next[i - 1] = 1
                    next[i + 1] = 1
                    total += 1
        cur = next

    return total


def part2(matrix: list[str]) -> int:
    start = matrix[0]
    cur = [0] * len(start)
    first_beam = start.find("S")
    cur[first_beam] = 1

    for row in matrix[1:]:
        next = [0] * len(start)
        for i, pos in enumerate(cur):
            if pos == 0:
                continue
            else:
                if row[i] == ".":
                    next[i] += pos
                else:
                    next[i - 1] += pos
                    next[i + 1] += pos
        cur = next

    return sum(cur)


def main():
    input = load_example("07", False)

    res_1 = part1(input)
    print(res_1)

    res_2 = part2(input)
    print(res_2)


if __name__ == "__main__":
    main()
