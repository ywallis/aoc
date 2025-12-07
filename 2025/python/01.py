from typing import TypeAlias

rotations: TypeAlias = list[tuple[str, int]]


def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        lines = file.readlines()
        cleaned_output = []
        for line in lines:
            line = line.strip()
            cleaned_output.append(line)

    return cleaned_output


def split_rotations(rotations: list[str]) -> rotations:
    output = []

    for i, rotation in enumerate(rotations):
        output.append((rotation[0], int(rotation[1:])))
    return output


def find_part_1(rotations: rotations) -> int:
    dial = 50
    count = 0

    for rotation in rotations:
        if rotation[0] == "R":
            dial += rotation[1]
        if rotation[0] == "L":
            dial -= rotation[1]
        dial = dial % 100
        if dial == 0:
            count += 1

    return count


def find_part_2(rotations: rotations) -> int:
    virtual_dial = 50
    count = 0

    for direction, amount in rotations:
        prev_dial = virtual_dial

        if direction == "R":
            virtual_dial += amount
            count += (virtual_dial // 100) - (prev_dial // 100)

        elif direction == "L":
            virtual_dial -= amount
            count += ((prev_dial - 1) // 100) - ((virtual_dial - 1) // 100)

        # print(virtual_dial, count, virtual_dial % 100)

    return count


def main():
    input = load_example("01", False)

    rotations = split_rotations(input)

    # part_1 = find_part_1(rotations)
    # print(part_1)
    part_2 = find_part_2(rotations)
    print(part_2)


if __name__ == "__main__":
    main()
