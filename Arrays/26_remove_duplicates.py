"""
LeetCode Problem 26: Remove Duplicates from Sorted Array
------------------------------------------------------
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

This file contains two approaches to solve the problem, both using the two-pointer technique.
"""

# ----------------------
# Approach 1: Two Pointers (i, j)
# ----------------------
def removeDuplicates(nums):
    """
    Removes duplicates from a sorted array in-place and returns the new length.
    
    This function uses the two-pointer technique:
    - 'i' tracks the position of the last unique element found.
    - 'j' scans through the array.
    When a new unique element is found at 'j', it is moved to position 'i+1'.
    
    Args:
        nums (List[int]): A sorted list of integers (may contain duplicates).
    
    Returns:
        int: The length of the array after duplicates have been removed.
    
    Example:
        nums = [1, 1, 2]
        k = removeDuplicates(nums)
        # nums[:k] is now [1, 2]
    """
    # Edge case: If the array has only one element, it's already unique
    if len(nums) == 1:
        return 1

    # Initialize two pointers:
    # i: points to the last unique element
    # j: scans ahead for new unique elements
    i, j = 0, 0

    # Iterate through the array
    while j <= len(nums) - 1:
        if nums[i] == nums[j]:
            # If duplicate, move j forward
            j += 1
        else:
            # Found a new unique element at j
            # Place it next to the last unique element
            nums[i + 1] = nums[j]
            i += 1
            j += 1

    # The new length is i + 1 (since i is index-based)
    return i + 1

# Detailed Explanation for Approach 1:
# -----------------------------------
# - The array is sorted, so duplicates are always adjacent.
# - Pointer 'i' keeps track of the last unique element's index.
# - Pointer 'j' scans ahead to find the next unique element.
# - When nums[j] != nums[i], nums[j] is a new unique value.
# - We place nums[j] at nums[i+1] to keep all unique elements at the start.
# - At the end, the first (i+1) elements of nums are unique.
# - The function returns i+1, the count of unique elements.

# ----------------------
# Approach 2: Alternative Two Pointers (i, j) with Swapping
# ----------------------
def removeDuplicates(nums):
    """
    Alternative approach to remove duplicates from a sorted array in-place.
    Uses two pointers, but swaps elements to maintain unique values at the start.
    
    Args:
        nums (List[int]): A sorted list of integers (may contain duplicates).
    
    Returns:
        int: The length of the array after duplicates have been removed.
    
    Example:
        nums = [1, 1, 2, 2, 3]
        k = removeDuplicates(nums)
        # nums[:k] is now [1, 2, 3]
    """
    if len(nums) == 1:
        return 1

    j = 0  # j points to the last unique element
    for i in range(0, len(nums)):
        if nums[i] != nums[j]:
            # Swap the next position after last unique with the new unique value
            nums[i], nums[j+1] = nums[j+1], nums[i]
            j += 1
    # At this point, nums[:j+1] contains all unique elements
    print(f"Array after removing duplicates: {nums[:j+1]}")
    return j + 1

# Usage Example (for testing):
# ----------------------------
# The following line demonstrates how the function works.
# It will print the array after removing duplicates and return the count of unique elements.
removeDuplicates([1,4,4,5,6,7,7,8])