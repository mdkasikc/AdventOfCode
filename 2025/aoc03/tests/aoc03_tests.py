import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.aoc03 import get_highest_joltage_part1, get_highest_joltage_part2

def test_get_highest_joltage():
    first_sequence = "987654321111111"
    highest_joltage = get_highest_joltage_part1(first_sequence)
    assert highest_joltage == 98

    second_sequence = "811111111111119"
    highest_joltage = get_highest_joltage_part1(second_sequence)
    assert highest_joltage ==  89

    third_sequence = "234234234234278"
    highest_joltage = get_highest_joltage_part1(third_sequence)
    assert highest_joltage ==  78

    fourth_sequence = "818181911112111"
    highest_joltage = get_highest_joltage_part1(fourth_sequence)
    assert highest_joltage ==  92


def test_get_highest_joltage_part2 ():
    first_sequence = "987654321111111"
    highest_joltage = get_highest_joltage_part2(first_sequence)
    assert highest_joltage ==  987654321111

    second_sequence = "811111111111119"
    highest_joltage = get_highest_joltage_part2(second_sequence)
    assert highest_joltage ==  811111111119

    third_sequence = "234234234234278"
    highest_joltage = get_highest_joltage_part2(third_sequence)
    assert highest_joltage ==  434234234278

    fourth_sequence = "818181911112111"
    highest_joltage = get_highest_joltage_part2(fourth_sequence)
    assert highest_joltage ==  888911112111