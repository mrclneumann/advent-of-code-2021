from itertools import permutations

digits = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

signals = "abcdefg"


def search(patterns: list[str]) -> dict[str, str]:
    return next(
        filter(
            lambda assignment: consistent(assignment, patterns),
            map(lambda segments: dict(zip(signals, segments)), permutations(signals)),
        )
    )


def consistent(assignment: dict[str, str], patterns: list[str]):
    return all(translate(pattern, assignment) in digits for pattern in patterns)


def translate(pattern: str, assignment: dict[str, str]) -> str:
    return "".join(sorted(pattern.translate(str.maketrans(assignment))))


def part_one(lines: list[list[str]]) -> int:
    return sum(len(pattern) in (2, 3, 4, 7) for line in lines for pattern in line[-4:])


def part_two(lines: list[list[str]]) -> int:
    total = 0

    for line in lines:
        patterns = line[:10]
        assignment = search(patterns)

        total += int(
            "".join(
                str(digits[translate(pattern, assignment)]) for pattern in line[-4:]
            )
        )

    return total


def read_puzzle(lines: list[str]) -> list[list[str]]:
    return [line.replace("|", "").strip().split() for line in lines]


if __name__ == "__main__":
    with open("../inputs/input_day_08.txt") as f:
        puzzle = read_puzzle(f.readlines())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
