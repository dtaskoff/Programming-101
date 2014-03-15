# simplifies 'fraction' which is a tuple
# of the form (nominator, denominator)
def simplify_fraction(fraction):
    nom = fraction[0]
    denom = fraction[1]
    div = gcd(nom, denom)

    return (nom // div, denom // div)

# returns the greatest common divisor of 'a' and 'b':
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
#   here is the tail recursion version, but since
#   Python doesn't support TCO, I preferred the other one
#   if a == 0:
#       return b
#   return gcd(b % a, a)