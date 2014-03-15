# returns list of the digits of 'n'
def number_to_list(n):  
    if n == 0:
        return []
    else:
        return number_to_list(n // 10) + [n % 10]

# returns True if 'n' is a palindrom
def is_int_palindrom(n):
    reversed = number_to_list(n)
    reversed.reverse()

    if reversed == number_to_list(n):
        return True

    return False