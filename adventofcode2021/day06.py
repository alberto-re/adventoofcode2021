#!/usr/bin/env python3
# --- Day 6: Lanternfish ---
from copy import deepcopy
from typing import List

EXAMPLE = "3,4,3,1,2"


def timers_from_input(puzzle_input: str) -> List[int]:
    return list(map(int, puzzle_input.split(",")))


timers = timers_from_input(EXAMPLE)
assert timers == [3, 4, 3, 1, 2], timers


def timetravel(timers: List[int], days: int = 1) -> List[int]:
    new_timers = deepcopy(timers)
    for _ in range(days):
        to_add = 0
        for index, value in enumerate(new_timers):
            new_timers[index] -= 1
            if value == 0:
                to_add += 1
                new_timers[index] = 6
        for _ in range(to_add):
            new_timers.append(8)
    return new_timers


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


def timetravel_optimized(starting_population: List[int], days: int = 1) -> int:
    population_size = len(starting_population)
    steps = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in starting_population:
        steps[fish] += 1
    for _ in range(days):
        to_add = steps[0]
        for i in range(8):
            steps[i] = steps[i + 1]
            steps[i + 1] = 0
        steps[6] += to_add
        steps[8] += to_add
        population_size += to_add

    return population_size


timers = timers_from_input(EXAMPLE)

fish_count = timetravel_optimized(timers, days=1)
assert fish_count == 5, fish_count
fish_count = timetravel_optimized(timers, days=2)
assert fish_count == 6, fish_count
fish_count = timetravel_optimized(timers, days=3)
assert fish_count == 7, fish_count
fish_count = timetravel_optimized(timers, days=4)
assert fish_count == 9, fish_count
fish_count = timetravel_optimized(timers, days=5)
assert fish_count == 10, fish_count
fish_count = timetravel_optimized(timers, days=8)
assert fish_count == 10, fish_count
fish_count = timetravel_optimized(timers, days=18)
assert fish_count == 26, fish_count
fish_count = timetravel_optimized(timers, days=80)
assert fish_count == 5934, fish_count
fish_count = timetravel_optimized(timers, days=256)
assert fish_count == 26984457539, fish_count


def main():
    with open("input/day06.txt") as f:
        puzzle_input = f.read()

    timers = timers_from_input(puzzle_input)
    timers = timetravel(timers, days=80)

    print(f"Part one solution: {len(timers)}")

    timers = timers_from_input(puzzle_input)
    print(f"Part two solution: {timetravel_optimized(timers, days=256)}")


if __name__ == "__main__":
    main()
