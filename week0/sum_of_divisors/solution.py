# returns the sum of all divisors of the integer 'n'
def sum_of_divisors(n):
    sum = n

    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum
    
#   and the short way:
#   return sum([x for x in range(1, n + 1) if n % x == 0])