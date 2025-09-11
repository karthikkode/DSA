def reverseString(s):
    start = 0
    end = len(s)-1
    while start<=end:
        # Swap characters at start and end indices
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start+=1
        end-=1
    
    #approach 2
    n = len(s)
    for i in range(0, n//2):
        # Swap characters at i and n-1-i indices
        temp = s[i]
        s[i] = s[n-1-i]
        s[n-1-i] = temp

# Notes
# The function reverseString takes a list of characters s and reverses it in-place.
# It uses two pointers, start and end, to track the positions of characters to be swapped.
# The while loop continues until the start pointer is less than or equal to the end pointer.
# Inside the loop, it swaps the characters at the start and end indices.
# After swapping, it increments the start pointer and decrements the end pointer to move towards the center of the list.
# The process continues until all characters have been swapped, effectively reversing the list.
# An alternative approach is also provided, which uses a for loop to iterate through the first half of the list and swaps characters symmetrically from the start and end.
# This approach achieves the same result of reversing the list in-place.
