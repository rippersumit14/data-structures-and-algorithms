#Write a function called productOfArray which takes the in an array of numbers and returns the product of them all

def productOfArray(arr):
    #input validation
    assert isinstance(arr, list), "Input must be a list"

    #Base case
    #Product of an empty array is 1
    if len(arr) == 0:
        return 1

    #Recursive case
    #First element * product of remaining array
    return arr[0] * productOfArray(arr[1:])

#the time and space complexity will be o(n^2)
#because of repeated list slicing



