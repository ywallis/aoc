def load_example(day: str, example: bool = True) -> list[str]:
    """Load the input for a certain day from a text file."""
    file_path = (
        f"../inputs/{day}_example.txt" if example else f"../inputs/{day}_input.txt"
    )
    with open(file_path, "r") as file:
        cleaned = []
        lines = file.readlines()

        for line in lines:
            cleaned.append(line.strip())

        return cleaned
