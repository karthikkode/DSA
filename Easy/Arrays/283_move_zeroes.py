def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    z=-1
    for i in range(0, len(nums)):
        if z>=0:
            if nums[i] != 0:
                nums[z] = nums[i]
                nums[i] = 0
                z += 1
        else:
            if nums[i] == 0:
                z = i

# Notes
# Two pointers approach
# Time complexity: O(n)
# Space complexity: O(1)
# Iterate through the array with one pointer
# If a zero is found, mark its index with the other pointer
# If a non-zero is found and the zero pointer is marked, swap the values and move the zero pointer to the right