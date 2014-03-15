# returns the number containing the 'digits'
def list_to_number(digits):
    number = 0

    for digit in digits:
        number *= 10
        number += digit
        
    return number