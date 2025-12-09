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


def parse_input(input: list[str]) -> tuple[list[list[int]], list[int]]:
    switch = False
    ranges = []
    ids = []

    for s in input:
        if s == "":
            switch = True
            continue
        if switch is True:
            ids.append(int(s))
        else:
            range_components = s.split("-")
            start, end = range_components[0], range_components[1]
            ranges.append([int(start), int(end)])
    return ranges, ids


def part_1(input: list[str]) -> int:
    count = 0
    ranges, ids = parse_input(input)

    for id in ids:
        for r in ranges:
            start, end = r[0], r[1]
            if start <= id <= end:
                count += 1
                break
    return count


def combine_ranges(ranges: list[list[int]]) -> list[list[int]]:
    ranges.sort(key=lambda x: x[0])
    combined_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        last_end = combined_ranges[-1][1]
        if start <= last_end:
            combined_ranges[-1][1] = max(end, last_end)
        else:
            combined_ranges.append([start, end])

    return combined_ranges


def part_2(input: list[str]) -> int:
    ranges, ids = parse_input(input)

    total = 0
    combined_ranges = combine_ranges(ranges)
    for r in combined_ranges:
        total += r[1] - r[0] + 1

    return total


def main():
    input = load_example("05", False)

    print(part_2(input))


if __name__ == "__main__":
    main()
