# returns the number of consonants in 'str'
def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0

    for char in str:
        if char.lower() in consonants:
            count += 1

    return count
#   short way:
#   len([char for char in str if char.lower() in consonants])