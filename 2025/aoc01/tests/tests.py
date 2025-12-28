import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.aoc01 import count_zeros

TEST_INPUT = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

def test__part_1__example():
    assert count_zeros(TEST_INPUT, False) == 3


def test__part_2__example():
    assert count_zeros(TEST_INPUT, True) == 6