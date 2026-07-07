#Finding the factorial of a number using recursion
def factorial(n):
    #Input validation
    assert n >= 0 and int(n) == n, "Number must be non-negative integer"

    #Base case
    #0! = 1
    #1! = 1
    if n == 0 or n == 1:
        return 1

    #recursive case
    #n! = n * (n-1)!
    return n * factorial(n - 1)


