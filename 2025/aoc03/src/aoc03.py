def get_highest_joltage_part1(sequence):
    """
    Iterates through a sequence of integers represented as a string and finds the two
    highest integers which combined equal the maximum possible sum. The sequence is
    obsererved doing so. It returns the combined integer as one integer.
    
    :param sequence: A string of integers without separation.
    """
    highest_joltage = -1

    for i, first_digit in enumerate(sequence):
        for second_number in sequence[i+1:]:
            combined_joltage = int(first_digit + second_number)
            if combined_joltage > highest_joltage:
                highest_joltage = combined_joltage
    
    return highest_joltage
            
def get_highest_joltage_part2(sequence):
    """
    Iterates through a sequence of integers represented as a string and finds the the twolve digits
    which combined equal the maximum possible sum. During the iteration, the sequence is observed.
    It returns the combined integer as one integer.
    
    :param sequence: A string of integers without separation.
    """
    highest_joltage = -1

    list_of_digits = list(map(int, sequence))
    last_index = -11
    current_index = 0
    list_of_highest_digits = []

    while last_index <= 0:
        if last_index == 0:
            sliced_digits = list_of_digits[current_index:]
        else:
            sliced_digits = list_of_digits[current_index:last_index]
        max_digit = max(sliced_digits)
        sliced_index = sliced_digits.index(max_digit)
        current_index += sliced_index + 1
        list_of_highest_digits.append(max_digit)
        last_index += 1

    highest_joltage = int(''.join(map(str, list_of_highest_digits)))
    return highest_joltage