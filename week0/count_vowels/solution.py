# returns the number of vowels in 'str'
def count_vowels(str):
    vowels = "aeouiy"
    count = 0

    for char in str:
        if char.lower() in vowels:
            count += 1

    return count
#   short way:
#   return len([char for char in str if char.lower() in vowels])