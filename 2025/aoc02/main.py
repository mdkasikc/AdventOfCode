from src.aoc02 import add_up_invalid_ids

def read_sequence():
    with open("sequence", "r") as file:
        sequence = file.read().strip()
    return sequence

def main():
    print("Hello, Advent of Code Day 2!")
    sequence = read_sequence()
    sum_invalid_ids = add_up_invalid_ids(sequence, version_2=True)
    print(f"The sum of all invalid IDs is: {sum_invalid_ids}")

if __name__ == "__main__":
    main()