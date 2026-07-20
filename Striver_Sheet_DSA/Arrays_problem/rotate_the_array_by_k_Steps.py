"""
------------------------------------------------------------
189. Rotate Array
Medium
------------------------------------------------------------

Problem Statement

Given an integer array nums, rotate the array to the right
by k steps, where k is non-negative.

You must modify the array in-place.

------------------------------------------------------------
Example 1

Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]

Explanation:

Rotate 1 step:
[7,1,2,3,4,5,6]

Rotate 2 steps:
[6,7,1,2,3,4,5]

Rotate 3 steps:
[5,6,7,1,2,3,4]

------------------------------------------------------------
Example 2

Input:
nums = [-1,-100,3,99]
k = 2

Output:
[3,99,-1,-100]

Explanation:

Rotate 1 step:
[99,-1,-100,3]

Rotate 2 steps:
[3,99,-1,-100]

------------------------------------------------------------
Constraints

1 <= nums.length <= 10^5

-2^31 <= nums[i] <= 2^31 - 1

0 <= k <= 10^5

------------------------------------------------------------
Definition

One Right Rotation:

Take the LAST element of the array
and move it to the FRONT.

Shift every other element one position
to the RIGHT.

Example:

Before:
[1,2,3,4,5]

After one right rotation:
[5,1,2,3,4]

------------------------------------------------------------
Function Signature

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

------------------------------------------------------------
Hints

1. What if k is greater than the array length?

2. Can you rotate without creating another array?

3. Can you solve it in O(n) time?

4. Think about reversing parts of the array.

------------------------------------------------------------
Time Complexity Target

O(n)

------------------------------------------------------------
Space Complexity Target

O(1)

------------------------------------------------------------
"""

listy = [1,2,3,4,5,6,7]
print(listy)

k = 3

#Creating the empty list with the rotation according to the k value
rotated_list = []

for i in range(len(listy), k + 1, -1):
    rotated_list.append(i)

final_rotated = []

rotated_list.reverse()
print(rotated_list)

for i in range(len(listy), k+1, -1):
    listy.remove(i)

print(listy)


result = rotated_list + listy
print(result)


listy2 = [1,2,3,4,5,6,7,8]

print(listy2)
#Reverse the whole array
listy2.reverse()


left = 0
right = k - 1
while left < right:
    listy2[left], listy2[right] = listy2[right],  listy2[left]

    left += 1
    right -= 1

left = k
right = len(listy2) - 1

while left < right:
    listy2[left], listy2[right] = listy2[right], listy2[left]
    left += 1
    right -= 1

print(listy2)



#Time-complexity->o(n)
#Space-complexity->o(1)






















