def singleNumberHash(nums):
    hash_table = dict()
    for i in range(0, len(nums)):
        if nums[i] not in hash_table:
            hash_table[nums[i]] = 1
        else:
            hash_table[nums[i]]+=1
    for key in hash_table.keys():
        if hash_table[key] == 1:
            return key
    
def singleNumber(nums):
    res = None
    for ele in nums:
        if res is None:
            res = ele
        else:
            res = res ^ ele
    return res

#  Notes
# The XOR operation has the property that a ^ a = 0 and a ^ 0 = a.
# By XORing all numbers together, pairs of identical numbers cancel each other out, leaving only the unique number.
# This approach uses constant space and runs in linear time, making it efficient for this problem.
# Initialize a variable to hold the result of the XOR operations.
# Iterate through each number in the array, updating the result by XORing it with the current number.
# After processing all numbers, the result will be the single number that appears only once in the array.
        