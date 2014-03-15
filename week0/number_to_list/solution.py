# returns list of the digits of 'n'
def number_to_list(n):  
    if n == 0:
        return []
    else:
        return number_to_list(n // 10) + [n % 10]