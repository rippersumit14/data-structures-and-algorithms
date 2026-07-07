# Callback function
def isOdd(num):
    return num % 2 != 0


# Recursive function
def someRecursive(arr, callback):

    # Input validation
    assert isinstance(arr, list), "Input must be a list"

    # Base Case
    # If array becomes empty, no element satisfied the condition
    if len(arr) == 0:
        return False

    # If the first element satisfies the callback
    if callback(arr[0]):
        return True

    # Recursive Case
    # Check the remaining elements
    return someRecursive(arr[1:], callback)


print(someRecursive([1, 2, 3, 4], isOdd))   # True
print(someRecursive([4, 6, 8, 9], isOdd))   # True
print(someRecursive([4, 6, 8], isOdd))      # False