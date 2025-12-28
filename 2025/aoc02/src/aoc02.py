def is_invalid_id(number):
    """
    Checks if the given number is an invalid ID based on specific criteria.
    An invalid ID is defined as one where only some sequence of digits is repeated twice.
    """
    num_str = str(number)
    length = len(num_str)
    if(length % 2 != 0):
        return False

    if num_str[:length // 2] == num_str[length // 2:]:
        return True

    return False

def get_invalid_ids(digit_range):
    """
    Counts the number of invalid digits in the given range.
    The range is expected to be a string of two integer for the starting and last index separated by a dash.
    The function returns a list of all the invalid IDs found in the range.
    """
    start_str, end_str = digit_range.split('-')
    start, end = int(start_str), int(end_str)
    invalid_ids = []

    for number in range(start, end + 1):
        if is_invalid_id(number):
            invalid_ids.append(number)

    return invalid_ids

def add_up_invalid_ids(ranges):
    """
    Takes a comma-separated string of ranges and returns the summed up invalid IDs.
    """
    total_invalid_ids = 0
    range_list = ranges.split(',')

    for digit_range in range_list:
        invalid_ids = get_invalid_ids(digit_range)
        total_invalid_ids += sum(invalid_ids)

    return total_invalid_ids