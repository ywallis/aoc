from typing import TypeAlias

ranges: TypeAlias = list[tuple[int, int]]


def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        line = file.readline()

        return line


def get_ranges(line: str) -> ranges:
    output = []

    split_lines = line.split(",")
    for li in split_lines:
        start, end = li.split("-")
        output.append((int(start), int(end)))

    return output


def part_1(id_blocks: ranges) -> int:
    count = 0
    for block in id_blocks:
        for i in range(block[0], block[1]):
            str_rep = str(i)
            if len(str_rep) % 2 != 0:
                continue
            str_middle = int(len(str_rep) / 2)
            if str_rep[:str_middle] == str_rep[str_middle:]:
                count += i

    return count


def part_2(id_blocks: ranges) -> int:
    invalid = set()

    for n in range(1, 100_000):
        r = 2

        d = n

        while int(str(n) * r) < 10_000_000_000:
            d = int(str(n) * r)

            for block in id_blocks:
                range_min = block[0]
                range_max = block[1]
                if range_min <= d <= range_max:
                    invalid.add(d)
            r += 1

    return sum(invalid)


def main():
    line = load_example("02", False)
    id_blocks: ranges = get_ranges(line)
    print(part_2(id_blocks))


if __name__ == "__main__":
    main()
