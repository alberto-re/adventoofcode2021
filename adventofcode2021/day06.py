#!/usr/bin/env python3
# --- Day 6: Lanternfish ---
from typing import List

EXAMPLE = "3,4,3,1,2"


def timers_from_input(puzzle_input: str) -> List[int]:
    return list(map(int, puzzle_input.split(",")))


timers = timers_from_input(EXAMPLE)
assert timers == [3, 4, 3, 1, 2], timers


def timetravel(timers: List[int], days: int = 1) -> List[int]:
    for _ in range(days):
        to_add = 0
        for index, value in enumerate(timers):
            timers[index] -= 1
            if value == 0:
                to_add += 1
                timers[index] = 6
        for _ in range(to_add):
            timers.append(8)
    return timers


timers = timetravel(timers)
assert timers == [2, 3, 2, 0, 1], timers
timers = timetravel(timers)
assert timers == [1, 2, 1, 6, 0, 8], timers
timers = timetravel(timers)
assert timers == [0, 1, 0, 5, 6, 7, 8], timers
timers = timetravel(timers)
assert timers == [6, 0, 6, 4, 5, 6, 7, 8, 8], timers
timers = timetravel(timers, days=14)
assert timers == [
    6,
    0,
    6,
    4,
    5,
    6,
    0,
    1,
    1,
    2,
    6,
    0,
    1,
    1,
    1,
    2,
    2,
    3,
    3,
    4,
    6,
    7,
    8,
    8,
    8,
    8,
], timers

assert len(timers) == 26, len(timers)
timers = timetravel(timers, days=62)
assert len(timers) == 5934, len(timers)


def main():
    with open("input/day06.txt") as f:
        puzzle_input = f.read()

    timers = timers_from_input(puzzle_input)
    timers = timetravel(timers, days=80)

    print(f"Part one solution: {len(timers)}")


if __name__ == "__main__":
    main()
