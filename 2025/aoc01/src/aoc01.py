def rotate_left(prev_position, number):
    "Subtract the number from the prev_position until it reaches zero, then start again at 99. Count the number of rotations."
    spins = number // 100
    rotations = number % 100
    current_position = prev_position - rotations
    if prev_position != 0 and current_position // 100 != 0:
        spins += 1
    current_position %= 100
    return (current_position, spins)

def rotate_right(prev_position, number):
    "Add the number to the prev_position until it reaches 99, then calculate modulo 100. Count the number of rotations."
    spins = number // 100
    rotations = number % 100
    current_position = prev_position + rotations
    if (prev_position != 0 and current_position != 100) and current_position // 100 != 0:
        spins += 1
    current_position %= 100    
    return (current_position, spins)

def count_zeros(sequence, count_rotations=False):
    "Counts the number of zeros after each rotation operation in the sequence. A sequence looks like: 'L10', 'R20', etc."
    position = 50
    zeros = 0
    spins = 0
    for seq in sequence:
        if seq.startswith('L'):
            position, left_spins = rotate_left(position, int(seq[1:]))
            spins += left_spins
        elif seq.startswith('R'):
            position, right_spins = rotate_right(position, int(seq[1:]))
            spins += right_spins
        if position == 0:
            zeros += 1
    if count_rotations:
        zeros += spins
    return zeros