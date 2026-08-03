#When you want to find the maximum subarray. it can be extended to minimum subarray

arr = [1,2,3,4,4,5,6]

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(current_sum)


nums = [2,1,0,1,0]

red = []
white = []
blue = []

for i in nums:
    if i == 0:
        red.append(i)
    elif i == 1:
        white.append(i)
    else:
        blue.append(i)

final = red + white + blue

print(final)

