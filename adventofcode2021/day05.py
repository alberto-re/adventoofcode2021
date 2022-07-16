#!/usr/bin/env python3
# --- Day 5: Hydrothermal Venture ---

from collections import defaultdict
from typing import Dict, List, Set, Tuple

EXAMPLE = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2\
"""

EXAMPLE_DIAGRAM = """\
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....\
"""

EXAMPLE_DIAGRAM_PART2 = """\
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....\
"""

DIAGRAM_SHAPE = (10, 10)


def lines_from_input(puzzle_input: str) -> List[List[int]]:
    lines = []
    for row in puzzle_input.split("\n"):
        start, _, end = row.split()
        line = []
        line.extend(start.split(","))
        line.extend(end.split(","))
        lines.append(list(map(int, line)))
    return lines


def points_from_line(
    line: List[int], include_diagonals: bool = False
) -> Set[Tuple[int, int]]:
    points: Set[Tuple[int, int]] = set()
    x1, y1, x2, y2 = line

    if x1 != x2 and y1 != y2 and not include_diagonals:
        return points

    if x2 >= x1:
        xs = [x for x in range(x1, x2 + 1)]
    else:
        xs = list(reversed([x for x in range(x2, x1 + 1)]))

    if y2 >= y1:
        ys = [y for y in range(y1, y2 + 1)]
    else:
        ys = list(reversed([y for y in range(y2, y1 + 1)]))

    if len(xs) > len(ys):
        ys = [y1 for _ in range(len(xs))]
    if len(ys) > len(xs):
        xs = [x1 for _ in range(len(ys))]

    for x, y in zip(xs, ys):
        points.add((x, y))

    return points


points = points_from_line([1, 1, 3, 1])
assert points == {(1, 1), (2, 1), (3, 1)}, points
points = points_from_line([3, 1, 1, 1])
assert points == {(1, 1), (2, 1), (3, 1)}, points
points = points_from_line([2, 5, 7, 5])
assert points == {(2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)}, points
points = points_from_line([7, 5, 2, 5])
assert points == {(2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)}, points
points = points_from_line([1, 1, 3, 3])
assert points == set(), points
points = points_from_line([1, 1, 3, 3], include_diagonals=True)
assert points == {(1, 1), (2, 2), (3, 3)}, points
points = points_from_line([3, 3, 1, 1], include_diagonals=True)
assert points == {(1, 1), (2, 2), (3, 3)}, points
points = points_from_line([8, 0, 0, 8], include_diagonals=True)
assert points == {
    (8, 0),
    (7, 1),
    (6, 2),
    (5, 3),
    (4, 4),
    (3, 5),
    (2, 6),
    (1, 7),
    (0, 8),
}, points


def diagram_from_lines(
    lines: List[List[int]], include_diagonals: bool = False
) -> Dict[Tuple[int, int], int]:
    diagram: Dict[Tuple[int, int], int] = defaultdict(int)
    for line in lines:
        points = points_from_line(line, include_diagonals)
        for point in points:
            diagram[point] += 1
    return diagram


diagram = diagram_from_lines([[1, 1, 3, 1], [2, 5, 7, 5]])
assert diagram == {
    (1, 1): 1,
    (2, 1): 1,
    (3, 1): 1,
    (2, 5): 1,
    (3, 5): 1,
    (4, 5): 1,
    (5, 5): 1,
    (6, 5): 1,
    (7, 5): 1,
}, diagram
diagram = diagram_from_lines([[3, 1, 1, 1], [7, 5, 2, 5]])
assert diagram == {
    (1, 1): 1,
    (2, 1): 1,
    (3, 1): 1,
    (2, 5): 1,
    (3, 5): 1,
    (4, 5): 1,
    (5, 5): 1,
    (6, 5): 1,
    (7, 5): 1,
}, diagram
diagram = diagram_from_lines(
    [[3, 1, 1, 1], [7, 5, 2, 5], [4, 4, 8, 8]], include_diagonals=True
)
assert diagram == {
    (1, 1): 1,
    (2, 1): 1,
    (3, 1): 1,
    (2, 5): 1,
    (3, 5): 1,
    (4, 5): 1,
    (5, 5): 2,
    (6, 5): 1,
    (7, 5): 1,
    (4, 4): 1,
    (6, 6): 1,
    (7, 7): 1,
    (8, 8): 1,
}, diagram


def diagram_repr(diagram: Dict[Tuple[int, int], int]) -> str:
    text = ""
    for y in range(DIAGRAM_SHAPE[1]):
        for x in range(DIAGRAM_SHAPE[0]):
            occurrences = str(diagram[(x, y)])
            if occurrences == "0":
                occurrences = "."
            text += occurrences
        if y < DIAGRAM_SHAPE[1] - 1:
            text += "\n"
    return text


def main():
    lines = lines_from_input(EXAMPLE)

    diagram = diagram_from_lines(lines)
    assert diagram_repr(diagram) == EXAMPLE_DIAGRAM, diagram_repr(diagram)
    assert len([overlaps for overlaps in diagram.values() if overlaps > 1]) == 5

    diagram = diagram_from_lines(lines, include_diagonals=True)
    assert diagram_repr(diagram) == EXAMPLE_DIAGRAM_PART2, diagram_repr(diagram)

    with open("input/day05.txt") as f:
        puzzle_input = f.read()

    lines = lines_from_input(puzzle_input)

    diagram = diagram_from_lines(lines)
    overlaps = len([overlaps for overlaps in diagram.values() if overlaps > 1])
    print(f"Part one solution: {overlaps}")

    diagram = diagram_from_lines(lines, include_diagonals=True)
    overlaps = len([overlaps for overlaps in diagram.values() if overlaps > 1])
    print(f"Part two solution: {overlaps}")


if __name__ == "__main__":
    main()
