# returns True if 'word' is in "a"^n"b"^n form (n > 0)
def is_an_bn(word):
    ays_and_bees = word.split('ab')
    bees_and_ays = word.split('ba')
    
    return len(ays_and_bees) == 2 and len(bees_and_ays) == 1 and \
        len(ays_and_bees[0]) == len(ays_and_bees[1])