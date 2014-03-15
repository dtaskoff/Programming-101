# returns True if 'needle' is member of the Fibonacci list sequence
# where the first and second list are respectively 'listA' and 'listB'
def member_of_nth_fib_lists(listA, listB, needle):
    while len(needle) > len(listA):
        listA, listB = listB, listA + listB
    return listA == needle