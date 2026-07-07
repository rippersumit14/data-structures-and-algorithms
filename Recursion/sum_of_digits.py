'''
SUM OF DIGITS USING RECURSION

Given a positive integer n,
return the sum of all its digits.
'''

def sum_of_n(n):

    # checking if input is a positive integer
    assert n >= 0 and int(n) == n, "The number must be positive"

    # Base Case
    # when number becomes 0, stop recursion
    if n == 0:
        return 0

    # Recursive Case
    # last digit + sum of remaining digits
    return (n % 10) + sum_of_n(n // 10)

#time complexity->o(n)
#space-complexity->o(n)
#the time and space for the recursive calls will dependent on the d digit given in the function



print(sum_of_n(1234))