#!/usr/bin/env python3
# --- Day 7: The Treachery of Whales ---
from typing import List

EXAMPLE = "16,1,2,0,4,2,7,1,2,14"

EXAMPLE_KNOWN_COSTS = [(2, 37), (1, 41), (3, 39), (10, 71)]


def positions_from_input(puzzle_input: str) -> List[int]:
    return list(map(int, puzzle_input.split(",")))


initial_positions = positions_from_input(EXAMPLE)
assert initial_positions == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], initial_positions


def alignment_cost(position_to_align: int, positions: List[int]) -> int:
    return sum([abs(p - position_to_align) for p in positions])


for position, cost_exp in EXAMPLE_KNOWN_COSTS:
    cost = alignment_cost(position, initial_positions)
    assert cost == cost_exp, cost


def minimize_cost(positions: List[int]) -> int:
    mincost = 99999999
    for pos in range(len(positions)):
        cost = alignment_cost(pos, positions)
        if cost < mincost:
            mincost = cost
    return mincost


min_cost = minimize_cost(initial_positions)
assert min_cost == EXAMPLE_KNOWN_COSTS[0][1], min_cost


def main():
    with open("input/day07.txt") as f:
        puzzle_input = f.read()

    initial_positions = positions_from_input(puzzle_input)
    min_cost = minimize_cost(initial_positions)

    print(f"Part one solution: {min_cost}")


if __name__ == "__main__":
    main()
