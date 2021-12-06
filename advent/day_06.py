from collections import Counter


def part_one(lanternfish: Counter[int]) -> int:
    return simulate(lanternfish, iterations=80)


def part_two(lanternfish: Counter[int]) -> int:
    return simulate(lanternfish, iterations=256)


def simulate(lanternfish: Counter[int], iterations: int) -> int:
    for _ in range(iterations):
        lanternfish = Counter({i - 1: lanternfish[i] for i in range(1, 9)}) + Counter(
            {
                6: lanternfish[0],
                8: lanternfish[0],
            }
        )

    return sum(lanternfish.values())


def read_puzzle(line: str) -> Counter[int]:
    return Counter(int(x) for x in line.strip().split(","))


if __name__ == "__main__":
    with open("../inputs/input_day_06.txt") as f:
        puzzle = read_puzzle(f.readline())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
