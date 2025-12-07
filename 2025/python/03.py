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


def find_highest_combo(line: int) -> int:
    highest_first_digit = 0
    highest_first_digit_idx = 0
    highest_second_digit = 0
    for i, n in enumerate(str(line)[:-1]):
        if int(n) > highest_first_digit:
            highest_first_digit = int(n)
            highest_first_digit_idx = i
    for i, n in enumerate(str(line)[highest_first_digit_idx + 1 :]):
        if int(n) > highest_second_digit:
            highest_second_digit = int(n)

    return int(str(highest_first_digit) + str(highest_second_digit))


def main():
    lines = load_example("03", False)
    total = 0
    for line in lines:
        total += find_highest_combo(line)

    print(total)


if __name__ == "__main__":
    main()
