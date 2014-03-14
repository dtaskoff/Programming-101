def number_to_list(n):  
    if n == 0:
        return []
    else:
        return number_to_list(n // 10) + [n % 10]

# returns True if 'digit' is present in 'number'
def contains_digit(number, digit):
    return digit in number_to_list(number)