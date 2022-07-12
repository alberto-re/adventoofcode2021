#!/usr/bin/env python3
# --- Day 2: Dive! ---


from typing import List, Tuple


def follow_planned_course(
    course: List[Tuple[str, int]], hp: int = 0, depth: int = 0, track_aim: bool = False
) -> Tuple[int, int]:
    aim = 0
    for action, qty in course:
        if action == "forward":
            if track_aim:
                hp += qty
                depth += aim * qty
            else:
                hp += qty
        elif action == "up":
            if track_aim:
                aim -= qty
            else:
                depth -= qty
        else:
            if track_aim:
                aim += qty
            else:
                depth += qty
    return hp, depth


def main():
    with open("input/day02.txt") as f:
        course = [
            (line.rstrip().split()[0], int(line.rstrip().split()[1])) for line in f
        ]

    hp, depth = follow_planned_course(course)

    print(f"Part one solution: {hp * depth}")

    hp, depth = follow_planned_course(course, track_aim=True)

    print(f"Part two solution: {hp * depth}")


if __name__ == "__main__":
    main()
