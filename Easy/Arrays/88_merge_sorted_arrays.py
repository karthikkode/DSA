def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    ptr1 = m - 1 # Pointer for the last element in the first m elements of nums1
    ptr2 = n - 1 # Pointer for the last element in nums2
    for i in range (len(nums1)-1, -1, -1): # Start from the end of nums1
        if ptr2<0 or (ptr1>=0 and nums1[ptr1] > nums2[ptr2]):
            nums1[i] = nums1[ptr1]
            ptr1-=1
        else:
            nums1[i] = nums2[ptr2]
            ptr2-=1

# Notes
# Please explain the code line by line in detail
# The function merge takes two sorted arrays, nums1 and nums2, and merges them into nums1 in-place.
# The parameters m and n represent the number of valid elements in nums1 and nums2 respectively.
# The function uses two pointers, ptr1 and ptr2, to track the current elements being compared in nums1 and nums2.
# It iterates from the end of nums1 to the beginning, placing the larger of the two elements pointed to by ptr1 and ptr2 into the current position in nums1.
# This approach ensures that we do not overwrite any elements in nums1 that have not yet been compared.
# The process continues until all elements from nums2 have been merged into nums1.
# The function does not return anything as it modifies nums1 in-place.