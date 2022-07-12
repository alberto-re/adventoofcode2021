#!/usr/bin/env python3
# --- Day 4: Giant Squid ---

from typing import List, Tuple

EXAMPLE = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7\
"""


class Board:
    def __init__(self, numbers: List[List[int]]) -> None:
        self._numbers = numbers
        self._rows, self._cols = self._rows_cols(numbers)

    @staticmethod
    def _rows_cols(numbers: List[List[int]]) -> Tuple[List[List[int]], List[List[int]]]:
        rows = []
        cols = []
        for row in numbers:
            rows.append(row)
        for i in range(len(rows)):
            cols.append([row[i] for row in rows])
        return rows, cols

    def check(self, number: int) -> bool:
        wins = False
        for row in self._rows:
            try:
                row.remove(number)
            except ValueError:
                pass
            if len(row) == 0:
                wins = True
        for col in self._cols:
            try:
                col.remove(number)
            except ValueError:
                pass
            if len(col) == 0:
                wins = True
        return wins

    def unmarked(self) -> List[int]:
        numbers = []
        for row in self._rows:
            for value in row:
                numbers.append(value)
        for col in self._cols:
            for value in col:
                numbers.append(value)
        return list(set(numbers))

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Board):
            return self._numbers == __o._numbers
        else:
            return False


def numbers_from_input(puzzle_input: str) -> List[int]:
    return list(map(int, puzzle_input.split("\n")[0].split(",")))


def boards_from_input(puzzle_input: str) -> list:  # TODO: narrow return type
    lines = puzzle_input.split("\n")[2:]
    boards = []
    board = []
    for line in lines:
        if line:
            board.append(list(map(int, line.split())))
        else:
            boards.append(Board(board))
            board = []
    else:
        boards.append(Board(board))
    return boards


def first_to_win(numbers: List[int], boards: List[Board]) -> Tuple[int, List[int]]:
    for number in numbers:
        for board in boards:
            if board.check(number):
                return number, board.unmarked()
    return -1, []


def last_to_win(numbers: List[int], boards: List[Board]) -> Tuple[int, List[int]]:
    last_number, unmarked = 0, []
    checked = []
    for number in numbers:
        for index, board in enumerate(boards):
            if index in checked:
                continue
            if board.check(number):
                last_number, unmarked = number, board.unmarked()
                checked.append(index)
    return last_number, unmarked


def main():
    numbers = numbers_from_input(EXAMPLE)
    assert numbers == [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]

    boards = boards_from_input(EXAMPLE)
    assert len(boards) == 3
    assert boards[0] == Board(
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ]
    )
    assert boards[1] == Board(
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ]
    )

    assert boards[2] == Board(
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ]
    )

    winning_board, unmarked = first_to_win(numbers, boards)
    assert winning_board * sum(unmarked) == 4512

    winning_board, unmarked = last_to_win(numbers, boards)
    assert winning_board * sum(unmarked) == 1924

    with open("input/day04.txt") as f:
        puzzle_input = f.read()

    numbers = numbers_from_input(puzzle_input)
    boards = boards_from_input(puzzle_input)

    winning_board, unmarked = first_to_win(numbers, boards)
    print(f"Part one solution: {winning_board * sum(unmarked)}")

    boards = boards_from_input(puzzle_input)

    winning_board, unmarked = last_to_win(numbers, boards)
    print(f"Part two solution: {winning_board * sum(unmarked)}")


if __name__ == "__main__":
    main()
