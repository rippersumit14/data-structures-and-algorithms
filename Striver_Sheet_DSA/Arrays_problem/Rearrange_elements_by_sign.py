'''
Problem: Rearrange Array Elements by Sign

Problem Statement:

You are given an array of even length.

The array contains:
- Equal number of positive integers.
- Equal number of negative integers.

Your task is to rearrange the array such that:

1. The first element is always positive.

2. Every consecutive pair has opposite signs.
   (+, -, +, -, +, - ...)

3. The relative order of positive numbers must remain the same.

4. The relative order of negative numbers must remain the same.

Return the rearranged array.

--------------------------------------------------

Example 1:

Input:
nums = [3,1,-2,-5,2,-4]

Output:
[3,-2,1,-5,2,-4]

Explanation:

Positive numbers:
[3,1,2]

Negative numbers:
[-2,-5,-4]

Interleave them while preserving their order.

--------------------------------------------------

Example 2:

Input:
nums = [-1,1]

Output:
[1,-1]

--------------------------------------------------

Constraints:

2 <= nums.length <= 2 * 10^5

nums.length is even.

The number of positive integers is equal to
the number of negative integers.

'''

nums = [3,1,-2,-5,2,-4]

#Using the unpotimized way
 #Using two different list to store positive and negaive in the same order
positive = []
negative = []

for i in nums:
    if i >= 0:
        positive.append(i) #[3,1,2]

for j in nums:
    if j <= 0:
        negative.append(j) #[-2,-5-,4]

        #Creating the final array
final = []



for i in range(len(positive)):
    final.append(positive[i])
    final.append(negative[i])

print(final)

