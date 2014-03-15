# returns True if 'seq' is a decreasing sequence of numbers
def is_decreasing(seq):
    for index in range(1, len(seq)):
        if seq[index - 1] <= seq[index]:
            return False

    return True