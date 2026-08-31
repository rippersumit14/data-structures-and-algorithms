"""
Test Result
75. Sort Colors
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

Example 2:

Input: nums = [2,0,1]

Output: [0,1,2]

Explanation:

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.
"""

nums = [1, 0, 0, 2, 1, 1]

# Three pointers
low = 0
mid = 0
high = len(nums) - 1

while mid <= high:

    # If current element is 0
    # Move it to the left side
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]

        low += 1
        mid += 1

    # If current element is 1
    # It is already in the correct middle region
    elif nums[mid] == 1:
        mid += 1

    # If current element is 2
    # Move it to the right side
    else:
        nums[mid], nums[high] = nums[high], nums[mid]

        high -= 1


print(nums)

























