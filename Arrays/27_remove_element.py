"""
LeetCode Problem 27: Remove Element
----------------------------------
Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

This file contains a two-pointer approach to solve the problem efficiently.
"""

def removeElement(nums, val):
    """
    Removes all instances of 'val' from the list 'nums' in-place and returns the new length.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    This function uses a two-pointer technique:
    - 'i' scans through the array.
    - 'j' keeps track of the position to place the next non-'val' element.
    - When nums[i] != val, we place nums[i] at nums[j] and increment j.
    - If nums[i] == val, we skip it.

    Args:
        nums (List[int]): The input list of integers.
        val (int): The value to remove from the list.

    Returns:
        int: The length of the array after removing all instances of 'val'.

    Example:
        nums = [3,2,2,3,4]
        k = removeElement(nums, 3)
        # nums[:k] is now [2, 2, 4]
    """
    j = 0
    for i in range(0, len(nums)):
        if nums[j] != val:
            j += 1
        elif nums[j] == val and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    print(nums[:j])
    return j

removeElement([3,2,2,3,4], 3)