# returns the biggest difference between any two numbers in 'arr'
def biggest_difference(arr):
    if len(arr) == 0:
        return 0
        
    return min(arr) - max(arr)