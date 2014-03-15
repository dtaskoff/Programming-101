# returns True if the integer 'n' is a prime number
def is_prime(n):
    if n < 2:
        return False

    return all(map(lambda x: n % x != 0, range(2, n // 2 + 1)))

# returns the number of divisors of 'n'
def number_of_divisors(n):
    number = 2

    for i in range(2, n):
        if n % i == 0:
            number += 1
    return number
#   the short way:
#   return len([x for x in range(1, n + 1) if n % x == 0])

# returns True if 'n' has a prime number of divisors
def prime_number_of_divisors(n):
    return is_prime(number_of_divisors(n))