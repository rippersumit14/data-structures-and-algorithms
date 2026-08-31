nums = [1, 2, 2, 3]

left = 1

for right in range(1, len(nums)):

    # Found a new unique element
    if nums[right] != nums[left - 1]:

        # Swap unique element with the duplicate position
        nums[left], nums[right] = nums[right], nums[left]

        # Move left to the next position
        left += 1


final_k = 0

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        final_k += 1
    else:
        break

print(nums)

print(final_k)