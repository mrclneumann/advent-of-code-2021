import pytest

from advent.day_02 import part_one, part_two, read_puzzle

lines = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@pytest.fixture
def small_puzzle():
    return lines.strip().split("\n")


@pytest.fixture
def instructions(small_puzzle):
    return read_puzzle(small_puzzle)


@pytest.fixture
def puzzle():
    with open("../inputs/input_day_02.txt") as f:
        return read_puzzle(f.readlines())


def test_small_puzzle(instructions):
    assert part_one(instructions) == 150
    assert part_two(instructions) == 900


def test_solution(puzzle):
    assert part_one(puzzle) == 2272262
    assert part_two(puzzle) == 2134882034
