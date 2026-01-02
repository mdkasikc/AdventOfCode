import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.aoc04 import count_rolls_of_paper, remove_rolls_of_paper

TEST_INPUT = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

def test_count_rolls_of_paper():
    result = count_rolls_of_paper(TEST_INPUT)
    assert result == 13

def test_count_removed_rolls_of_paper():
    result = remove_rolls_of_paper(TEST_INPUT)
    assert result == 43