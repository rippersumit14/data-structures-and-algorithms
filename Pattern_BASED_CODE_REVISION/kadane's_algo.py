#When you want to find the maximum subarray. it can be extended to minimum subarray

arr = [1,2,3,4,4,5,6]

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(current_sum)

