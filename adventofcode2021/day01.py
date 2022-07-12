#!/usr/bin/env python3
# --- Day 1: Sonar Sweep ---

from typing import List


def count_increments(depths: List[int]) -> int:
    return sum([depths[i] > depths[i - 1] for i in range(1, len(depths))])


def sliding_windows(series: List[int], size: int = 3) -> List[int]:
    return [sum(series[i : i + size]) for i in range(len(series) - size + 1)]


def main():
    with open("input/day01.txt") as f:
        lines = [int(line.rstrip()) for line in f]

    print(f"Part one solution: {count_increments(lines)}")
    print(f"Part two solution: {count_increments(sliding_windows(lines))}")


if __name__ == "__main__":
    main()
