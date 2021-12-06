import pytest

from advent.day_06 import part_one, part_two, read_puzzle

lines = """
3,4,3,1,2
"""


@pytest.fixture
def small_puzzle():
    return read_puzzle(lines.strip())


@pytest.fixture
def puzzle():
    with open("../inputs/input_day_06.txt") as f:
        return read_puzzle(f.readline())


def test_small_puzzle(small_puzzle):
    assert part_one(small_puzzle) == 5934
    assert part_two(small_puzzle) == 26984457539


def test_solution(puzzle):
    assert part_one(puzzle) == 372984
    assert part_two(puzzle) == 1681503251694
