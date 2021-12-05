import re
from collections import Counter, namedtuple
from itertools import chain
from typing import Iterable

import numpy as np

Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["a", "b"])


def points(line: Line) -> Iterable[Point]:
    a: Point
    b: Point

    a, b = (
        (
            line.a,
            line.b,
        )
        if line.a < line.b
        else (line.b, line.a)
    )

    for i in range(np.subtract(b, a).max() + 1):
        if horizontal(line):
            dx = 1
            dy = 0
        elif vertical(line):
            dx = 0
            dy = 1
        else:
            dx = 1
            dy = 1 if a.y < b.y else -1

        yield a.x + i * dx, a.y + i * dy


def vertical(line: Line) -> bool:
    return line.a.x == line.b.x


def horizontal(line: Line) -> bool:
    return line.a.y == line.b.y


def diagonal(line: Line) -> bool:
    return not (vertical(line) or horizontal(line))


def part_one(lines: list[Line]) -> int:
    return count_overlap(
        chain.from_iterable(
            points(line) for line in lines if vertical(line) or horizontal(line)
        )
    )


def part_two(lines: list[Line]) -> int:
    return count_overlap(chain.from_iterable(points(line) for line in lines))


def count_overlap(lines: Iterable[Line]) -> int:
    return len([v for v in Counter(lines).values() if v > 1])


def read_puzzle(lines: list[str]) -> list[Line]:
    vents = []

    for line in lines:
        m = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line.strip())
        vents.append(
            Line(
                Point(int(m.group(1)), int(m.group(2))),
                Point(int(m.group(3)), int(m.group(4))),
            )
        )

    return vents


if __name__ == "__main__":
    with open("../inputs/input_day_05.txt") as f:
        puzzle = read_puzzle(f.readlines())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
