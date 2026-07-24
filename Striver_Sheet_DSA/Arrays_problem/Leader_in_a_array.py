'''
Problem: Leaders in an Array

Problem Statement:
Given an integer array arr of size n, return all the leaders in the array.

An element is called a leader if it is greater than or equal to every element to its right.
The rightmost element is always considered a leader because there are no elements to its right.

Return the leaders in the same order as they appear in the array.

Examples:

Example 1:
Input:
arr = [4, 7, 1, 0]

Output:
[7, 1, 0]

Explanation:
0 is the rightmost element, so it is always a leader.
1 is greater than all the elements to its right.
7 is greater than all the elements to its right.
4 is not a leader because 7 is greater than 4.

--------------------------------------------------

Example 2:
Input:
arr = [10, 22, 12, 3, 0, 6]

Output:
[22, 12, 6]

Explanation:
6 is the rightmost element, so it is always a leader.
12 is greater than all the elements to its right (3, 0, 6).
22 is greater than all the elements to its right (12, 3, 0, 6).
10 is not a leader because 22 is greater than 10.

--------------------------------------------------

Constraints:

1 <= n <= 10^5
-10^9 <= arr[i] <= 10^9

Function Signature:

def leaders(arr):
    pass

Expected Time Complexity:
O(n)

Expected Auxiliary Space:
O(1) (excluding the output array)

'''


#suppose an array [1,2,34,4,2,0]

#An elements is a leader if all it's right elements are equal or lesser

# Suppose an array
nums = [1, 2, 34, 4, 2, 0]

# Creating the leader array
arrLeader = []

# Traverse every element
for i in range(len(nums)):

    # Last element is always a leader
    if i == len(nums) - 1:
        arrLeader.append(nums[i])

    # Check if current element is greater than or equal
    # to every element on its right
    elif nums[i] >= max(nums[i + 1:]):
        arrLeader.append(nums[i])

print(arrLeader)

#Brute force apprach
#Tc and sc ==> o(n)



#Optimized way

nums2 = [1,2,34,4,2,0]

leaders = []

#Rightmost element
rightMost = nums2[-1]
leaders.append(rightMost)

for i in range(len(nums) - 2, -1, -1):
    if nums2[i] >= rightMost:
        leaders.append(nums2[i])
        rightMost = nums2[i]

#Reverse the leader array
leaders.reverse()

print(leaders)

#Tc - > o(n) and sc -> o(1)






















































