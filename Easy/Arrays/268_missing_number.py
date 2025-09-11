def missingNumber(nums):
    n = len(nums)
    totalSum = (n*(n+1))/2
    print(totalSum)
    actualSum = 0
    for i in range(0, len(nums)):
        actualSum+=nums[i]
    
    return int(totalSum - actualSum)

# Notes
# Calculate the expected sum of the first n natural numbers using the formula n(n+1)/2.
# Calculate the actual sum of the numbers present in the array.
# The missing number is the difference between the expected sum and the actual sum.