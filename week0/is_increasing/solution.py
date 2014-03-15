# returns True if 'seq' is an increasing sequence of numbers
def is_increasing(seq):
    for index in range(1, len(seq)):
        if seq[index - 1] >= seq[index]:
            return False
            
    return True