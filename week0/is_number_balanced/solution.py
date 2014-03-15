# returns list of the digits of 'n'
def number_to_list(n):  
    if n == 0:
        return []
    else:
        return number_to_list(n // 10) + [n % 10]

# returns True if 'n' is balanced (i. e. has equal
# sums of digits from left and right parts:
# 1379209, 'cause 1 + 3 + 7 = 2 + 0 + 9)
def is_number_balanced(n):
    number = number_to_list(n)
    middle = len(number) // 2
    if len(number) % 2 == 0:
        return sum(number[:middle]) == sum(number[middle:])
    else:
        return sum(number[:middle]) == sum(number[middle + 1:])