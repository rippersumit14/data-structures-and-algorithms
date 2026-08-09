#Given an integer array nums, return true if any value appears more than once in the array, otherwise false

nums = [1,2,2,3,4,5,6]

setty = set(nums)

j = 0
for i in range(1, len(nums)):
    if nums[j] != nums[i]:
        print("true")
    else:
        print("false")

    i += 1
    j += 1

#O(n) time complexity
#o(1) space complexity


