def reverseString(s):
    """
    Reverses a given string s in-place.

    Args:
        s (str): The input string to be reversed.

    Returns:
        None: This function modifies the input string in-place and does not return anything.
    """
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
