from src.aoc04 import count_rolls_of_paper, remove_rolls_of_paper

def read_sequence():
    "Reads a sequence of numbers from a file and returns them as a list of integers"
    with open('sequence', 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    print("Hello, Advent of Code Day 4!")
    sequence = read_sequence()
    result = remove_rolls_of_paper(sequence)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()