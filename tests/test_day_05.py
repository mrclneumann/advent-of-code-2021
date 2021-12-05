import pytest

from advent.day_05 import part_one, part_two, read_puzzle

lines = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


@pytest.fixture
def small_puzzle():
    return read_puzzle(lines.strip().split("\n"))


@pytest.fixture
def puzzle():
    with open("../inputs/input_day_05.txt") as f:
        return read_puzzle(f.readlines())


def test_small_puzzle(small_puzzle):
    assert part_one(small_puzzle) == 5
    assert part_two(small_puzzle) == 12


def test_solution(puzzle):
    assert part_one(puzzle) == 4728
    assert part_two(puzzle) == 17717
