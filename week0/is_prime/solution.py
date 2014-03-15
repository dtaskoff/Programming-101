# returns True if the integer 'n' is a prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True
#   the short way:
#   if n < 2:
#       return False
#
#   return all(map(lambda x: n % x != 0, range(2, n // 2 + 1)))