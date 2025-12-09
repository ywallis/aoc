def load_example(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        cleaned = []
        lines = file.readlines()

        for line in lines:
            cleaned.append(line.strip().split())

        return cleaned


def load_example_part_2(day: str, example: bool = True):
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        cleaned = []
        lines = file.readlines()

        sub_list = []
        operands, operators = lines[:-1], lines[-1].strip().split()
        for i in reversed(range(len(operands[0][:-1]))):
            col = ""
            for o in operands:
                col += o[i]

            if col.strip() == "":
                cleaned.append(sub_list)
                sub_list = []
            else:
                sub_list.append(int(col.strip()))
        cleaned.append(sub_list)

        operators.reverse()
        return cleaned, operators


def part_1(input: list[list[str]]) -> int:
    total = 0

    operands, operators = input[:-1], input[-1]

    for i, col in enumerate(operands[0]):
        col_total = int(operands[0][i])

        if operators[i] == "*":
            for row in operands[1:]:
                col_total *= int(row[i])
        else:
            for row in operands[1:]:
                col_total += int(row[i])
        total += col_total

    return total


def part_2(operands: list[list[int]], operators: list[str]) -> int:
    total = 0

    for i in range(len(operands)):
        col_total = int(operands[i][0])
        if operators[i] == "*":
            for n in operands[i][1:]:
                col_total *= int(n)
        else:
            for n in operands[i][1:]:
                col_total += int(n)
        total += col_total

    return total


def main():
    operands, operators = load_example_part_2("06", False)
    print(part_2(operands, operators))


if __name__ == "__main__":
    main()
