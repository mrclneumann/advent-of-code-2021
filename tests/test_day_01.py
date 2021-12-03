import pytest

from aoc.day_01 import part_01, part_02


@pytest.fixture
def report():
    f = """
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

    return [row.strip() for row in f.split()]


def test_part_01(report):
    assert part_01(report) == 7


def test_part_02(report):
    assert part_02(report) == 5
