# When you need to find something in all subarrays/substrings of fixed size k
# Used in network packet analysis, fixed size log data

array_1 = [1, 3, 2, -1, -4, 1, 8, 2]

def max_sum_subArray_k(arr, k):

    # sum of first window
    window_sum = sum(arr[:k])

    # initialize max sum
    max_sum = window_sum

    # slide the window
    for i in range(k, len(arr)):

        # add incoming element
        # remove outgoing element
        window_sum += arr[i] - arr[i - k]

        # update maximum sum
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sum_subArray_k(array_1, 4))

