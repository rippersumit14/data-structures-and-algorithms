'''recursiveRange
Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.

Examples

recursiveRange(6) # 21
recursiveRange(10) # 55 '''

def recursiveRange(n):
    #assert that n must be a positive value and integer
    assert n >= 0 and int(n) == n, "Positive integer and must be an integer"

    #Base case if n == 0, then return 0
    if n == 0:
        return 0

    #Recursive case
    return n + recursiveRange(n-1)

#the time and space complexity will be o(n)


print(recursiveRange(6))