#Given an array, we have to find the largest element in the array
'''
Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}
Output:
 5
Explanation:

5 is the largest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}
Output:
 10
Explanation:

10 is the largest element in the array.
'''

class solution:
    def max_largest(self, nums: list):

        # Assume first element is the largest
        maxi = nums[0]

        # Traverse through the array
        for i in range(1, len(nums)):

            # If current element is greater than
            # the largest value found so far
            if nums[i] > maxi:
                maxi = nums[i]

        return maxi


solution_class = solution()

nums = [1, 2, 3, 4, 5]

result = solution_class.max_largest(nums)

print(result)

#The time complexity of the code will be o(n)
#The space complexity of the code will be o(1)

























