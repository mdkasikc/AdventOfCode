def read_sequence():
    "Reads a sequence of numbers from a file and returns them as a list of integers"
    with open('sequence', 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def rotate_left(value, amount):
    "Subtract the amount from the value until it reaches zero, then start again at 99."
    result = value - amount
    if result < 0:
        result %= 100
    return result

def rotate_right(value, amount):
    "Add the amount to the value until it reaches 99, then calculate modulo 100."
    result = value + amount
    if result > 99:
        result %= 100
    return result

def count_zeros(sequence):
    "Counts the number of zeros after each rotation operation in the sequence. A sequence looks like: 'L10', 'R20', etc."
    starting_value = 50
    zeros = 0
    for seq in sequence:
        if seq.startswith('L'):
            starting_value = rotate_left(starting_value, int(seq[1:]))
        elif seq.startswith('R'):
            starting_value = rotate_right(starting_value, int(seq[1:]))
        if starting_value == 0:
            zeros += 1
    return zeros

def main():
    "Entrance point of the program"
    sequence = read_sequence()
    zeros = count_zeros(sequence)
    print("Hello, Advent of Code!")
    print(f"Number of zeros in the sequence: {zeros}")

if __name__ == "__main__":
    main()
