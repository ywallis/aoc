# There are two main ideas at work here:
# - Although it is stated otherwise, the order of the stones don't matter.
# - Stones follow a set path, so if you've calculated the transformation of one once, you don't need to do it again.

# The second point should scream HASHMAP, and that's what we are doing.""""


def stone_split(stone: int) -> list[int]:

    if stone == 0:

        return [1]
    elif len(str(stone)) % 2 == 0:

        middle: int = len(str(stone)) // 2
        a = int(str(stone)[0:middle])
        b = int(str(stone)[middle:])
        return [a, b]

    else:
        return [stone * 2024]


# Set iterations here

iterations: int = 75 

with open("../inputs/11_input.txt") as file:
    vec: list[int] = [int(x) for x in file.readlines()[0].strip().split()]

    hashmap: dict[int, int] = {k: 1 for k in vec}

    for i in range(iterations):

        new_hashmap: dict[int, int] = {}

        for stone, num in hashmap.items():
            for new_stone in stone_split(stone):
                # If the calculation has already been made, add the new quantity

                if new_stone in new_hashmap:
                    new_hashmap[new_stone] += num
                else:
                    new_hashmap[new_stone] = num

        hashmap = new_hashmap

    print(
        f"Length of vec (amount of stones) after {iterations} iterations is {sum(hashmap.values())}"
    )
