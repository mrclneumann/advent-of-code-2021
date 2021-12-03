import pytest

from aoc.day_01 import part_one, part_two, read_puzzle

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
def puzzle():
    return lines.strip().split("\n")


@pytest.fixture
def report(puzzle):
    return read_puzzle(puzzle)


def test_part_one(report):
    assert part_one(report) == 7


def test_part_two(report):
    assert part_two(report) == 5
