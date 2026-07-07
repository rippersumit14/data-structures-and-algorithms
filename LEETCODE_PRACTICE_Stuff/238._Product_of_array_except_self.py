#Given an integer nums, Return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i]
#Brute force solution

arr = [1,2,3,4]

result = []

for i in range(len(arr)):
    product = 1

    for j in range(len(arr)):
        #skip the current index
        if i != j:
            product *= arr[j]

    result.append(product)

#Time-complexity->o(n^2)
#Space-complexity->o(n)

class Solution:
    def productExceptSelf(self,  List):

        n = len(list)

        # result array
        # first we store prefix products in it
        result = [1] * n

        # prefix = product of all elements on left side
        prefix = 1

        for i in range(n):

            # store product of left side
            result[i] = prefix

            # update prefix with current element
            prefix *=[list]

        # suffix = product of all elements on right side
        suffix = 1

        for i in range(n - 1, -1, -1):

            # multiply left product with right product
            result[i] *= suffix

            # update suffix with current element
            suffix *= list[i]

        return result

sol = Solution()

sol.productExceptSelf(nums=[1,12,2,3])

