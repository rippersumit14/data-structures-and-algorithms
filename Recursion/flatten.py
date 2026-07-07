'''flatten
Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

Examples

flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]'''

# Flatten a nested list using recursion

def flatten(arr):

    # Input validation
    assert isinstance(arr, list), "Input must be a list"

    # Result list
    result = []

    # Traverse each element
    for item in arr:

        # If current element is a list,
        # flatten it recursively
        if isinstance(item, list):
            result.extend(flatten(item))

        # Otherwise, append the element
        else:
            result.append(item)

    return result


print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))

