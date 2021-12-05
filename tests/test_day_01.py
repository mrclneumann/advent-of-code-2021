import pytest

from advent.day_01 import part_one, part_two, read_puzzle

lines = """
199
200
208
210
200
207
240
269
260
263
"""


@pytest.fixture
def small_puzzle():
    return read_puzzle(lines.strip().split("\n"))


@pytest.fixture
def puzzle():
    with open("../inputs/input_day_01.txt") as f:
        return read_puzzle(f.readlines())


def test_small_puzzle(small_puzzle):
    assert part_one(small_puzzle) == 7
    assert part_two(small_puzzle) == 5


def test_solution(puzzle):
    assert part_one(puzzle) == 1228
    assert part_two(puzzle) == 1257
