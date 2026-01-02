def count_rolls_of_paper(rolls_list):
    """
    Counts the number of rolls of paper which have fewer than 4 rolls of paper in the eight
    adjacent positions (horizontally, vertically, and diagonally). A role of paper is
    represented by the "@" character. No role is represented by the "." character.
    
    :param rolls_list: List of strings representing rolls of paper
    """
    removable_indices = get_indices_of_rolls_to_remove(rolls_list)
    count = len(removable_indices)
    return count

def remove_rolls_of_paper(rolls_list):
    """
    Removes rolls of paper from the rolls_list which have fewer than 4 rolls of paper in the
    eight adjacent positions (horizontally, vertically, and diagonally). This process is done
    iteratively until no more rolls of paper can be removed. The amount of removed rolls is
    counted and returned. A role of paper is represented by the "@" character. No role is
    represented by the "." character.
    
    :param rolls_list: List of strings representing rolls of paper
    :return: The amount of removed rolls of paper
    """
    total_removed = 0
    while True:
        removable_indices = get_indices_of_rolls_to_remove(rolls_list)
        if not removable_indices:
            break
        total_removed += len(removable_indices)
        for i, j in removable_indices:
            rolls_list[i] = rolls_list[i][:j] + '.' + rolls_list[i][j+1:]
    return total_removed

def get_indices_of_rolls_to_remove(rolls_list):
    """
    Returns a list of tuples representing the indices of rolls of paper in the rolls_list
    which can be removed. A removeable roll of paper is defined as one that has fewer than 4
    rolls of paper in the eight adjacent positions (horizontally, vertically, and diagonally).
    A roll of paper is represented by the "@" character. No roll is represented by the "." character.
    
    :param rolls_list: List of strings representing rolls of paper
    :return: List of tuples (i, j) where rolls_list[i][j] == '@'
    """
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    def is_valid(x, y):
        return 0 <= x < len(rolls_list) and 0 <= y < len(rolls_list[0])
    
    removable_indices = []
    for i in range(len(rolls_list)):
        for j in range(len(rolls_list[0])):
            if rolls_list[i][j] == '@':
                adjacent_count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if is_valid(ni, nj) and rolls_list[ni][nj] == '@':
                        adjacent_count += 1
                if adjacent_count < 4:
                    removable_indices.append((i, j))
    return removable_indices