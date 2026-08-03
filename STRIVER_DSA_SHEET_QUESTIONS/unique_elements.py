nums = [2,2,1,1,4,4,3]

nums.sort()

 #[2,2,1]
# #[1,2,2]

print(nums)

unique = 0

j = 0

for i in range(1, len(nums)): #
    if nums[i] != nums[j]:
        unique = nums[j]

print(unique)



