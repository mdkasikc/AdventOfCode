import itertools
import textwrap

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


def is_invalid_id_v2(number):
    """
    Checks if the given number is an invalid ID based on specific criteria.
    An invalid ID is defined if a sequence of digits is repeated at least twice consecutively.
    So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times),
    and 1111111 (1 seven times) are all invalid IDs.
    """
    id = str(number)
    for i in range(1, len(id) // 2 + 1):
        if len(set(textwrap.wrap(id, i))) == 1:
            return True
    return False


def get_invalid_ids(digit_range, version_2=False):
    """
    Counts the number of invalid digits in the given range.
    The range is expected to be a string of two integer for the starting and last index separated by a dash.
    The function returns a list of all the invalid IDs found in the range.
    """
    start_str, end_str = digit_range.split('-')
    start, end = int(start_str), int(end_str)
    invalid_ids = []

    for number in range(start, end + 1):
        if version_2:
            if is_invalid_id_v2(number):
                invalid_ids.append(number)
        else:
            if is_invalid_id(number):
                invalid_ids.append(number)

    return invalid_ids

def add_up_invalid_ids(ranges, version_2=False):
    """
    Takes a comma-separated string of ranges and returns the summed up invalid IDs.
    """
    total_invalid_ids = 0
    range_list = ranges.split(',')

    for digit_range in range_list:
        invalid_ids = get_invalid_ids(digit_range, version_2=version_2)
        total_invalid_ids += sum(invalid_ids)

    return total_invalid_ids