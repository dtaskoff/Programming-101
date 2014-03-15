from collections import defaultdict

# returns a dictionary of the following kind:
# {"word" : count (= occurrences in 'arr')}
def count_words(arr):
    counts = {}
# using defaultdict to avoid checking if
# key is in the dictionary 'counts' or not
    counts = defaultdict(lambda: 0)
    for word in arr:
            counts[word] += 1

    return dict(counts)

# returns the number of different words in 'arr'
def unique_words_count(arr):
    dict = count_words(arr)
    return len(dict.keys())