import pytest

from advent.day_07 import part_one, part_two, read_puzzle

lines = """
16,1,2,0,4,2,7,1,2,14
"""


@pytest.fixture
def small_puzzle():
    return read_puzzle(lines.strip())


@pytest.fixture
def puzzle():
    with open("../inputs/input_day_07.txt") as f:
        return read_puzzle(f.readline())


def test_small_puzzle(small_puzzle):
    assert part_one(small_puzzle) == 37
    assert part_two(small_puzzle) == 168


def test_solution(puzzle):
    assert part_one(puzzle) == 356179
    assert part_two(puzzle) == 99788435
