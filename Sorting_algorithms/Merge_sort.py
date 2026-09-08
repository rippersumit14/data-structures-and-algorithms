#Merge sort algorithm is divide_and_conquerer algorithm
#That sorts the array by first breaking it down into smaller arrays and then building back the
#array back together the correct way so that is sorted

def merge_sort(arr):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(right_half, left_half)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left)  and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1


    result.extend(left[i:])
    result.extend(right[j:])

    return result

#Time complexity => o(n log n)
#Space complexity => o(n)

