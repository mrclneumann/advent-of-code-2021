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
def puzzle():
    return lines.strip().split("\n")


@pytest.fixture
def report(puzzle):
    return read_puzzle(puzzle)


def test_part_one(report):
    assert part_one(report) == 198


def test_part_two(report):
    assert part_two(report) == 230
