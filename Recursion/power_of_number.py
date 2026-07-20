#How to calculate the power of a number using recursion

def power(n, exponent):
    assert int(exponent) == exponent,'The exponent must be integer only'
    if exponent == 0:
        return 1 #base case
    return  n * power(n, exponent-1)

print(power(2, 3))




