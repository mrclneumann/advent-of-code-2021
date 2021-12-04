from dataclasses import dataclass
from itertools import chain


@dataclass()
class Cell:
    value: int
    marked: bool


class Board:
    def __init__(self, board: list[list[int]]) -> None:
        self.board = [[Cell(x, False) for x in row] for row in board]
        self.last_drawn_number = None

    def __bool__(self):
        return any(
            all(cell.marked for cell in line)
            for line in chain(self._rows(), self._cols())
        )

    def _rows(self):
        yield from self.board

    def _cols(self):
        for col in range(len(self.board[0])):
            yield [self.board[i][col] for i in range(len(self.board))]

    def draw(self, number: int):
        self.last_drawn_number = number

        for row in self.board:
            for cell in row:
                if cell.value == number:
                    cell.marked = True

    def score(self):
        return (
            sum(cell.value for row in self.board for cell in row if not cell.marked)
            * self.last_drawn_number
        )


@dataclass
class Bingo:
    numbers: list[int]
    boards: list[Board]


def part_one(bingo: Bingo) -> int:
    for number in bingo.numbers:
        for board in bingo.boards:
            board.draw(number)

            if board:
                return board.score()


def part_two(bingo: Bingo) -> int:
    score = None

    for number in bingo.numbers:
        for board in bingo.boards:
            board.draw(number)

            if board:
                score = board.score()

        bingo.boards = [board for board in bingo.boards if not board]

    return score


def read_puzzle(lines: list[str]) -> Bingo:
    numbers = [int(x) for x in lines[0].strip().split(",")]

    boards = []
    for chunk in chunks(lines[1:], 6):
        boards.append(
            Board([[int(x) for x in line.strip().split()] for line in chunk[1:]])
        )

    return Bingo(numbers, boards)


def chunks(lines: list, n: int):
    for i in range(0, len(lines), n):
        yield lines[i : i + n]


if __name__ == "__main__":
    with open("../inputs/input_day_04.txt") as f:
        puzzle = read_puzzle(f.readlines())

    print(f"Part 1: {part_one(puzzle)}")
    print(f"Part 2: {part_two(puzzle)}")
