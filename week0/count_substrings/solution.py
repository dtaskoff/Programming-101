# returns all occurrences of 'needle' in 'haystack'
def count_substrings(haystack, needle):
    count = 0
    needle_size = len(needle)
    haystack_size = len(haystack)

    i = 0
    while i < haystack_size:
        if haystack[i : (i + needle_size)] == needle:
            count += 1
            i += needle_size
        else:
            i += 1

    return count