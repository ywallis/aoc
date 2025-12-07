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


def main():
    line = load_example("02", False)
    id_blocks: ranges = get_ranges(line)
    print(part_1(id_blocks))


if __name__ == "__main__":
    main()
