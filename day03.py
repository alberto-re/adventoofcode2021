#!/usr/bin/env python3
# --- Day 3: Binary Diagnostic ---


from typing import Dict, List, Tuple
from copy import deepcopy

MOST_COMMON = 1
LEAST_COMMON = 0

EXAMPLE = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010\
"""


def lines_to_matrix(lines: List[str]) -> List[List[str]]:
    matrix = []
    for n, line in enumerate(lines):
        matrix.append([])
        for bit in list(line.rstrip()):
            matrix[n].append(bit)
    return matrix


def count_bits_by_position(report: List[List[str]]) -> List[Dict[str, int]]:
    bit_count = []
    for col in range(len(report[0])):
        bit_count.append({"0": 0, "1": 0})
        for row in range(len(report)):
            digit = report[row][col]
            bit_count[col][digit] += 1
    return bit_count


def compute_gamma_epsilon(bit_count: List[Dict[str, int]]) -> Tuple[str, str]:
    gamma, epsilon = "", ""
    for i in range(len(bit_count)):
        if bit_count[i]["0"] > bit_count[i]["1"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return gamma, epsilon


def compute_rating(report: List[List[str]], criteria: int) -> Tuple[str, str]:
    considered = deepcopy(report)
    for i in range(len(report[0])):
        bit_count = count_bits_by_position(considered)
        if bit_count[i]["0"] == bit_count[i]["1"]:
            filter_match = str(criteria)
        else:
            filter_match = sorted(bit_count[i].items(), key=lambda kv: kv[1])[criteria][
                0
            ]
        considered = list(filter(lambda x: x[i] == filter_match, considered))
        if len(considered) == 1:
            break
    return "".join(considered.pop())


report = lines_to_matrix(EXAMPLE.split("\n"))
assert len(report) == 12
assert len(report[0]) == 5

bit_count = count_bits_by_position(report)
assert bit_count[0]["0"] == 5
assert bit_count[0]["1"] == 7

gamma, epsilon = compute_gamma_epsilon(bit_count)

assert gamma == "10110"
assert epsilon == "01001"

power_consumption = int(gamma, base=2) * int(epsilon, base=2)
assert power_consumption == 198

oxygen_generator_rating = compute_rating(report, MOST_COMMON)
co2_scrubber_rating = compute_rating(report, LEAST_COMMON)

assert oxygen_generator_rating == "10111"
assert co2_scrubber_rating == "01010"

life_support_rating = int(oxygen_generator_rating, base=2) * int(
    co2_scrubber_rating, base=2
)
assert life_support_rating == 230


with open("input/day03.txt") as f:
    report = lines_to_matrix(f.readlines())

bit_count = count_bits_by_position(report)

gamma, epsilon = compute_gamma_epsilon(bit_count)
power_consumption = int(gamma, base=2) * int(epsilon, base=2)

print(f"Part one solution: {power_consumption}")

oxygen_generator_rating = compute_rating(report, MOST_COMMON)
co2_scrubber_rating = compute_rating(report, LEAST_COMMON)

life_support_rating = int(oxygen_generator_rating, base=2) * int(
    co2_scrubber_rating, base=2
)

print(f"Part two solution: {life_support_rating}")
