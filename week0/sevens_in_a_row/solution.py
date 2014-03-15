# returns True if 'arr' has at least 'n' consecutive sevens
def sevens_in_a_row(arr, n):
    consecutive = 0

    for number in arr:
        if number == 7:
            consecutive += 1
        elif consecutive >= n:
            return True
        else:
            consecutive = 0

    return False