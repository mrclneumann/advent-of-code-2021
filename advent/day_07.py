from statistics import median


def part_one(positions: list[int]) -> int:
    return int(sum(abs(position - median(positions)) for position in positions))


def part_two(positions: list[int]) -> int:
    return min(
        sum(costs(abs(position - i)) for position in positions)
        for i in range(min(positions), max(positions) + 1)
    )


def costs(steps: int) -> int:
    return steps * (steps + 1) // 2


def read_puzzle(line: str) -> list[int]:
    return [int(x) for x in line.strip().split(",")]


if __name__ == "__main__":
    with open("../inputs/input_day_07.txt") as f:
        puzzle = read_puzzle(f.readline())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
