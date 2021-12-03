import pandas as pd


def count_increases(s: pd.Series) -> int:
    return (s.diff() > 0).sum()


def part_one(report: list[int]) -> int:
    return count_increases(pd.Series(report))


def part_two(report: list[int]) -> int:
    return count_increases(pd.Series(report).rolling(3).sum())


def read_puzzle(lines: list[str]) -> list[int]:
    return [int(line.strip()) for line in lines]


if __name__ == "__main__":
    with open("../inputs/input_day_01.txt") as f:
        puzzle = read_puzzle(f.readlines())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
