import pytest

from aoc.day_02 import part_one, part_two, read_puzzle

lines = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@pytest.fixture
def puzzle():
    return lines.strip().split("\n")


@pytest.fixture
def instructions(puzzle):
    return read_puzzle(puzzle)


def test_part_one(instructions):
    assert part_one(instructions) == 150


def test_part_two(instructions):
    assert part_two(instructions) == 900
