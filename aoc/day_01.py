import pandas as pd


def count_increases(s: pd.Series):
    return (s.diff() > 0).sum()


def part_01(report: list[str]) -> int:
    return count_increases(pd.Series(int(x) for x in report))


def part_02(report: list[str]):
    return count_increases(pd.Series(int(x) for x in report).rolling(3).sum())


if __name__ == "__main__":
    with open("../inputs/input_day_01.txt") as f:
        report = [row.strip() for row in f.readlines()]

    print(f"Part 1: {part_01(report)}")
    print(f"Part 2: {part_02(report)}")
