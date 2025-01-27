import time

list_a: list[int] = []
list_b: list[int] = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # print(line.strip().split())
        line_clean = line.strip().split()
        list_a.append(int(line_clean[0]))
        list_b.append(int(line_clean[1]))


def compare_lists(list1: list[int], list2: list[int]) -> int:
    assert len(list1) == len(list2)
    sorted_1 = sorted(list1)
    sorted_2 = sorted(list2)
    cumulative = 0

    for index in range(len(list1)):
        n1 = sorted_1[index]
        n2 = sorted_2[index]
        cumulative += max(n1, n2) - min(n1, n2)

    return cumulative


def calculate_similarity(list1: list[int], list2: list[int]) -> int:
    score = 0

    # Going through list1, then list2

    for n1 in list1:
        for n2 in list2:
            if n1 == n2:
                score += n1

    return score


start = time.perf_counter()
print(compare_lists(list_a, list_b))
print(calculate_similarity(list_a, list_b))

end = time.perf_counter()

print(f"Time elapsed: {(end - start):.6f}")
