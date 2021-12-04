from typing import Callable

import pandas as pd


def part_one(df: pd.DataFrame) -> int:
    return gamma_rate(df) * epsilon_rate(df)


def part_two(df: pd.DataFrame) -> int:
    return oxygen_generator_rating(df) * co2_scrubber_rating(df)


def gamma_rate(df: pd.DataFrame) -> int:
    return bits_to_int(df.mode().iloc[0])


def epsilon_rate(df: pd.DataFrame) -> int:
    return bits_to_int(1 - df.mode().iloc[0])


def oxygen_generator_rating(df: pd.DataFrame) -> int:
    return select_by_bit_criteria(df, most_common)


def co2_scrubber_rating(df: pd.DataFrame) -> int:
    return select_by_bit_criteria(df, least_common)


def select_by_bit_criteria(
    df: pd.DataFrame, criteria: Callable[[pd.Series], int]
) -> int:
    for col in df.columns:
        df = df[df[col] == criteria(df[col])]

    return bits_to_int(df.iloc[0])


def bits_to_int(s: pd.Series) -> int:
    return int("".join(s.astype(str).tolist()), 2)


def most_common(s: pd.Series) -> int:
    mode = s.mode()
    return 1 if len(mode) > 1 else mode.iloc[0]


def least_common(s: pd.Series) -> int:
    return s.iloc[0] if len(s) == 1 else 1 - most_common(s)


def read_puzzle(lines: list[str]) -> pd.DataFrame:
    return pd.DataFrame([parse_line(line) for line in lines])


def parse_line(line: str) -> list[int]:
    return [int(x) for x in line.strip()]


if __name__ == "__main__":
    with open("../inputs/input_day_03.txt") as f:
        puzzle = read_puzzle(f.readlines())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
