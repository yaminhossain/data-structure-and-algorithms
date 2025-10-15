def getSingleNumber(nums):
    res=0
    for i in range(len(nums)):
        res ^=nums[i]
    return res
nums = [4,1,2,1,2]
res= getSingleNumber(nums)
print(res)

# Time complexity: O(n)
# Space complexity: O(1)