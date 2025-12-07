def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        lines = file.readlines()
        cleaned_output = []
        for line in lines:
            line = line.replace("\n", "")
            line.strip()
            cleaned_output.append(line)

    return cleaned_output


def split_rotations(rotations: list[str]) -> list[tuple[str, int]]:
    output = []

    for i, rotation in enumerate(rotations):
        output.append((rotation[0], int(rotation[1:])))
    return output


def main():
    input = load_example("01", False)

    rotations = split_rotations(input)

    dial = 50
    count = 0

    for rotation in rotations:
        if rotation[0] == "R":
            dial += rotation[1]
        if rotation[0] == "L":
            dial -= rotation[1]
        dial = dial % 100
        if dial < 0:
            dial = 100 + dial
        if dial == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
