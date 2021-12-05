import pytest

from advent.day_03 import part_one, part_two, read_puzzle

lines = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


@pytest.fixture
def small_puzzle():
    return read_puzzle(lines.strip().split("\n"))


@pytest.fixture
def puzzle():
    with open("../inputs/input_day_03.txt") as f:
        return read_puzzle(f.readlines())


def test_small_puzzle(small_puzzle):
    assert part_one(small_puzzle) == 198
    assert part_two(small_puzzle) == 230


def test_solution(puzzle):
    assert part_one(puzzle) == 4006064
    assert part_two(puzzle) == 5941884
