from collections import namedtuple

Instruction = namedtuple("Instruction", ["command", "units"])


class Submarine:
    def __init__(self) -> None:
        self.horizontal_position: int = 0
        self.depth: int = 0

    def forward(self, units: int):
        self.horizontal_position += units

    def down(self, units: int):
        self.depth += units

    def up(self, units: int):
        self.depth -= units


class AimSubmarine(Submarine):
    def __init__(self) -> None:
        super().__init__()
        self.aim = 0

    def forward(self, units: int):
        super(AimSubmarine, self).forward(units)
        self.depth += self.aim * units

    def down(self, units: int):
        self.aim += units

    def up(self, units: int):
        self.aim -= units


def part_one(instructions: list[Instruction]) -> int:
    return interpret(instructions, Submarine())


def part_two(instructions: list[Instruction]) -> int:
    return interpret(instructions, AimSubmarine())


def interpret(instructions: list[Instruction], ship: Submarine) -> int:
    for command, units in instructions:
        getattr(ship, command)(units)

    return ship.horizontal_position * ship.depth


def read_puzzle(lines: list[str]) -> list[Instruction]:
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> Instruction:
    command, units = line.strip().split()
    return Instruction(command, int(units))


if __name__ == "__main__":
    with open("../inputs/input_day_02.txt") as f:
        puzzle = read_puzzle(f.readlines())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
