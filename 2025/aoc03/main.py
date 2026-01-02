from src.aoc03 import get_highest_joltage_part1, get_highest_joltage_part2

def read_sequence():
    "Reads a sequence of numbers from a file and returns them as a list of integers"
    with open('sequence', 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    print("Hello, Advent of Code Day 3!")
    sequence = read_sequence()
    combined_joltage = 0
    for seq in sequence:
        highest_joltage = get_highest_joltage_part2(seq)
        combined_joltage += highest_joltage
    print(f"The combined highest joltage from all sequences is: {combined_joltage}")

if __name__ == "__main__":
    main()