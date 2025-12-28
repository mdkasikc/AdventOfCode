from src.aoc01 import count_zeros

def read_sequence():
    "Reads a sequence of numbers from a file and returns them as a list of integers"
    with open('sequence', 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    print("Hello, Advent of Code!")
    sequence = read_sequence()
    zeros = count_zeros(sequence, True)
    print(f"Number of zeros in the sequence: {zeros}")

if __name__ == "__main__":
    main()